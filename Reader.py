import json
import time
import threading
from queue import Queue


class Reader(threading.Thread):
    def __init__(self, control, clima):
        self.state = True
        self.clima = clima
        self.control = control
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if self.get_state():
                time.sleep(2)
                self.clima.board_0.flushInput()
                temp = float(self.clima.board_0.readline())
                msg = json.dumps({"type": "temp", "temp": temp})
                print("Temperatura: ", temp)
                self.control.put_element_queue(msg)
            time.sleep(0.01)

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
