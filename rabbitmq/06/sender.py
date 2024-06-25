import pika


# we should athenticate the client before letting them to do smt

# we can split our rabbitmq instance to diffrent vhost's to do diffrernt tasks in our vhost's | every vhost is called Node 

# every rabbitmq instance has a vhost in the name of (/)

# in the staging part we have a user named guest:guest , but in the production mode guest cannot use the admin panel , but if you put loopback_users = none guest then can access ->> !!!!! do not do that !!!!!

# >>rabitmqctl list_users -> shows the list of the users and in the [] we can see the tags and premissions

# newly created users , can't even login to the admin page 

# >>rabbitmqctl add_user 'username' 'password'

# >>rabitmqctl set_user_tags username (user_tag)-> https://www.rabbitmq.com/management.html : see the user tag table

# >>rabbitmqctl set_premissions -p 'vhost:/' 'usrrname' 'config' 'write' 'read' -> .* : means complete premission -> "*" "*" "*" : means it can does everything
credentials = pika.PlainCredentials('username' , 'password')
connection = pika.BaseConnection(pika.ConnectionParameters(host='localhost'),credentials=credentials)
ch = connection.channel()


ch.queue_declare(queue='one')
ch.basic_publish(exchange='' , routing_key='one' , body='Hello world')
print('message send...')
connection.close()