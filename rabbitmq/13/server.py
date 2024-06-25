import pika 

credentials = pika.PlainCredentials('guest' , 'guest')
Connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = Connection.channel()

ch.exchange_declare(exchange='z' , exchange_type='fanotu')
ch.queue_declare(queue='mongard')
ch.queue_bind('mongard' , 'z') #queue is connected to the relative exchange 


def callback(ch , method , properties , body):
    print(f'recieved : {body}')

ch.basic_consume(queue='mongard' , auto_ack=True , on_message_callback=callback)
print('start consuming ..')
ch.start_consuming()    