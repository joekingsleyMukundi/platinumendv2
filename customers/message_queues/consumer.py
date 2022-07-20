import json
import pika
import os

from dotenv import load_dotenv

load_dotenv()
# connexting to then rabbitmq server
params = pika.URLParameters(os.getenv('RABBITMQ_URL'))
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='auth')

def callback (ch, method, properties, body):
  print ('message recived in consumer')
  data = json.loads(body)
  print(data)

channel.basic_consume(queue='auth',on_message_callback=callback, auto_ack=True)
print('started consuming')
channel.start_consuming()
channel.close()