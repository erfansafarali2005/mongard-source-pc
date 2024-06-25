import pika
import uuid 

credentials = pika.PlainCredentials('guest' , 'guest')
connection = pika.BaseConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()


reply_queue = ch.queue_declare(queue='' , exclusive=True)

def on_reply_message_recieve(ch , method , properties , body):
    print(f'recived {body}')

ch.basic_consume(queue=reply_queue , auto_ack=True , on_message_callback=on_reply_message_recieve)

ch.queue_declare(queue='request-queue')

cor_id = str(uuid.uuid4())  # a correleation id , create dby uuid library

print(f'sending request :{{cor_id}}')

ch.basic_publish('' , routing_key='request-queue',properties=pika.BasicProperties(
    reply_to=reply_queue.method.queue,
    correlation_id=cor_id,
    body='can i request a reply ?'))

print('start client ')

ch.start_consuming()

