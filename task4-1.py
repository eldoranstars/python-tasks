#!/c/Users/AngryBear/AppData/Local/Microsoft/WindowsApps/python

import psutil
import time 
import json
from settings import output, interval
from datetime import datetime

#https://www.w3schools.com/python/python_classes.asp
#Modify your application from the (Hometask3) to use classes. 

class log_class:
    def json_func(self):
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
            print(to_json)
            with open('log.json', 'a') as log:
                log.write(json.dumps(to_json) + '\n')
            time.sleep(interval)
    def txt_func(self):
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

#https://www.w3schools.com/python/python_inheritance.asp
#Create an inheritance hierarchy for any of your user defined classes.
class monitor(log_class):
    pass

if output == "json":
    print(monitor().json_func())
elif output == "txt":
    print(monitor().txt_func())
else:
    print('wrong input! try "json" or "txt"')