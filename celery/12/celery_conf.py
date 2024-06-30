task_default_queue = 'mongard'


task_routes = {
    'one.add' : {'queue' : 'first'},
    'one.sub' : {'queue' : 'second'}
}