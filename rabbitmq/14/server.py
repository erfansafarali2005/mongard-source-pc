import pika 

credentials = pika.PlainCredentials('guest' , 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='alt' , exchange_type='fanout')
ch.exchange_declare(exchange='main' , exchange_type='direct' , arguments={'alternate-exchange' : 'alt'}) #alternate-exchange is ghardady 

ch.queue_declare(exchange='altq' , exchange_type='fanout')
ch.queue_bind('altq' , 'alt') #no routing key becasue of fanout exchange           | queue is decleared and binded to its exchange

ch.queue_declare('mainq')
ch.queue_bind('mainq' , 'main' , routing_key='home') #main sends requests to mainq with home routing_key

def alt_callback(ch , method , properties , body):
    print(f'Alt: {body}')

def main_callback(ch , method , properties , body):
    print(f'Main : {body}')

ch.basic_consume(queue='altq' , on_message_callback=alt_callback , auto_ack=True) 
ch.basic_consume(queue='mainq' , on_message_callback=main_callback , auto_ack=True)      


print('start consuming ...')

ch.start_consuming()