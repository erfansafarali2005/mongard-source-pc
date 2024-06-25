import pika


credentials = pika.PlainCredentials('guest' , 'guest')
connection = pika.BaseConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()


ch.queue_declare('request-queue')


def on_request_message_recieved (ch , method , proeprties , body):
    print(f'recieved request : {proeprties.correlation_id}')
    ch.basic_publich('' , routing_key = proeprties.reply_to , body=f'replying to {proeprties.correlation_id}')



ch.basic_consume('request-queue' , auto_ack=True , on_message_callback=on_request_message_recieved)

print('starting server')
ch.start_consuming()