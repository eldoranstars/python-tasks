#!/c/Users/AngryBear/AppData/Local/Microsoft/WindowsApps/python
#   Create a simple, separate python app which would monitor the your system/server.
#   Output should be written to the plain text file or json file.(needs to be specified in configuration file)
#   For monitoring purposes use psutilmodule, see: https://pythonhosted.org/psutil/
#   It should create snapshots of the state of the system each 5 minutes (interval should be configurable):
#    ● Overall CPU load
#    ● Overall memory usage
#    ● Overall virtual memory usage
#    ● IO information
#    ● Network information
#   Example of the structure for output data is about as follows:
#   SNAPSHOT 1: TIMESTAMP : <columns for system wide data>
#   SNAPSHOT 2: TIMESTAMP : <columns for system wide data>
#   SNAPSHOT 3: TIMESTAMP : <columns for system wide data>
#   Config example
#   [common]
#   output = json
#   interval = 5
#   You can use any type of configs: ini files, yaml, json or even python settings.py.

import psutil
import time 
import json
from datetime import datetime


while True:
    to_txt = 'TIMESTAMP {} CPU_LOAD {}% MEMORY_USAGE {}% SWAP {}%'  \
        .format (
        datetime.now(),
        psutil.cpu_percent(interval=1, percpu=False),
#    print(round(psutil.virtual_memory().total / (1024.0 ** 3)), 'Gb')
#    print(round(psutil.virtual_memory().used / (1024.0 ** 3)), 'Gb')
        psutil.virtual_memory().percent,
#    print(round(psutil.swap_memory().total / (1024.0 ** 3)), 'Gb')
#    print(round(psutil.swap_memory().used / (1024.0 ** 3)), 'Gb')
        psutil.swap_memory().percent
#    print('IO information:')
#    print(psutil.disk_io_counters().read_count)
#    print(psutil.disk_io_counters().write_count)
#    print('Network information:')
#    print(round(psutil.net_io_counters().bytes_sent / (1024.0 ** 3)), 'Gb')
#    print(round(psutil.net_io_counters().bytes_recv / (1024.0 ** 3)), 'Gb')
    )
    print(to_txt)
    time.sleep(10)
