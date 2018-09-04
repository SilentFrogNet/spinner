import threading
import time


class Spinner(threading.Thread):

    def __init__(self, stop_event, prefix=None, spinner_string=None, speed=0.1):
        super(Spinner, self).__init__()
        self.daemon = True
        self.stop_event = stop_event
        self.prefix = prefix if prefix else ""
        self.spinner_string = spinner_string if spinner_string else Spinner.SpinnerTypes.CLASSIC
        self.speed = speed # adjust this to change the speed

    def run(self):
        while True:
            for cursor in self.spinner_string:
                print(f"\r{self.prefix}{cursor}", end='\r')
                time.sleep(self.speed)
                if self.stop_event.is_set():
                    clean_str = " " * 50
                    print(f"\r{clean_str}", end='\r')
                    return

    class SpinnerTypes:

        CLASSIC = '|/-\\'
        SINGLE_PIPES = [u'\u2514', u'\u250c', u'\u2510', u'\u2518']
        DOUBLE_PIPES = [u'\u255a', u'\u2554', u'\u2557', u'\u255d']
        VERTICAL = ['_', u'\u2584', u'\u2588', u'\u2580', u'\xaf', u'\u2580', u'\u2588', u'\u2584']
        DOT = ['   ', '.  ', ' . ', '  .', ' . ', '.  ']
        DOTS = ['   ', '.  ', '.. ', '...', '.. ', '.  ']
        DOTS2 = ['   ', '.  ', '.. ', '...', ' ..', '  .', ' ..', '...', '.. ', '.  ']
