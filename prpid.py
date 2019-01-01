"""
назначение:
запуск процесса, указанного в качестве аргумента
вывод id запускаемого процесса
"""
# coding=utf8

import sys  # будем использовать sys.argv
import subprocess  # думаю, что нужен будет subprocess.Popnen
import psutil


# arg = sys.argv # получение аргументов из командной строки
arg = str(input())  # пока пусть будет запрос на ввод имени программы
# print (arg) # чисто для теста смотрим, что там в этом arg
subprocess.Popen(arg)
for proc in psutil.process_iter():
    if proc.name() == arg:
        print (proc.pid, proc.name())
