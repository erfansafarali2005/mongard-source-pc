import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.queue_declare(queue='one')

###

# why do we declare these stuffs again ? -> we dont know if the request is firstly sent from the client or the server , if the queue exists it goes through , if it dosn't it creats

###
def callback(ch , method , properties , body): #these args are vital
    print(f'recieved : {body}')

ch.basic_consume(queue='one' , on_message_callback=callback , auto_ack=True) #now we basically consume the requeust | queue -> the name of the queue | on_message_callback : the function which starts after receiving the requests | auto_ack -> a message which is sent to the client and says : i suscessfully recieved the message
print("wating for messages, to exit press ctrl + c")
ch.start_consuming() #now we start the server


#even if our servers are down , after restarting , the requests will come through the reciever (so we ususally set senders in client)