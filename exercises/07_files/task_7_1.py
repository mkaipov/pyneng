# -*- coding: utf-8 -*-
import re
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

routes = []
with open('ospf.txt') as file:
    for i in file:
        re_route = re.sub('[^a-zA-Z0-9-/ .]', '', i)
        routes.append([j for j in re_route.split()])

template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

for route in routes:
    print(template.format(route[1], route[2], route[4], route[5], route[6]).rstrip('\n'))
