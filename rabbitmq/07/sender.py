<<<<<<< HEAD
import pika
import time

credentials = pika.PlainCredentials('username' , 'password')
connection = pika.BaseConnection(pika.ConnectionParameters(host='localhost'),credentials=credentials)
ch = connection.channel()


ch.queue_declare(queue='one')
ch.basic_publish(exchange='' , routing_key='one' , body='Hello world' , properties=pika.BasicProperties(

   ### see https://www.rabbitmq.com/publishers.html for properties ###
   content_type='text/plain',
   content_encoding='gzip',
   timestamp='10000',
   expiration=str(time.time), #-> if expiration time is done , the message wont be sended to the broker
   delivery_mode=1, ## 1 -> saved on memory , 2 -> saved also on disk : on disk it has negative aspect on performance , if it is on 1 -> if server crashs it wont be recovered like logging , but on payment we use 2 to be saved on disk 
   user_id='10',
   app_id = '11',
   headers={'name' : 'amir' , 'age' : '30'}, #headers must be map , can be used when using header exchange method
))
print('message send...')
=======
import pika
import time

credentials = pika.PlainCredentials('username' , 'password')
connection = pika.BaseConnection(pika.ConnectionParameters(host='localhost'),credentials=credentials)
ch = connection.channel()


ch.queue_declare(queue='one')
ch.basic_publish(exchange='' , routing_key='one' , body='Hello world' , properties=pika.BasicProperties(

   ### see https://www.rabbitmq.com/publishers.html for properties ###
   content_type='text/plain',
   content_encoding='gzip',
   timestamp=int(time.now),
   expiration=str(time.time), #-> if expiration time is done , the message wont be sended to the broker
   delivery_mode=1, ## 1 -> saved on memory , 2 -> saved also on disk : on disk it has negative aspect on performance , if it is on 1 -> if server crashs it wont be recovered like logging , but on payment we use 2 to be saved on disk 
   user_id='10',
   app_id = '11',
   headers={'name' : 'amir' , 'age' : '30'}, #headers must be map , can be used when using header exchange method
))
print('message send...')
>>>>>>> 0a1e8d14f3bcf356f7d22729fa32779236fb71d5
connection.close()