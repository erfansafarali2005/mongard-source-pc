import pika

credentials = pika.PlainCredentials('guest' , 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost') , credentials=credentials)
ch = connection.channel()

ch.exchange_declare(exchange='main' , exchange_type='direct' , durable=True , auto_delete=False)
ch.queue_declare(queue='mainq' , durable=True , exclusive=False , auto_delete=False)

def callback(ch , method , properties , body):
    print(body)

ch.basic_consume(queue='mainq' , on_message_callback=callback)
print('start consuming ...')
ch.start_consuming()    