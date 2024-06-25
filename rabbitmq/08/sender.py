import pika
import time

credentials = pika.PlainCredentials('username' , 'password')
connection = pika.BaseConnection(pika.ConnectionParameters(host='localhost'),credentials=credentials)
ch = connection.channel()


ch.queue_declare(queue='one')
ch.basic_publish(exchange='' , routing_key='one' , body='Hello world' , properties=pika.BasicProperties(


   content_type='text/plain',
   content_encoding='gzip',
   timestamp=int(time.now),
   expiration=str(time.time),
   delivery_mode=1, 
   user_id='10',
   app_id = '11',
   headers={'name' : 'amir' , 'age' : '30'}, 
))
print('message send...')
connection.close()