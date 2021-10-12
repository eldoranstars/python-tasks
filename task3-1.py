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
from datetime import datetime, date

while True:
    print('========SNAPSHOT========')
    print("Date: "+str(date.today().year)+"-"+str(date.today().month)+"-"+str(date.today().day))
    print("Time: "+str(datetime.today().hour)+":"+str(datetime.today().minute)+":"+str(datetime.today().second))
    print('Overall CPU load:', psutil.cpu_percent(1))
    print('Overall swap memory usage:')
    print(psutil.swap_memory())
    print('IO information:')
    print(psutil.disk_io_counters())
    print('Overall virtual memory usage:')
    print(psutil.virtual_memory())
    print('Network information:')
    print(psutil.net_io_counters())
    time.sleep(10)
