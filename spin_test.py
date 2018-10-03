#!/usr/bin/env python3
import time
import sys

from spinner import Spinner, SpinnerTypes


def print_spinner(text, spin_type, sleep=4):
    with Spinner(prefix=text, spinner_type=spin_type):
        time.sleep(sleep)

    dots = "..."
    if text.endswith('...'):
        dots = ""
    print(f"{text}{dots}DONE\n")


def main(sleeptime):
    time.sleep(2)
    print_spinner('   classic...', SpinnerTypes.CLASSIC, sleep=sleeptime)
    print_spinner('   single...', SpinnerTypes.SINGLE_PIPES, sleep=sleeptime)
    print_spinner('   double...', SpinnerTypes.DOUBLE_PIPES, sleep=sleeptime)
    print_spinner('   vertical...', SpinnerTypes.VERTICAL, sleep=sleeptime)
    print_spinner('   dot', SpinnerTypes.DOT, sleep=sleeptime)
    print_spinner('   dots', SpinnerTypes.DOTS, sleep=sleeptime)
    print_spinner('   dots2', SpinnerTypes.DOTS2, sleep=sleeptime)


if __name__ == '__main__':
    sleep_time = 4
    if len(sys.argv) > 1:
        sleep_time = int(sys.argv[1])

    main(sleep_time)
