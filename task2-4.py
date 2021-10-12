#!/c/Users/AngryBear/AppData/Local/Microsoft/WindowsApps/python
#Предположим, у нас есть access.log веб¬сервера. Нужно написать скрипт, который найдет десять IP-адресов, от которых было больше всего запросов. 
import re
import string
import heapq

frequency = { }
#The first thing we want to do is to store the text file in a string variable.
document_text = open('access.log', 'r')
text_string = document_text.read()
#Let's write our regular expression that would return all the IPs
match_pattern = re.findall(r'[0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}', text_string)
#At this point, we want to find the frequency of each IP in the document. 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

max_IP = heapq.nlargest(10, frequency, key=frequency.get)
for IP in max_IP:
    print(frequency[IP], IP)
