import abc
from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def crear_legajo(self):
        pass