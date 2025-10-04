# repo_base.py
from abc import ABC, abstractmethod

class RepoBase(ABC):
    @abstractmethod
    def guardar(self, libros, prestamos):
        """Guarda el estado (libros y préstamos)"""
        pass

    @abstractmethod
    def cargar(self):
        """Carga el estado previamente guardado. """
        pass
