#!/c/Users/AngryBear/AppData/Local/Microsoft/WindowsApps/python
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
