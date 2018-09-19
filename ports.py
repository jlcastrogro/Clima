# standard libraries
import time
import getopt
import subprocess
import serial
import os
if os.name == 'nt':
    import serial.tools.list_ports_windows as serial_tools
elif os.name == 'posix':
    import serial.tools.list_ports_posix as serial_tools
else:
    raise ImportError(
        "Sorry: no implementation for your platform ('%s') available" % (os.name,))


def all_ports():
    result = []
    for port in serial_tools.comports():
        result.append(port[0])
    return result


print(all_ports())
