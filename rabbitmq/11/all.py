import pika

credentials = pika.PlainCredentials('guest' , 'guest')
connection = pika.BaseConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='he' , exchange_type='headers')
ch.queue_declare('hq-all')

bind_args = {'x-match':'all' , 'name':'mongard' , 'age' : '5'}


def callback(ch , method , properties , body):
    print(f'recived {body}')

ch.queue_bind('hq-all', 'any' ,arguments=bind_args)
ch.basic_consume('hq-all' , auto_ack=True,on_message_callback=callback)

print('wating')
ch.start_consuming()