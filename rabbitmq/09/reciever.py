<<<<<<< HEAD
import pika
import time

credentials = pika.PlainCredentials('username' , 'password')
connection = pika.BaseConnection(pika.ConnectionParameters(host='localhost'),credentials=credentials)
ch = connection.channel()

### we declare exchange on the boths sides becasue we dont know if sender starts first or the reciever ###


ch.exchange_declare(exchange='logs' , exchange_type='fanout')
result = ch.queue_declare(queue='',exclusive=True) #if qeueu name is empty it creates a queue by a choosen name by rabbitmq | exclusive -> this queueu is exclusive to the consumer , if consumer lost connection or the oprations is done , the qeueu will be deleted(like models in django)

### when ever the reciever is started an exclusive queue will get opens and fanout sender , sends the request to these exclusive queues ###


### now we should connect that queue to the exchange with binding ###

ch.queue_bind(exchange='logs' , queue='result.method.queue')

print('wating for logs ...')
print(result.method.queue)

def callback(ch , method , properties , body):
    print(f'recieved {body} in reciever1')


ch.basic_consume(queue=result.method.queue , on_message_callback=callback , auto_ack=True)
=======
import pika
import time

credentials = pika.PlainCredentials('username' , 'password')
connection = pika.BaseConnection(pika.ConnectionParameters(host='localhost'),credentials=credentials)
ch = connection.channel()

### we declare exchange on the boths sides becasue we dont know if sender starts first or the reciever ###


ch.exchange_declare(exchange='logs' , exchange_type='fanout')
result = ch.queue_declare(queue='',exclusive=True) #if qeueu name is empty it creates a queue by a choosen name by rabbitmq | exclusive -> this queueu is exclusive to the consumer , if consumer lost connection or the oprations is done , the qeueu will be deleted(like models in django)

### when ever the reciever is started an exclusive queue will get opens and fanout sender , sends the request to these exclusive queues ###


### now we should connect that queue to the exchange with binding ###

ch.queue_bind(exchange='logs' , queue='result.method.queue')

print('wating for logs ...')
print(result.method.queueu)

def callback(ch , method , properties , body):
    print(f'recieved {body}')


ch.basic_consume(queue=result.method.queue , on_message_callback=callback , auto_ack=True)
>>>>>>> 0a1e8d14f3bcf356f7d22729fa32779236fb71d5
ch.start_consuming()