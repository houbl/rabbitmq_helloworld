#!/usr/bin/env python
import pika
import sys
import json
import socket

# RabbitMQ Server
broker = 'elephant109.heprc.uvic.ca'
queue = 'squiddata'

def amqp_send(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
                    broker, 5672))
    channel = connection.channel()

    channel.queue_declare(queue=queue)

    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=data)
    print " [x] Sent ",data
    connection.close()

data = {}
data['hostname'] = socket.gethostname()
data['key2'] = "value"

json_str = json.dumps(data)

amqp_send(json_str)







#result = channel.exchange_declare(exchange='logs',
#				  type='fanout')
#
#
#channel.basic_publish(exchange='logs',
#                      routing_key='',
#                      body=message)
#print " [x] Sent %r" % (message,)
