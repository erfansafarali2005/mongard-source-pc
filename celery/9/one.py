from celery import Celery , chain , group
import time

app = Celery('one' , broker='amqp://guest:guest@localhost:5672')

@app.task
def add(a,b):
    time.sleep(2)
    return a + b

@app.task
def sub(a,b):
    time.sleep(2)
    return a -b
##############################chain###################################33
result = chain(add.signatrue(3,4) , sub.signature(2))   #first signatrue will be executed and then the result weil be sent to sub with 2 argument

result() #-> its now executed
result().get() # -> result will be printed out

print(result)

print(result().parent.get()) # -> parents means the privous chain , now it prints the reuslt of the add not the last one (sub)

#########################################group###################################

result = result = group(add.signatrue(3,4) , sub.signature(2 ,4)) #now they wil be executed togheter , so now we give the sub 2 arguemnts

result.apply_async() 

print(result.ready()) #false , because it wasn't executed
print(result.get()) #printed in the output and executed
print(result.ready()) #now it has been excuted in get now its True
print(result.completed_count())
# ^-> !!!! no () becasue its already executed in apply_async()

#######################################chord################################### -> only in database backends

######################################map##################################### -> read in docs

