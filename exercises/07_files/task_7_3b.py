# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
template = """{0:<9}{1:<20}{2}"""
mac_table = []

with open('CAM_table.txt') as cam_table:
    for line in cam_table:
        lst_line = line.split()
        if lst_line and lst_line[0].isdigit():
            vlan, mac, _, interface = lst_line
            mac_table.append([int(vlan), mac, interface])


mac_info = int(input('Enter VLAN number: '))

for i in mac_table:
    if i[0] == mac_info:
        print(template.format(i[0], i[1], i[2]))
