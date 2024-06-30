from celery.schedules import contab

beat_schedule = {
    'call_show_every_one_minute' : { # a good name
        'task' : 'one.show',
        'schedule' : contab(minute='*/1'), #everyone minute | no value : everyone minute
        'args':('amir',)
    },
    #'another_task' : {}
}

# read the docs for more info