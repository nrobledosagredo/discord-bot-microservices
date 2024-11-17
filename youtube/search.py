import os, time
import pika
from youtubesearchpython import VideosSearch

print('start youtube...')

time.sleep(10)

########### CONNEXIÓN A RABBIT MQ #######################

HOST = os.environ['RABBITMQ_HOST']
print("rabbit:"+HOST)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'cartero'
channel.exchange_declare(exchange='cartero', exchange_type='topic', durable=True)

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue="youtube", exclusive=True, durable=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='cartero', queue=queue_name, routing_key="youtube")

##########################################################


########## ESPERA Y HACE ALGO CUANDO RECIBE UN MENSAJE ####

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
	print(body.decode("UTF-8"))
	arguments = body.decode("UTF-8").split(" ")

	if (arguments[0]=="!search"):

		word = arguments[1]

		videosSearch = VideosSearch(word, limit=2)

		result = (videosSearch.result()['result'][0]['link'])

		########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
		print("send a new message to rabbitmq: "+result)
		channel.basic_publish(exchange='cartero',routing_key="discord_writer",body=result)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

#######################