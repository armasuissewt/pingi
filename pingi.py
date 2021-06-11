from ping3 import ping, verbose_ping
from datetime import datetime
from time import sleep
import sys
import argparse
from typing import Tuple

try:
    from pynput import keyboard
except ImportError:
    raise ImportError('pynput not supported in this environment')


# global variable -> if false pingi will stop
go_on = True


# stop pingi when 'q' pressed
def on_press(key):
    global go_on
    try:
        if key.char == 'q':
            go_on = False
            return False
    except AttributeError:
        pass


def start_ping_test(addr: str, interval: float, file_name: str):
    """
    This function keeps sending pings to a defined
    server address in a specified interval. A simple
    statistics is done.
    :param addr: Server address or ip
    :param interval: Pinging interval in seconds
    :param file_name: Result file name 
    """

    print("pingi:", addr, ", interval [s]:", interval, ", result file: ", file_name)

    ok = 0
    fail = 0
    ping_time_accum = 0.0

    f = open(file_name, "w")

    # listen to the keyboard to stop the loop
    with keyboard.Listener(on_press=on_press) as listener:

        while go_on:
            ping_res = ping(addr)
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")

            if not ping_res:
                fail += 1
                sys.stdout.write("#")
            else:
                ok += 1
                ping_time_accum += ping_res
                sys.stdout.write(".")
                f.write(dt_string + "," + str(ping_res) + "\n")
                f.flush()

            # print out intermediate results every 10th ping
            if (ok + fail) % 10 == 0:
                success_rate = ok / (ok + fail) * 100.0
                avg_ping_reply_time = ping_time_accum / max(1.0, ok)
                print("  ", dt_string, "-> Success rate =", success_rate,
                      " , Avg. ping reply [s] =", avg_ping_reply_time)

            sleep(interval)

        f.close()
        listener.join()
        print("\n", "Quite pingi")


def parse_pingi_args(argv) -> Tuple[str, float, str]:
    """
    This function parses the pingi command line input.
    :param argv: list of strings
    :return: ping address, ping interval, result file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--destination", dest="addr", required=False,
                        help="Ping destination address or IP", default="8.8.8.8")
    parser.add_argument("-i", "--interval", dest="interval", required=False,
                        help="Ping interval in seconds", type=float, default=5.0)
    parser.add_argument("-o", "--output", dest="file_name", required=False,
                        help="Result file name (csv)", default="ping.csv")
    args = parser.parse_args(argv)
    return (args.addr, args.interval, args.file_name)


if __name__ == "__main__":
    ping_addr, ping_interval, file_name = parse_pingi_args(sys.argv[1:])
    start_ping_test(ping_addr, ping_interval, file_name)
