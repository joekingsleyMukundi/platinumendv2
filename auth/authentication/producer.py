import pika
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Connect to RabbitMQ
params = pika.URLParameters(os.environ['RABBITMQ_URL'])
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Create a queue
def publish (method, body):
  properties = pika.BasicProperties(method)
  print(body)
  channel.basic_publish(exchange='', routing_key='auth', body=json.dumps(body), properties=properties)
  connection.close()