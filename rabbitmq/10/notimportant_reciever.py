import pika

credentials = pika.PlainCredentials('guest' , 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credentials))
ch = connection.channel()


ch.exchange_declare(exchange='topic_logs' , exchange_type='topic')

result = ch.queue_declare(queue='' , exclusive=True , ) #whenever consumer is closed the qeuue will be terminated

ch.queue_bind(exchange='topic_logs' , queue=result.method.queue , routing_key='*.*.notimportant') #  *.*.notimportant -> the first and second pairs are not important , only look for the last part  | '#.important'
print('waiting for messages ...')


def callback(ch , method , properties , body):
    print(body)


ch.basic_consume(queue=result.method.queue , on_message_callback=callback , auto_ack=True)    