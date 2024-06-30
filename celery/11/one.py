from celery import Celery , chain , group

app = Celery('one' , broker='amqp://guest:guest@localhost:5672')

app.config_from_object('celery_conf')

@app.task
def show(name):
    print(f"hello {name}")


###########################################################priodic tasks ####################################


# first start a normal worker then in another cmd : 
# 
# >>celery -A one beat    

###########################################################3

# we start the workers with demonisiation in order to run the worker in the background (in django 3rd course)