#!/usr/bin/env python3
import json
import threading
from queue import Queue
from RabbitMQ import RabbitMQ


class Consumer(RabbitMQ, threading.Thread):
    def __init__(self, control, clima):
        self.clima = clima
        self.control = control
        # Constructor
        RabbitMQ.__init__(self,
                          self.clima.server_consumer, self.clima.user_consumer, self.clima.password_consumer,
                          self.clima.queue_consumer_rabbit)
        threading.Thread.__init__(self)

    def run(self):
        self.channel.basic_consume(self.callback,
                                   queue=self.queue_rabbit,
                                   no_ack=True)

        try:
            print(' [*] Consumer started. To exit press CTRL+C')
            self.channel.start_consuming()
        except KeyboardInterrupt:
            print('Conexión terminada')
            self.connection.close()

    def callback(self, ch, method, properties, body):
        msg = json.loads(body)
        self.control.put_element_queue(json.dumps(msg))
        print("Mensaje recibido por el consumidor: ", msg)
