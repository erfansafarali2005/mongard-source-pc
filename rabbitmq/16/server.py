import pika

credentials = pika.PlainCredentials('guest' , 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost') , credentials=credentials)
ch = connection.channel()

ch.exchange_declare(exchange='aj' , exchange_type='fanout')
ch.queue_declare(queue='main')
ch.queue_bind('main' , 'aj')

def callback(ch , method , properties , body):
    if method.delivery_tag %5 ==0:
        ch.basic_nack(delivery_tag=method.delivery_tag , requeue=False , multiple=True) #if the delivery tag % 5 is 0 : its gonna be negative acknowledge | requeue : if True , the request will be requeued again | multiple : to accept and process multiple reqeuests at the same time 
    print(f'recieved {method.delivery_tag}')

ch.basic_consume(queue='main' , on_message_callback=callable)
print('start consuming ...')
ch.start_consuming()          