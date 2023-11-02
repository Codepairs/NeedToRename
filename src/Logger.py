import logging
import sys


class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level=logging.INFO)
        if self.logger.hasHandlers():
            self.logger.handlers.clear()
        self.file_handler = logging.FileHandler('info.log')
        self.console_handler = logging.StreamHandler(stream=sys.stdout)
        self.set_format()
        self.set_handlers()

    def set_handlers(self):
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)

    def set_format(self):
        for_file = '[%(asctime)s: %(levelname)s] %(message)s'
        for_console = '[%(asctime)s: %(levelname)s %(message)s]'
        file_format = logging.Formatter(fmt=for_file)
        console_format = logging.Formatter(fmt=for_console)
        self.file_handler.setFormatter(file_format)
        self.console_handler.setFormatter(console_format)

    def send_exception(self, message):
        self.logger.exception(message)

    def send_message(self, message):
        self.logger.info(message)



