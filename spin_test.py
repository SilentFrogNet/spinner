import threading
import time

from metagoofil2.utils.utils import Spinner


def print_spinner(text, spin_type):
    stop_spinner = threading.Event()
    spin_thread = Spinner(stop_spinner, prefix=text, spinner_string=spin_type)
    spin_thread.start()

    time.sleep(4)

    stop_spinner.set()
    spin_thread.join()
    stop_spinner.clear()

    print(f"{text}DONE\n")


print_spinner('classic...', Spinner.SpinnerTypes.CLASSIC)
print_spinner('single...', Spinner.SpinnerTypes.SINGLE_PIPES)
print_spinner('double...', Spinner.SpinnerTypes.DOUBLE_PIPES)
print_spinner('vertical...', Spinner.SpinnerTypes.VERTICAL)


