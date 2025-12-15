from abc import ABC, abstractmethod
from typing import Callable, Self

"""
This is based on the latest Java designs that I was using.
@Adligo we use underscores for interfaces (i.e. I_Log2), at IBM they don't use underscores.

"""

class I_Log2(ABC):
    """
    The basic logging interface, which will usually simply print to the console,
    unless your getting fancy.  Note it has a 2 for version 2 style logging with functional suppliers
    which defer string creation, and improve performance of logging and amount of code.

    """
    TRACE = 0
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4

    @abstractmethod
    def debug(self, message_supplier: Callable[..., str]) -> Self:
        """
        Send the log to the message_consumer, which may print it to the console
        or send it somewhere else (i.e. to a JSON file for the ELK stack)
        :param message_supplier:
        :return:
        """
        pass

    @abstractmethod
    def error(self, message_supplier: Callable[..., str]) -> Self:
        """
        Send the log to the message_consumer, which may print it to the console
        or send it somewhere else (i.e. to a JSON file for the ELK stack)
        :param message_supplier:
        :return:
        """
        pass

    @abstractmethod
    def name(self) -> str:
        """

        :return: The name of the logger
        """
        pass

    @abstractmethod
    def level(self) -> int:
        """

        :return: The logging level i.e. I_Log2.INFO
        """
        pass

    @abstractmethod
    def info(self, message_supplier: Callable[..., str]) -> Self:
        """
        Send the log to the message_consumer, which may print it to the console
        or send it somewhere else (i.e. to a JSON file for the ELK stack)
        :param message_supplier:
        :return:
        """
        pass

    @abstractmethod
    def trace(self, message_supplier: Callable[..., str]) -> Self:
        """
        Send the log to the message_consumer, which may print it to the console
        or send it somewhere else (i.e. to a JSON file for the ELK stack)
        :param message_supplier:
        :return:
        """
        pass

    @abstractmethod
    def warn(self, message_supplier: Callable[..., str]) -> Self:
        """
        Send the log to the message_consumer, which may print it to the console
        or send it somewhere else (i.e. to a JSON file for the ELK stack)
        :param message_supplier:
        :return:
        """
        pass

class I_Log2Config(ABC):
    """
    The basic logging config methods,
    actual implementations could be tied to a file or simply configured from code
    """

    @abstractmethod
    def default_level(self) -> int:
        """

        :return: the default logging level (i.e. I_Log2.INFO)
        """
        pass

    @abstractmethod
    def loggers(self) -> dict[str,I_Log2]:
        """

        :return: a dictionary of the all the loggers
        """
        pass

    @abstractmethod
    def levels(self) -> dict[str, int]:
        """

        :return: a dictionary of the all the logging levels (i.e. I_Log2.INFO)
        """
        pass

class I_Log2Manager(ABC):
    """
    The separation of concerns from the logger to the
    """
    def level4(self, name: str) -> int:
        """

        :param name:
        :return: a logging level (i.e. I_Log2.INFO) for the name
        """
        pass

    def log4(self, name: str) -> I_Log2:
        """

        :param name:
        :return: a I_Log2 instance for the name.
        """
        pass