from celery import Celery
import time

app = Celery('one' , broker='amqp://guest:guest@localhost:5672')


@app.task
def add(a , b):
    time.sleep(3)
    return a / b

#          ^-> its like a sleeped task 
result = add.signature((2,) , countdown=1) # a signal to be sent to another place | arguments should be in a tuple

result.delay(3) # no arguemnts needed becaseu of result variable

# !!! this signature is a partial , its incompleted so we will complete it later !!! like when user is going to the payment page and we are wating for the final status

print(result)
print(result.options)
print(result.args)

# call back : 
@app.task
def sub(a,b):

    return a - b

add.apply_async((2,2) , link=sub.signature((3,))) #the result of add will be sent to the link with the second arguments 3

# immutablity :

add.apply_async((2,2) , link=sub.signature((3,) , immutable=True)) #the result is not needed , we want to create a chain of tasks to be executed togheter 