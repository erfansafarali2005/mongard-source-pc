from celery import Celery , signals
import time

app = Celery('one' , broker='amqp://guest:guest@localhost:5672')

########## signals ######### -> we sent signal to another place , if userpurchase was ok , we sent signal into models , admin panel and etc .. to do somethings

@app.task
def add(a,b):
    time.sleep(2)
    return a + b

@app.task
def sub(a,b):
    time.sleep(2)
    return a -b

# signals get run before the main task    

@signals.task_prerun.connect(sender=add) #signal is only send into add
def show(sender=None , **kwargs):
    print('task before run')
    print(sender)
    print(kwargs)

# se docs for more signals -> soooo usefull    