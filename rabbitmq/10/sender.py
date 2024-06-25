<<<<<<< HEAD
import pika

credentials = pika.PlainCredentials('guest' , 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='topic_logs' , exchange_type='topic') # topic exchange type which is about the pairs of names to be true _> so it dosn't need queue


messages = {

    'error.warning.important' : 'this is an important message',
    'info.debug.notimportant' : 'this is not an important message',
    # ^      ^        ^

}

for k,v in messages.items():
    ch.basic_publish(exchange='topic_logs' , routing_key=k , body=v)

print('sent message ..')
=======
import pika

credentials = pika.PlainCredentials('guest' , 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='topic_logs' , exchange_type='topic') # topic exchange type which is about the pairs of names to be true 


messages = {

    'error.warning.important' : 'this is an important message',
    'info.debug.notimportant' : 'this is not an important message'
    # ^      ^        ^

}

for k,v in messages.items():
    ch.basic_publish(exchange='topic_logs' , routing_key=k , body=v)

print('sent message ..')
>>>>>>> 0a1e8d14f3bcf356f7d22729fa32779236fb71d5
connection.close()