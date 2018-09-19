import json
import threading
from Publisher_Extern import Publisher_Extern as Publisher
from Consumer_Extern import Consumer_Extern as Consumer


def test():
    threading.Thread(target=Consumer("localhost", "user",
                                     "xer0xer0", "out").run).start()
    # threading.Thread(target=Publisher("localhost", "user", "xer0xer0", "in").send_message(json.dumps({"cmd": "LOW", "pin": 12}))).start()


if __name__ == '__main__':
    test()