from abc import ABC, abstractmethod


class Dto(ABC):
    '''dto base class'''
    @abstractmethod
    def deserialize(self,a):
        '''Abstract method'''
        pass

    @abstractmethod
    def serialize(self,a):
        '''Abstract method'''
        pass