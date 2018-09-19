import json
import threading
from Publisher_Extern import Publisher_Extern as Publisher
from Consumer_Extern import Consumer_Extern as Consumer
import utils
import sys

def test():
    # threading.Thread(target=Consumer("localhost", "user",
                                    #  "xer0xer0", "out").run).start()
    # threading.Thread(target=Publisher("localhost", "user", "xer0xer0", "in").send_message(json.dumps({"cmd": "LOW", "pin": 12}))).start()
    server, user, password, args = utils.attributes(sys.argv[1:])
    pub = Publisher(server, user, password, "in")

    pub.send_message(args)


if __name__ == '__main__':
    test()