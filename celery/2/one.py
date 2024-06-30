from celery import Celery
import time


app = Celery('one' , broker='amqp://guest:guest@localhost:5672') #5672 is for rabbitmq

# >> celery -A one  :

'''

    we have appname 
    we have trasprot which is the queueing app -> rabbitmq
    concurency : number of cpu cores
    queues : the main queue -> exchange = celery(direct) routingkey = celery -> rabbitmq queue and exchange

'''

# >> celery -A one -l info/debug/fatal/warning/ciritical -> it shows the error with the custom level


