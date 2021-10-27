from abc import ABC, abstractmethod


class BaseAugmentation(ABC):
    """Базовый класс аугментаций"""
    def __init__(self, probability:float):
        self.probability = probability

    @abstractmethod
    def __call__(self, text:str)->str:
        pass
