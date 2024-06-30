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
    queues must be manually sent
    >> celery -A one worker -l info -Q first,second -> creates a first and second queue
    >> add.delay(2,3)
    >> sub.delay(3,4)
    
"""