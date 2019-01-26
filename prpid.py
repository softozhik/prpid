#!/usr/bin/env python3
# coding=utf8

import sys
import subprocess

args = sys.argv[1:]

if args:
    try:
        launch = subprocess.Popen(args)
        print('PID:', launch.pid)
        try:
            launch.wait()
            print('Return code:', launch.returncode)
        except KeyboardInterrupt:
            launch.kill()
            print('\nReturn code:', launch.returncode)
    except FileNotFoundError:
        print('o-ops! file not found...')
    except PermissionError:
        print('o-ops! permission denied...')
else:
    print('o-ops! no arguments...')