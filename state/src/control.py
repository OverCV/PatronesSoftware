from abc import ABC, abstractmethod

from state.src.reloj import Reloj


class RelojException(Exception):
    """
    Informa de acciones no permitidas en la comunicación
    entre el reloj y el celular.
    """

    pass


class ModoReloj(ABC):
    """
    Clase base abstracta para los modos del reloj.
    """

    def __init__(self, reloj):
        self.reloj: Reloj = reloj

    @abstractmethod
    def mostrar_mensaje(self, mensaje: str, tipo_mensaje: str): ...

    @abstractmethod
    def obtener_medida(self, nombre_medida: str) -> float: ...
