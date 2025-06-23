import logging
from typing import Any


class Logger:
    def __init__(self, name: str):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

    def debug(self, msg: Any):
        self._logger.debug(msg)

    def info(self, msg: Any):
        self._logger.info(msg)

    def warning(self, msg: Any):
        self._logger.warning(msg)

    def error(self, msg: Any, exc_info: bool = False):
        self._logger.error(msg, exc_info=exc_info)

    def critical(self, msg: Any):
        self._logger.critical(msg)


log = Logger(__name__)
