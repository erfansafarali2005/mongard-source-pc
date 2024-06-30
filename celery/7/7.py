from celery import Celery
import time

app = Celery('one' , broker='amqp://guest:guest@localhost:5672')

#app.conf.result_backend = 'rpc://'


app.conf.update(
    result_backend = 'rpc://',
    task_time_limit = 20 , #a worker only works on the task for 20 seconds
    task_soft_time_limit = 15 , # if a worker worked in task_time_limit , ok but if it dosn't , it returns the exception for furtur action
    worker_concurrency = 4 , # a worker need to work on 4 tasks togheter , set it like as your cpu cores or one below
    worker_prefetch_multiplier =  1, # how many tasks need to be sent to every worker default is 4
    #                             ^-> 1 : wait for the worker to be emty
    task_ignore_result = True , # i dont need the results (logs)
    task_always_eager = True , # only use in debug mode : caues the tasks to be executed in the client not in worker !!! dont use this !!!
    task_acks_late = True , # if a task is recieved , its imideditly checked as done ! dont use this always !


)


#app.config_from_object('celery_conf')


@app.task
def add(a , b):
    time.sleep(5)
    return a / b

