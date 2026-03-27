import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='Post Office', durable=True, arguments={'x-queue-type': 'quorum'})

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body= 'Mail')
print(" [gavin] Sent 'You got mail'")

connection.close()
