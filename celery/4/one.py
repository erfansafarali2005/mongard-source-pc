from celery import Celery
from celery.utils.log import get_task_logger


app = Celery('one' , broker='amqp://guest:guest@localhost:5672')
logger = get_task_logger(__name__)


@app.task(name='one.adding' , bind=True , default_retry_countdown = 20) #this retry countdown will be applied for all tasks and can be overwriten like code below
def add(self,a,b):
    try :
        return a / b
    except ZeroDivisionError:
        logger.info('sorry')
        self.retry(countdown = 4 , max_retries = 10) #wait for 4 secnds (oversirtes the main default one)
#                                               ^-> only retries it for 10 times

'''
[2024-06-28 10:04:48,206: WARNING/ForkPoolWorker-2] <Context: {'lang': 'py', 'task': 'one.adding', 'id': 'ca178bbe-8cd5-4bc4-8681-10484dc46853', 
'shadow': None, 'eta': None, 'expires': None, 'group': None, 'group_index': None, 'retries': 0, 'timelimit': [None, None], 'root_id': 'ca178bbe-8cd5-4bc4-8681-10484dc46853', 
'parent_id': None, 'argsrepr': '(2, 3)', 'kwargsrepr': '{}', 'origin': 'gen22270@cuthbert-pc', 'ignore_result': False, 'properties': {'content_type': 'application/json', 'content_encoding': 'utf-8', 
'application_headers': {'lang': 'py', 'task': 'one.adding', 'id': 'ca178bbe-8cd5-4bc4-8681-10484dc46853', 'shadow': None, 'eta': None, 'expires': None, 'group': None, 'group_index': None, 'retries': 0, 
'timelimit': [None, None], 'root_id': 'ca178bbe-8cd5-4bc4-8681-10484dc46853', 'parent_id': None, 'argsrepr': '(2, 3)', 'kwargsrepr': '{}', 'origin': 'gen22270@cuthbert-pc', 'ignore_result': False}, 'delivery_mode': 2, 
'priority': 0, 'correlation_id': 'ca178bbe-8cd5-4bc4-8681-10484dc46853', 'reply_to': '13778d6d-b8b8-35d0-876a-fb3bfb1d2ec4'}, 'reply_to': '13778d6d-b8b8-35d0-876a-fb3bfb1d2ec4', 'correlation_id': 'ca178bbe-8cd5-4bc4-8681-10484dc46853', 
'hostname': 'celery@cuthbert-pc', 'delivery_info': {'exchange': '', 'routing_key': 'celery', 'priority': 0, 'redelivered': False}, 'args': [2, 3], 'kwargs': {}, 'is_eager': False, 'callbacks': None, 'errbacks': None, 'chain': None, 'chord': None,
 'called_directly': False, '_protected': 1}>


'''