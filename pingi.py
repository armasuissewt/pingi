from ping3 import ping, verbose_ping
from datetime import datetime
from time import sleep
import sys
import argparse
from typing import Tuple, List


def start_ping_test(addr: str, interval: float):
    """
    This function keeps sending pings to a defined
    server address in a specified interval. A simple
    statistics is done.
    :param addr: Server address or ip
    :param interval: Pinging interval in seconds
    """

    print("pingi:", addr, ", interval [s]:", interval)

    ok = 0
    fail = 0
    ping_time_accum = 0.0

    while True:

        ping_res = ping(addr)

        if not ping_res:
            fail += 1
            sys.stdout.write("#")
        else:
            ok += 1
            ping_time_accum += ping_res
            sys.stdout.write(".")

        # print out intermediate results every 10th ping
        if (ok + fail) % 10 == 0:
            success_rate = ok / (ok + fail) * 100.0
            avg_ping_reply_time = ping_time_accum / max(1.0, ok)
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            print("  ", dt_string, "-> Success rate =", success_rate, " , Avg. ping reply [s] =", avg_ping_reply_time)

        sleep(interval)


def parse_pingi_args(argv) -> Tuple[str, float]:
    """
    This function parses the pingi command line input.
    :param argv: list of strings
    :return: ping address, ping interval
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--destination", dest="addr", required=False,
                        help="Ping destination address or IP", default="8.8.8.8")
    parser.add_argument("-i", "--interval", dest="interval", required=False, help="Ping interval in seconds",
                        type=float, default=5.0)
    args = parser.parse_args(argv)
    return (args.addr, args.interval)


if __name__ == "__main__":
    ping_addr, ping_interval = parse_pingi_args(sys.argv[1:])
    start_ping_test(ping_addr, ping_interval)