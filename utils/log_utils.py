from time import time

def calculate_elapsed_time(start_time: float):
    et = time() - start_time

    minutes = et/60

    if minutes < 1:
        return f'{et:.03f}s'
    else:
        hour = minutes / 60
        if hour < 1:
            return f'{minutes:.03f}m'
        else:
            return f'{hour:.03f}h'