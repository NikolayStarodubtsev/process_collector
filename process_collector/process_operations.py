import os
import psutil
import json

from process_collector import time_operations


def get_single_process_info(process):
    username = process.username()
    c_time = process.create_time()
    exe = process.exe()
    arguments = process.cmdline()
    open_ports = []
    for connection in process.connections():
        open_ports.append(connection.laddr)

    # NOTE: repack process children in a list of dicts for future json
    # serialization.
    children = process.children()
    children_list = []
    for child in children:
        child_dict = {
                         'name': child.name(),
                         'pid': child.pid
                         }
        children_list.append(child_dict)

    # FIXME: need to investigate why psutil.Process.exe() can return None and
    # rewrite properly.
    if exe:
        exe_stat = os.stat(exe)
        exe_info = {
                    'create_time': time_operations.convert_to_iso8601(
                        exe_stat.st_ctime),
                    'last_modified': time_operations.convert_to_iso8601(
                        exe_stat.st_mtime),
                    'size': exe_stat.st_size
                   }
    else:
        exe_stat = ''
        exe_info = {}

    process_info = {
            'username': username,
            'process_create_time': time_operations.convert_to_iso8601(
                c_time),
            'exe_file': exe,
            'arguments': arguments,
            'open_ports': open_ports,
            'children': children_list,
            'exe_info': exe_info
           }
    return process_info


def get_processes_info():

    pids = psutil.pids()
    info = {}
    for pid in pids:
        try:
            process = psutil.Process(pid)
        except psutil.NoSuchProcess:
            info[pid] = {
                         'pid': pid,
                         'status': 'gone'
                        }
            continue
        process_info = get_single_process_info(process)
        info[pid] = process_info
    return info


def create_info_file():
    curr_time = time_operations.get_current_time()
    data = get_processes_info()
    with open('{}.json'.format(curr_time), "w+") as f:
        json.dump(data, f, indent=4)
