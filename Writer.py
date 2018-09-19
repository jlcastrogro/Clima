import time
import json
import threading
from queue import Queue


class Writer(threading.Thread):
    def __init__(self, clima):
        self.auto = True
        self.state = True
        self.clima = clima
        self.queue = Queue(100)
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if self.state and (not self.empty_queue()):
                msg = json.loads(self.get_element_queue())
                cmd, pin = msg['cmd'], msg['pin']
                if cmd == "HIGH":
                    pin_off = self.clima.pin_actuador_0
                    self.clima.board_1.digital[pin].write(1)
                    self.clima.board_1.digital[pin_off].write(0)
                elif cmd == "LOW":
                    pin_off = self.clima.pin_actuador_1
                    self.clima.board_1.digital[pin].write(1)
                    self.clima.board_1.digital[pin_off].write(0)
                print(
                    "Escribiendo en el arduino: ", msg)
            if self.auto is False:

                pass
            time.sleep(0.01)

    def put_element_queue(self, element):
        self.queue.put(element)

    def get_element_queue(self):
        return self.queue.get()

    def get_state(self):
        return self.state

    def set_state(self, state):
        if state == False:
            pin_off = self.clima.pin_actuador_0
            self.clima.board_1.digital[pin_off].write(0)
            pin_off = self.clima.pin_actuador_1
            self.clima.board_1.digital[pin_off].write(0)
        self.state = state

    def empty_queue(self):
        return self.queue.empty()
    
    def set_auto(self, state):
        if state == False:
            self.queue = Queue(100)
        self.auto = state
