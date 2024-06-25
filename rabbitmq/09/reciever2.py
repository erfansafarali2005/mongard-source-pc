import pika

credentials = pika.PlainCredentials('username' , 'password')
connection = pika.BaseConnection(pika.ConnectionParameters(host='localhost'),credentials=credentials)
ch = connection.channel()



ch.exchange_declare(exchange='logs' , exchange_type='fanout')
result = ch.queue_declare(queue='',exclusive=True) #if qeueu name is empty it creates a queue by a choosen name by rabbitmq | exclusive -> this queueu is exclusive to the consumer , if consumer lost connection or the oprations is done , the qeueu will be deleted(like models in django)




ch.queue_bind(exchange='logs' , queue='result.method.queue')

print('wating for logs ...')
print(result.method.queue)

def callback(ch , method , properties , body):
    print(f'recieved {body} in recieve 2 ')


ch.basic_consume(queue=result.method.queue , on_message_callback=callback , auto_ack=True)
ch.start_consuming()


# now if we run both receivers , we recieve messages in both recievers