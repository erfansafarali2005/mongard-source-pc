import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) #we set up our connection which is Blocking type | for parameters we use pika.ConnectionParameters class | host : is the adress of your host

ch = connection.channel() #so now we declare a channel

ch.queue_declare(queue='one') #so now we declare a queue with the name of one
ch.basic_publish(exchange='' , routing_key='one' , body="hello world") # now we publish a request basically | exchange ='' -> means direct exchange | routing_key is the queue | body : **
print(("message sent ..."))
connection.close() # in order to save resources after all we close our connection