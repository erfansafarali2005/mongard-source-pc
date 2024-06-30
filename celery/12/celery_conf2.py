from kombu import Queue , Exchange

default_exchange = Exchange('default' , type='direct')
media_exchange = Exchange('media' , type='direct')

task_queues = (
    #       ^-> name
    Queue('default' , default_exchange , routing_key='default'),
    Queue('video' , media_exchange , routing_key='video'),
    Queue('image' , media_exchange , routing_key='image'),
)

task_default_queue = 'default' # the main queueu of the whole project in line2
task_default_exchange = 'default'
task_default_rounting_key = 'default'


task_routes = {
    'one.add' : {'queue' : 'video'},
    'one.sub' : {'queue' : 'default'}
}