import time


# -- Get time in seconds with lot of decimals --
get_time = time.time()


def start_timer():
    # -- Calculate time in seconds with 2 decimals
    run_timer = round((time.time() - get_time), 2)
    return run_timer


def stop_timer():
    return (str(start_timer()))
