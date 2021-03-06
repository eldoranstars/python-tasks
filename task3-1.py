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

#https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html
#https://pythonworld.ru/moduli/modul-datetime.html
import psutil
import time 
import json
from settings import output, interval
from datetime import datetime


if output == "json":
    while True:
        to_json = {
            "DATE"          : str(datetime.now()),
            "CPU_LOAD"      : psutil.cpu_percent(interval=1, percpu=False),
            "MEMORY_USAGE"  : psutil.virtual_memory().percent,
            "SWAP"          : psutil.swap_memory().percent,
            "DISK_IO_R"     : round(psutil.disk_io_counters().read_count / 1024.0),
            "DISK_IO_W"     : round(psutil.disk_io_counters().write_count / 1024.0),
            "NET_IO_SENT"   : round(psutil.net_io_counters().bytes_sent / (1024.0 ** 3)),
            "NET_IO_RECV"   : round(psutil.net_io_counters().bytes_recv / (1024.0 ** 3))
        }
#https://www.w3schools.com/python/python_json.asp
        print(to_json)
        with open('log.json', 'a') as log:
            log.write(json.dumps(to_json) + '\n')
        time.sleep(interval)
else:
    while True:
        to_txt = '{} CPU_LOAD {}% MEMORY_USAGE {}% SWAP {}% DISK_IO {}/{} NET_IO {}/{}' .format (
        datetime.now(),
        psutil.cpu_percent(interval=1, percpu=False),
        psutil.virtual_memory().percent,
        psutil.swap_memory().percent,
        round(psutil.disk_io_counters().read_count / 1024.0),
        round(psutil.disk_io_counters().write_count / 1024.0),
        round(psutil.net_io_counters().bytes_sent / (1024.0 ** 3)),
        round(psutil.net_io_counters().bytes_recv / (1024.0 ** 3))
        )
        print(to_txt)
        with open('log.txt', 'a') as log:
            log.write(to_txt + '\n')
        time.sleep(interval)