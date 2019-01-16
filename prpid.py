#!/usr/bin/env python3
"""
назначение:
запуск процесса, указанного в качестве аргумента
вывод id запускаемого процесса
"""
# coding=utf8

import sys  # будем использовать sys.argv
import subprocess  # думаю, что нужен будет Popnen()

arg = sys.argv # получение аргументов из командной строки
arg.pop(0)
#print ((a for a in arg))
launch = subprocess.Popen(arg)
print(launch.pid)
#exit()