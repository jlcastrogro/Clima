#!/usr/bin/env python3
import pika


class RabbitMQ(object):
    def __init__(self, server, user, password, queue_rabbit):
        # Varibles internas
        self.state = True
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

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state
