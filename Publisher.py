import json
import threading
import time
from queue import Queue
from RabbitMQ import RabbitMQ


class Publisher(RabbitMQ, threading.Thread):
    def __init__(self, clima):
        # Varibles internas
        self.clima = clima
        self.queue = Queue(100)
        # Constructor
        RabbitMQ.__init__(self,
                          self.clima.server_publisher, self.clima.user_publisher, self.clima.password_publisher,
                          self.clima.queue_publisher_rabbit)
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if self.state and (not self.empty_queue()):
                msg = json.dumps(self.get_element_queue())
                self.send_message(msg)
            time.sleep(0.01)

    def send_message(self, msg):
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_rabbit,
                                   body=msg)
        print("Mensaje para el consumer externo: ", msg)

    def put_element_queue(self, element):
        self.queue.put(element)

    def get_element_queue(self):
        return self.queue.get()

    def empty_queue(self):
        return self.queue.empty()
