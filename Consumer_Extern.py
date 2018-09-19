import pika
import sys
import base64
import json
import utils
import queue


class Consumer_Extern(object):
    def __init__(self, server, user, password, queue_rabbit):
        # Variables de RabbitMQ
        self.connection = None
        self.channel = None
        self.server = server
        self.user = user
        self.password = password
        self.queue_rabbit = queue_rabbit
        # Funciones para inicializar la conexión
        self.create_connection()
        self.create_channel()
        self.declare_queue()

    def create_connection(self):
        credentials = pika.credentials.PlainCredentials(
            self.user, self.password)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.server, credentials=credentials))

    def create_channel(self):
        self.channel = self.connection.channel()

    def declare_queue(self):
        self.channel.queue_declare(queue=self.queue_rabbit)

    def run(self):
        self.channel.basic_consume(self.callback,
                                    queue=self.queue_rabbit,
                                    no_ack=True)

        try:
            print(' [*] Waiting for messages. To exit press CTRL+C')
            self.channel.start_consuming()
        except KeyboardInterrupt:
            print('Conexión terminada')
            self.connection.close()

    def callback(self, ch, method, properties, body):
        msg = json.loads(body)
        print("Mensaje recibido: ", msg)
