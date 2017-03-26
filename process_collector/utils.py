import os
import sys

import datetime


def privilege_check():
    if os.name == 'posix':
        if os.geteuid() != 0:
            print('You need to have root privileges to run this script.')
            sys.exit(1)
    else:
        print('This script works properly only on Linux systems')
        sys.exit(1)


def get_current_time():
    return datetime.datetime.now().replace(microsecond=0).isoformat()


def convert_to_iso8601(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).replace(
        microsecond=0).isoformat()
