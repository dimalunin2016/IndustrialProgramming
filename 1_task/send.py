#!/usr/bin/env python
import pika
import time
import random
import sys

def sleeps():
    time.sleep(5)

def connect():
    conn_params = pika.ConnectionParameters(host = "rabbit")
    connection = pika.BlockingConnection(conn_params)
    channel = connection.channel()
    channel.queue_declare(queue='task_random')
    return channel, connection

sleeps()
while True:
    try:
        channel, connection = connect()
        while True:
            number = random.randint(-100, 100)
            sleeps()
            print('sending:', number, flush = True)
            channel.basic_publish(exchange='',
			  routing_key='task_random',
			  body=str(number))
    except pika.exceptions.ConnectionClosed:
        sleeps()
        print("lost connection")

sleeps()
connection.close()
