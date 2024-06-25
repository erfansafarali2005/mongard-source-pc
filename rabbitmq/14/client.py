import pika 

credentials = pika.PlainCredentials('guest' , 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='alt' , exchange_type='fanout') # alternative exchange
ch.exchange_declare(exchange='main' , exchange_type='direct')# main exchange         


ch.basic_publish(exchange='mian' , routing_key='home' , body='hello world')

print('sent')

connection.close()