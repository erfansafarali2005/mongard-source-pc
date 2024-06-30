from celery import Celery
from celery.utils.log import get_task_logger

app = Celery('one' , broker='amqp://guest:guest@localhost:5672')
logger = get_task_logger(__name__)


@app.task(name='one.adding' , bind=True , default_retry_countdown = 20)
def add(self,a,b):
    try :
        return a / b
    except ZeroDivisionError:
        logger.info('sorry')
        self.retry(countdown = 10 , max_retries = 10)

# >> celery --broker=amqp://guest:guest@localhost:5672// flower -> to enable the flower on that worker !!! its like a worker and need to be ran

# >> celery status | celery purge | celery inspect active/revoked/stats ...