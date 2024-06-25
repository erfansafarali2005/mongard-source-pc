import pika
import time

### round robin method -> sends the requests of users to the servers in a clear order way 
### in order to prevent over populated servers , we use acknowledge signals for receiver to tell clients that send your request to the server which is not busy



connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.queue_declare(queue='one')


def callback(ch , method , properties , body): #properties here are the properties which are coming from sender 
    
    print(f'recieved : {body}')
    print(properties)
    print(properties.app_id) 
    time.sleep(5)
    print('done ..')
    ch.basic_ack(delivery_tag = method.delivery_tag)

ch.basic_qos(prefetch_count=1)  #prefetch_count -> how many requets should be sent to the servers at the same time 

ch.basic_consume(queue='one' , on_message_callback=callback ) # -> auto_ack is removed due to ch.basic_ack in the function

print("wating for messages, to exit press ctrl + c")

ch.start_consuming() 


