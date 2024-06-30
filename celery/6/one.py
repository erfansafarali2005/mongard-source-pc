from celery import Celery
import time

app = Celery('one' , broker='amqp://guest:guest@localhost:5672' , backend='rpc://')



@app.task
def add(a , b):
    time.sleep(5)
    return a / b

"""
            see celery.result docs

 >> r = add.delay(2,3)
 >> r.ready() ->returns true or false if the task was sent or not
 >> r.get(timeout=2) -> returns the result of the task | timeout : if task was not ready in 2 seconds , skips it !!! if task raises error , it returns it too ! 
                                                                    if you wanna not to see the exception , set the propagate=False
 >> r.traceback() -> retuns the error                                                                   
 
 >> r.status -> returns the stastus of the task
 
 >> r.successfull() -> retuns true of the task was successfull
 
"""

