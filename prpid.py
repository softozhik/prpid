#!/usr/bin/env python3
"""
назначение:
запуск процесса, указанного в качестве аргумента
вывод id запускаемого процесса
"""
# coding=utf8

import sys  # будем использовать sys.argv
import subprocess  # думаю, что нужен будет Popnen()
import time

args = sys.argv[1:] # получение аргументов из командной строки
#arg.pop(0)
#print ((a for a in arg))

if args:
    try:
        launch = subprocess.Popen(args)
        print(launch.pid)
        try:
            launch.wait()
        except KeyboardInterrupt:
            launch.kill()
    except FileNotFoundError:
        print ('o-ops! file not found...')


else:
    print ('o-ops! no arguments...')
#exit()
