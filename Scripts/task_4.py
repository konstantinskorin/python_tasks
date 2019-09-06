#!/usr/bin/env python3


import re #импортируем регулярные выражения

from collections import Counter #из модуля collections импортируем словарь для счета неизменяемых объектов
 
with open('access.log') as file: # открываем файл в режиме для чтения
    list = file.read() # читаем весь файл в переменную
# файл закроется сам
    
r = re.compile('^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', re.M)
data = r.findall(list)
#находим все совпадения в начале каждой строки удовлетворяющие регулярному выражению

 
for ip, count in Counter(data).most_common(10): # дальше считаем и берём десять наиболее популярных
    print(ip)
