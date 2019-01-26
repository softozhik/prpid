# prpid назначение:
Запуск процесса, указанного в качестве аргумента, и вывод PID запускаемого процесса
После запуска ожидает закрытия запущенного процесса, или закрывает его принудительгл нажатием Ctrl-C
Используются стандартные библиотеки `sys` и `subprocess`

# примеры использования:
`./prpid.py ls -A`

`./prpid.py firefox ya.ru`

---
Start of the process specified as prpid's argument and print the PID of the started process
After starting it waits for the closure of the running process, or closes it by pressing Ctrl-C
Uses standard libraries `sys` and `subprocess`

# examples:
`./prpid.py ls -A`

`./prpid.py firefox ya.ru`
