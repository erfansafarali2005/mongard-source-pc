import pika 

credentials = pika.PlainCredentials('guest' , 'guest')
Connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = Connection.channel()

ch.exchange_declare(exchange='a' , exchange_type='direct')
ch.exchange_declare(exchange='z' , exchange_type='fanout')
ch.exchange_bind('z' , 'a') #two exchanges are connected togheter 

ch.basic_publish(exchange='a' , routing_key='' , body='hello world')

print('sent ..')
Connection.close()