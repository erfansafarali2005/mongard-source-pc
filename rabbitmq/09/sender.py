import pika
import time

credentials = pika.PlainCredentials('username' , 'password')
connection = pika.BaseConnection(pika.ConnectionParameters(host='localhost'),credentials=credentials)
ch = connection.channel()


### !! we dont declare any queue because we use fanout exchange and it will connect to any queue that it finds

ch.exchange_declare(exchange='logs' , exchange_type='fanout')

ch.basic_publish(exchange='logs' , routing_key='' , body='fanout exchange ..') #no routing key needed because of the fanout exchange | fanout dosn't need queue

print('message sent')

