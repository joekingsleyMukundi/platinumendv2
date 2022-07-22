import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'customers.settings')

django.setup()
import json
import pika
from users.models import Users
from client.models import Client
from employers.models import Employer, Company
from dotenv import load_dotenv


load_dotenv()
# connexting to then rabbitmq server


params = pika.URLParameters(os.getenv('RABBITMQ_URL'))
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='auth')


def callback(ch, method, properties, body):
    print('message recived in consumer with this properties: ', properties.content_type)
    props = properties.content_type
    data = json.loads(body)
    try:
        if props=='user_created':
            user = Users.objects.create(user_id=data['user_id'], name=data['username'], email=data['email'],
                                        phone=data['phone'], role=data['role'], is_verified=data['is_verified'],
                                        is_active=data['is_active'])
            return

        elif props=='employer_activated':
            employer = Employer.objects.create(employer_id=data['employer_id'], username=data['username'],
                                                email=data['email'], phone=data['phone'],
                                                is_verified=data['is_verified'])
            return

        elif props=='company_set':
            employer_id = data['owner']['id']
            employer = Employer.objects.get(employer_id=employer_id)
            company = Company.objects.create(company_id=data['id'], owner=employer, name=data['name'],
                                                email=data['email'], phone=data['phone'])
            return company

        elif props == 'client_activated':
            client = Client.objects.create(client_id=data['client_id'], name=data['username'], email=data['email'],
                                            phone=data['phone'], is_verified=data['is_verified'])
            return 
    except Exception as e:
        print(e)
        raise InternalServerError()


channel.basic_consume(queue='auth', on_message_callback=callback, auto_ack=True)
print('started consuming')
channel.start_consuming()
channel.close()
