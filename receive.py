#!/usr/bin/env python
import pika
import json
import os
import time

# RabbitMQ Server
host = 'elephant109.heprc.uvic.ca'
queue = 'squiddata'
json_folder = '/home/mchester/rabbitmq_helloworld/dumps'

connection = pika.BlockingConnection(pika.ConnectionParameters(
	host,5672))
channel = connection.channel()

channel.queue_declare(queue=queue)

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    data = json.loads(body)
    file = '{0}.json'.format(os.path.join(json_folder,data['hostname']))

    print " [x] Received {0}.".format(data['hostname'])
    print data


channel.basic_consume(callback,
		      queue=queue,
		      no_ack=True)

channel.start_consuming()
