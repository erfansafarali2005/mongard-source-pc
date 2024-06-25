import pika

credentials = pika.PlainCredentials('guest' , 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost') , credentials=credentials)
ch = connection.channel()

ch.exchange_declare(exchange='main' , exchange_type='direct')
ch.exchange_declare(exchange='dlx' , exchange_type='fanout') # an exchange for dead letters

ch.queue_declare(queue='mainq' , arguments={'x-dead-letter-exchange':'dlx' , 'x-message-ttl':5000 , 'x-max-lenght':100})
#                                             ^-> the exchange of deadletter        ^->time to live        ^-> the max lenght -> if any of this conditions go false : the message is gonna to be deadletter
ch.queue_bind('mainq' , 'main' , 'home')

ch.queue_declare('dlxq')
ch.queue_bind('dlxq' ,  'dlx')
def dlx_callback(ch , method , properties , body):
    print(f'dead letter : {body}')

ch.basic_consume(queue='dlxq' , on_message_callback=dlx_callback , auto_ack=True)

print('start consume ..')
ch.start_consuming()