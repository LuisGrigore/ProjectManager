from abc import ABC


class Dto(ABC):
    def deserialize(self,a):
        pass
    def serialize(self,a):
        pass