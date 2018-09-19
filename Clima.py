from Writer import Writer
from pyfirmata import Arduino, util
from Control import Control
import serial

class Clima(object):
    def __init__(self,
                 server_consumer, user_consumer, password_consumer, queue_consumer_rabbit,
                 server_publisher, user_publisher, password_publisher, queue_publisher_rabbit,
                 pin_sensor, pin_actuador_0, pin_actuador_1, port_arduino_sensor, port_arduino_actuador):
        self.state = True
        # Variables Consumer
        self.server_consumer = server_consumer
        self.user_consumer = user_consumer
        self.password_consumer = password_consumer
        self.queue_consumer_rabbit = queue_consumer_rabbit
        # Variables Publisher
        self.server_publisher = server_publisher
        self.user_publisher = user_publisher
        self.password_publisher = password_publisher
        self.queue_publisher_rabbit = queue_publisher_rabbit
        # Variables arduino
        self.board_0 = serial.Serial(port_arduino_sensor, 9600)
        self.board_1 = Arduino(port_arduino_actuador)
        self.pin_sensor = pin_sensor
        self.pin_actuador_0 = pin_actuador_0 #LED verde
        self.pin_actuador_1 = pin_actuador_1 #LED rojo
        self.it = util.Iterator(self.board_1)
        self.it.start()

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

def main():
    clima = Clima("localhost", "user", "xer0xer0", "in",
                  "localhost", "user", "xer0xer0", "out",
                  2, 8, 9, "/dev/ttyUSB0", "/dev/ttyUSB1")
    control = Control(clima)
    control.run()

if __name__ == '__main__':
    main()
