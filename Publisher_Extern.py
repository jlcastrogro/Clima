#!/usr/bin/env python3
import pika
import sys
import base64
import json
import os
import utils
import queue


class Publisher_Extern(object):
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

    def send_message(self, msg):
        msg = self.encode_message(msg)
        self.channel.basic_publish(exchange='',
                                    routing_key=self.queue_rabbit,
                                    body=msg)
        print("Mensaje enviado: ", msg)
        self.close_connection()

    def encode_message(self, msg):
        return msg

    def close_connection(self):
        self.connection.close()
