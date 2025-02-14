from abc import ABC, abstractmethod

from flask import Response


class Dto(ABC):
    '''dto base class'''
    @abstractmethod
    def deserialize(self,a):
        '''Abstract method'''
        pass

    @abstractmethod
    def serialize(self) -> Response:
        '''Abstract method'''
        pass

class CreateDto(Dto):
    def deserialize(self, a):
        pass

    def serialize(self) -> Response:
        pass

class GetDto(Dto):
    def deserialize(self, a):
        pass

    def serialize(self) -> Response:
        pass