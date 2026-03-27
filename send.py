import pika
import time
import socket

hostname = socket.gethostname()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='Post Office', durable=True, arguments={'x-queue-type': 'quorum'})

# Send messages once per second with counter
counter = 1
while True:
    message = f"My name is Gavin and I love Python! {counter}"
    channel.basic_publish(exchange='',
                        routing_key='Post Office',
                        body=message)
    print(f" {hostname} Sent '{message}'")
    counter += 1
    time.sleep(1)