from ping3 import ping, verbose_ping
from datetime import datetime
from time import sleep
import sys


def test_connection(addr: str):

    ok = 0
    fail = 0

    while True:
        if not ping(addr):
            fail += 1
            sys.stdout.write("#")
        else:
            ok += 1
            sys.stdout.write(".")

        if (ok + fail) % 20 == 0:
            success_rate = ok / (ok + fail) * 100.0
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            print("  ", dt_string, "-> Success rate = ", success_rate)

        sleep(6)

if __name__ == "__main__":
    test_connection("www.google.ch")