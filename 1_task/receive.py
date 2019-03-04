#!/usr/bin/env python
import pika
import traceback
import sys
import time


time.sleep(20)
connection = pika.BlockingConnection(pika.ConnectionParameters(host= "rabbit", socket_timeout = 15))
channel = connection.channel()

channel.queue_declare(queue='task_random')

print("Waiting for messages.")

def callback(ch, method, properties, body):
    print("get:", body, flush = True)

channel.basic_consume(callback, queue='task_random')

try:
    channel.start_consuming()
except pika.exceptions.ConnectionClosed:
    channel.stop_consuming()
    time.sleep(20)
    traceback.print_exc(file=sys.stdout)

connection.close()
