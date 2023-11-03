import logging
import sys
import os


class Logger:
    """
    Logger class. Logs messages to file and console.
    """
    def __init__(self, name):
        """
        Constructor.
        :param name: Need to be unique.
        """
        self._log_core = logging.getLogger(name)
        self._log_core.setLevel(level=logging.DEBUG)
        if self._log_core.hasHandlers():
            self._log_core.handlers.clear()
        self._file_handler = logging.FileHandler(os.path.dirname(__file__)[:-5] + r'\TokenFiles\info.log')
        self._console_handler = logging.StreamHandler(stream=sys.stdout)
        self._set_format()
        self._add_all_handlers()

    def _add_all_handlers(self):
        """
        Apply all handlers to logger.
        :return:
        """
        self._log_core.addHandler(self._file_handler)
        self._log_core.addHandler(self._console_handler)

    def _set_format(self):
        """
        Sets logging format.
        """
        for_file = '[%(asctime)s: %(levelname)s %(message)s]'
        for_console = '[%(asctime)s: %(levelname)s %(message)s]'
        file_format = logging.Formatter(fmt=for_file)
        console_format = logging.Formatter(fmt=for_console)
        self._file_handler.setFormatter(file_format)
        self._console_handler.setFormatter(console_format)

    def send_exception_message(self, message: str) -> str:
        """
        Sends exception message to file by logger.
        """
        self._log_core.exception(message)
        return message

    def send_info_message(self, message: str) -> str:
        """
        Sends information message to file by logger.
        """
        self._log_core.info(message)
        return message

    def send_error_message(self, message: str) -> str:
        """
        Sends critical error message to file by logger.
        """
        self._log_core.error(message)
        return message

    def send_debug_message(self, message: str) -> str:
        """
        Sends debug message to file by logger.
        """
        self._log_core.debug(message)
        return message

    def get_logger_object(self):
        """
        Returns logger object
        :return:
        """
        return self._log_core
