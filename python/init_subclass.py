from abc import ABC, abstractclassmethod, abstractmethod
from typing import Dict, Iterator, Tuple, Any

class Factory(ABC):
    __REGISTER = {}

    def __init__(self):
        pass

    def __init_subclass__(cls, *, type_):
        Factory.__REGISTER[type] = cls
        super().__init_subclass__()

    @staticmethod
    def get_factory(type_) -> 'Factory':
        return Factory.__REGISTER[type_]

    @abstractmethod
    def __call__(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
        pass

class MoxieFactory(Factory, type_='moxie'):
    def __init__(self):
        super().__init__()

class FrogFactory(Factory, type_='frog'):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    factory = Factory.get_factory('moxie')
    print(factory)