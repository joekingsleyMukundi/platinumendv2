import pika
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Connect to RabbitMQ
params = pika.URLParameters(os.getenv('RABBITMQ_URL'))
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Create a queue
def publish (method, body):
  properties = pika.BasicProperties(method)
  print(body)
  channel.basic_publish(exchange='', routing_key='customer', body=json.dumps(body), properties=properties)
  connection.close()