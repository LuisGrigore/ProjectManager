from abc import ABC


class Error(ABC):
    def __init__(self, message: str = ''):
        self.message = message
