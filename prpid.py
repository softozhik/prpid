"""
назначение:
запуск процесса, указанного в качестве аргумента
вывод id запускаемого процесса
"""
# coding=utf8

import sys # будем использовать sys.argv
import subprocess # думаю, что нужен будет subprocess.Popnen
import os

'''
функция подсмотрена здесь: https://stackoverflow.com/questions/3761639/how-do-you-get-the-process-id-of-a-program-in-unix-or-linux-using-python
она работает, нужно в ней поразбираться
def osgetpid(process_name):
    return [item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:] if process_name in item.split()]
'''

# arg = sys.argv # получение аргументов из командной строки
arg = str(input()) # пока пусть будет запрос на ввод имени программы
# print (arg) # чисто для теста смотрим, что там в этом arg
subprocess.Popen(arg)
allid=os.popen('tasklist').read().splitlines()[4:]

print (allid)