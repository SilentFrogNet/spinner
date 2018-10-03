import threading
import time


class Spinner:

    def __init__(self, prefix=None, spinner_type=None, speed=0.1):
        super(Spinner, self).__init__()
        self.daemon = True
        self.prefix = prefix if prefix else ""
        self.spinner_type = spinner_type if spinner_type else SpinnerTypes.CLASSIC
        self.speed = speed  # adjust this to change the speed

    def __enter__(self):
        self.stop_event = threading.Event()
        self.spin_thread = InnerSpinner(self.stop_event, prefix=self.prefix, spinner_type=self.spinner_type, speed=self.speed)
        self.spin_thread.start()
        return self.spin_thread

    def __exit__(self, type, value, traceback):
        self.stop_event.set()
        self.spin_thread.join()
        self.stop_event.clear()


class InnerSpinner(threading.Thread):

    def __init__(self, stop_event, prefix=None, spinner_type=None, speed=0.1):
        super(InnerSpinner, self).__init__()
        self.daemon = True
        self.stop_event = stop_event
        self.prefix = prefix
        self.spinner_type = spinner_type
        self.speed = speed

    def run(self):
        while True:
            for cursor in self.spinner_type:
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
