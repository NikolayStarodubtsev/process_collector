import os
import sys

import datetime


def privilege_check():
    if os.name == 'posix':
        if os.geteuid() != 0:
            print('You do not have root privileges, so you will see only'
                  'processes run under current user')
    else:
        print('This script works properly only on Linux systems')
        sys.exit(1)


def get_current_time():
    return datetime.datetime.now().replace(microsecond=0).isoformat()


def convert_to_iso8601(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).replace(
        microsecond=0).isoformat()
