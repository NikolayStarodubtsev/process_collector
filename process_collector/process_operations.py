import os
import psutil
import json

from process_collector import utils


def get_single_process_info(process):
    # NOTE: Do not get connections from as_dict, because we need to repack it.
    process_info = process.as_dict(['username',
                                    'create_time',
                                    'exe',
                                    'pid',
                                    'cmdline',
                                    'name'])

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
    if process_info['exe']:
        exe_stat = os.stat(process_info['exe'])
        exe_info = {
                    'create_time': utils.convert_to_iso8601(
                        exe_stat.st_ctime),
                    'last_modified': utils.convert_to_iso8601(
                        exe_stat.st_mtime),
                    'size': exe_stat.st_size
                   }
    else:
        exe_info = {}

    process_info['exe_info'] = exe_info
    process_info['open_ports'] = open_ports
    process_info['create_time'] = utils.convert_to_iso8601(
        process_info['create_time'])

    return process_info


def get_processes_info():
    info = []
    for process in psutil.process_iter():
        try:
            process_info = get_single_process_info(process)
            info.append(process_info)
        except psutil.AccessDenied:
            pass
    return info


def create_info_file():
    curr_time = utils.get_current_time()
    data = get_processes_info()
    with open('{}.json'.format(curr_time), "w+") as f:
        json.dump(data, f, indent=4)
