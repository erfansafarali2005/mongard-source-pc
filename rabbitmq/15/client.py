# if the request won't reach the consumer , its a dead letter and it will be sent to the dead letter queue

import pika

credentials = pika.PlainCredentials('guest' , 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost') , credentials=credentials)
ch = connection.channel()

ch.exchange_declare(exchange='main' , exchange_type='direct')
ch.basic_publish(exchange='main' , routing_key='home' , body='hello world')

print('sent ..')
connection.close()