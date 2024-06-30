from celery import Celery , signals

app = Celery('one' , broker='amqp://guest:guest@localhost:5672')

app.config_from_object('celery_conf2')


@app.task(name='one.add')
def add(a,b):
    return a + b

@app.task(name='one.sub')
def sub(c,d):
    return c - d

@signals.task_postrun.connect # to show the queue details
def show_info(sender=None , **kwargs):
    print(sender.request)

"""
    >> add.delay(3,5)
    >> add.delay(4,1)

    we can also send tasks into queuses with apply_async instead of task_routes in celery_conf2 -> 

    add.apply_async(args=(4,5) , queue='image') -> !! now we dont nead that task_routes in celery_conf2



"""