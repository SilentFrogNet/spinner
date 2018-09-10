#!/usr/bin/env python3
import threading
import time
import sys

from spinner import Spinner


def print_spinner(text, spin_type, sleep=4):
    stop_spinner = threading.Event()
    spin_thread = Spinner(stop_spinner, prefix=text, spinner_string=spin_type)
    spin_thread.start()

    time.sleep(sleep)

    stop_spinner.set()
    spin_thread.join()
    stop_spinner.clear()

    print(f"{text}DONE\n")


def main(sleep):
    print("\n")
    time.sleep(2)
    print_spinner('   classic...', Spinner.SpinnerTypes.CLASSIC, sleep=sleep)
    print_spinner('   single...', Spinner.SpinnerTypes.SINGLE_PIPES, sleep=sleep)
    print_spinner('   double...', Spinner.SpinnerTypes.DOUBLE_PIPES, sleep=sleep)
    print_spinner('   vertical...', Spinner.SpinnerTypes.VERTICAL, sleep=sleep)
    print_spinner('   dot', Spinner.SpinnerTypes.DOT, sleep=sleep)
    print_spinner('   dots', Spinner.SpinnerTypes.DOTS, sleep=sleep)
    print_spinner('   dots2', Spinner.SpinnerTypes.DOTS2, sleep=sleep)


if __name__ == '__main__':
    sleep = 4
    if len(sys.argv) > 1:
        sleep = int(sys.argv[1])

    main(sleep)
