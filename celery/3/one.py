from celery import Celery
import time


app = Celery('one' , broker='amqp://guest:guest@localhost:5672')

@app.task(name='one.adding')
def add(a,b):
    time.sleep(15)
    return a + b

'''

 >>add.delay(2,3) -> simple async without any option

 >> add.apply_async(args=[2,3] , expire = 5 , countdown = 2) -> expire -> how many seconds takes to be expired
                                                    and countdown means hoe many sconds takes to be sent                                                              

'''