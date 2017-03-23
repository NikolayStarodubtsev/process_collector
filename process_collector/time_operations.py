import datetime


def get_current_time():
    return datetime.datetime.now().replace(microsecond=0).isoformat()


def convert_to_iso8601(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).replace(
        microsecond=0).isoformat()
