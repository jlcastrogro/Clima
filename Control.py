import json
import threading
import time
from Reader import Reader
from Writer import Writer
from Publisher import Publisher
from Consumer import Consumer
from queue import Queue


class Control(threading.Thread):
    def __init__(self, clima):
        self.clima = clima
        self.queue = Queue(100)
        self.reader = Reader(self, self.clima)
        self.writer = Writer(self.clima)
        self.consumer = Consumer(self, self.clima)
        self.publisher = Publisher(self.clima)

    def run(self):
        threads = [self.reader, self.writer, self.consumer, self.publisher]

        for thread in threads:
            thread.start()

        while True:
            if self.clima.state and (not self.queue.empty()):
                self.type_message(self.get_element_queue())
            time.sleep(0.01)

    def type_message(self, msg):
        msg = json.loads(msg)
        type = msg['type']
        if type == "temp":
            if msg['temp'] > 28:
                msg = json.dumps(
                    {"cmd": "HIGH", "pin": self.clima.pin_actuador_1})
            else:
                msg = json.dumps(
                    {"cmd": "LOW", "pin": self.clima.pin_actuador_0})
        elif type == "cmd":
            cmd = msg["cmd"]
            if cmd == "offreader":
                self.reader.set_state(False)
            elif cmd == "onreader":
                self.reader.set_state(True)
            elif cmd == "offwriter":
                self.writer.set_state(False)
            elif cmd == "onwriter":
                self.writer.set_state(True)
            elif cmd == "autowriter":
                self.reader.set_state(True)
                self.writer.set_auto(True)
            elif cmd == "noautowriter":
                self.reader.set_state(False)
                self.writer.set_auto(False)
            elif cmd == "offclima":
                self.clima.set_state(False)
            elif cmd == "onclima":
                self.clima.set_state(True)
            else: 
                msg = json.dumps(msg)

        print("Escribiendo en la cola del writer:", msg)
        if self.writer.get_state():
            self.writer.put_element_queue(msg)
        if self.publisher.get_state:
            self.publisher.put_element_queue(msg)

    def put_element_queue(self, element):
        self.queue.put(element)

    def get_element_queue(self):
        return self.queue.get()

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state
