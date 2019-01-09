#!/usr/bin/env python3
"""
назначение:
запуск процесса, указанного в качестве аргумента
вывод id запускаемого процесса
"""
# coding=utf8

import sys  # будем использовать sys.argv
import subprocess  # думаю, что нужен будет Popnen()

arg = sys.argv.pop() # получение аргументов из командной строки
launch = subprocess.Popen(arg, shell=True)
print(launch.pid)
#exit()