#!/c/Users/AngryBear/AppData/Local/Microsoft/WindowsApps/python
#Предположим, у нас есть access.log веб¬сервера. Нужно написать скрипт, который найдет десять IP-адресов, от которых было больше всего запросов. 
import re

your_file = 'RoutingTable.txt'
with open(your_file) as f:
    all_IP = re.findall(r'[0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}', f.read())
print(all_IP)
