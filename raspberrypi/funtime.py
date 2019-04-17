# ------- Time ------- #
# function to time converter


def time_converter(time):
    from datetime import datetime
    converted_time = datetime.fromtimestamp(
        int(time)).strftime('%H:%M:%S')
    return converted_time


def current_time():
    from datetime import datetime
    exactly = datetime.today().strftime('%H:%M')
    return exactly

