from celery import Celery , chain , group

app = Celery('one' , broker='amqp://guest:guest@localhost:5672')

app.config_from_object('celery_conf')


@app.task(name='one.add')
def add(a,b):
    return a + b

@app.task(name='one.sub')
def sub(c,d):
    return c - d


"""
    prefork : cpu bound proccess (usdes cores)
    solo : a cpu sensetiv process
    eventlet : IO bound (uses threads)

    

    >> celery -A one worker -l info --concurency=2 : now worker gets 2 cores and puts them into his pool
    >> celery -A one worker -l info --pool=solo --concurency=1 : solo only does a woke in meantime  and cuncurency dosn't work even if its number is more than 1
    >> celery -A one worker -l info --pool=eventlet : eventlet type 


    create queues for cpu bound and eventlets , then connect your tasks and works to their specified queues and exchanges
"""