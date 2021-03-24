import configparser
import json

import pika

config = configparser.ConfigParser()
config.read('config.ini')
params = pika.URLParameters(config['rabbitmq']['uri'])

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
