# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
    ip = [i for i in (input('Введите ip адрес: ')).split('.')]
    Flag = True

    if len(ip) == 4:

        for i in ip:
            if not (i.isdigit() and int(i) in range(256)):
                Flag = False
                break
    else:
        Flag = False

    if Flag:
        break
    print('Неправильный IP-адрес')


if 1 < int(ip[0]) < 223:
    print('unicast')
elif 224 < int(ip[0]) < 239:
    print('multicast')
elif '.'.join(ip) == '0.0.0.0':
    print('unassigned')
elif '.'.join(ip) == '255.255.255.255':
    print('local broadcast')
else:
    print('unused')
