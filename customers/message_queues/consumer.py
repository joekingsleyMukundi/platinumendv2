import json
import pika
import os

from dotenv import load_dotenv
from users.models import User
from employers.models import Employer
from client.models import Client
from errors.custom_internal_server_error import InternalServerError
load_dotenv()
# connexting to then rabbitmq server
params = pika.URLParameters(os.getenv('RABBITMQ_URL'))
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='auth')

def callback (ch, method, properties, body):
  print ('message recived in consumer with this properties: ', properties.content_type)
  data = json.loads(body)
  try:
    switch (properties.content_type){
      case 'user_created':
        user = User.objects.create(user_id=data['user_id'], name=data['username'], email=data['email'], phone=data['phone'], role=data['role'], is_verified=data['is_verified'], is_active=data['is_active'])
        break;
      case 'employer_activated':
        employer = Employer.objects.create(employer_id=data['employer_id'], username=data['username'], email=data['email'], phone=data['phone'], is_verified=data['is_verified'])
        break;
      case 'company_set':
        employer_id = data['owner']['id']
        employer = Employer.objects.get(employer_id=employer_id)
        company = Company.objects.create(company_id=data['id'], owner=employer, name=data['name'], email=data['email'], phone=data['phone'])
        break;
      case 'client_activated':
        client = Client.objects.create(client_id=data['client_id'], name=data['username'], email=data['email'], phone=data['phone'], is_verified=data['is_verified'])
        break;
    }
  except Exception as e:
    print(e)
    raise InternalServerError();

channel.basic_consume(queue='auth',on_message_callback=callback, auto_ack=True)
print('started consuming')
channel.start_consuming()
channel.close()