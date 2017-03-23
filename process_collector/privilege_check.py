import os
import sys


def privilege_check():
    if os.name == 'posix':
        if os.geteuid() != 0:
            print('You need to have root privileges to run this script.')
            sys.exit(1)
    else:
        print('This script works properly only on Linux systems')
        sys.exit(1)
