import os

import ctypes
import datetime


def privilege_check():
    non_admin = ('You do not have root privileges, so you will see only'
                 'processes run under current user')
    if os.name == 'posix':
        if os.geteuid() != 0:
            print(non_admin)
    elif os.name == 'nt':
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print(non_admin)


def get_current_time():
    dt = datetime.datetime.now().replace(microsecond=0).isoformat()
    return dt.replace(':', '-')


def convert_to_iso8601(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).replace(
        microsecond=0).isoformat()
