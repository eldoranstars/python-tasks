#!/c/Users/AngryBear/AppData/Local/Microsoft/WindowsApps/python
import psutil

#Overall CPU load
print(psutil.cpu_percent(percpu=True))
#Network information
print(psutil.net_io_counters())
