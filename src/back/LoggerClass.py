import logging
import sys
import os


class Logger:
    """
    Logger class. Logs message to file and console.

    Use the same names for loggers if you need to store information in one file (with the name of the logger)

    Use different names for loggers if you need to store information separately from each other (in different files)

    """
    def __init__(self, name: str):
        """
        Constructor.
        """
        self._log_core = logging.getLogger(name)
        self._log_core.setLevel(level=logging.DEBUG)
        self._logs_path = os.path.join(os.path.dirname(__file__)[:-5], 'Logs', f'{name}.log')
        if self._log_core.hasHandlers():
            self._log_core.handlers.clear()
        self._file_handler = logging.FileHandler(self._logs_path)
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

    def send_exception_message(self, message: str) -> None:
        """
        Sends exception message to file by logger.
        """
        self._log_core.exception(message)

    def send_info_message(self, message: str) -> None:
        """
        Sends information message to file by logger.
        """
        self._log_core.info(message)

    def send_error_message(self, message: str) -> None:
        """
        Sends critical error message to file by logger.
        """
        self._log_core.error(message)

    def send_debug_message(self, message: str) -> None:
        """
        Sends debug message to file by logger.
        """
        self._log_core.debug(message)

    def get_logger_object(self):
        """
        Returns logger object
        :return:
        """
        return self._log_core

    def get_logs_path(self):
        """
        Returns logs path
        """
        return self._logs_path

    def set_logs_path(self, path):
        """
        Sets logs path
        """
        self._logs_path = path

