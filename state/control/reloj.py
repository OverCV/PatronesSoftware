from enum import Enum

from excepciones import RelojException


class Modo(Enum):
    """
    Formas de uso de un reloj inteligente.
    """

    NORMAL = 1
    EJERCICIO = 2
    REPOSO = 3


class Reloj:
    def __init__(self, material: str):
        self.material = material
        self.modo = Modo.NORMAL
        self.color_fondo = "blanco"
        self.medidas = {}

    def mostrar_mensaje(self, mensaje: str, tipo_mensaje: str):
        """
        Muestra un mensaje enviado por el celular.
        Dependiendo del modo puede mostrar (o no) algunos tipos de mensajes.
        """
        if self.modo == Modo.REPOSO:
            if tipo_mensaje == "alarma":
                print(mensaje)
        elif self.modo == Modo.EJERCICIO:
            if tipo_mensaje == "llamada":
                print(mensaje)  
        else:
            print(mensaje)

    def cambiar_modo(self, nuevo_modo: Modo):
        self.modo = nuevo_modo

    def obtener_medida(self, nombre_medida: str) -> float:
        """
        Obtener el valor de alguna medida para mostrarlo en el celular
        """
        if self.modo == Modo.NORMAL or self.modo == Modo.EJERCICIO:
            return self.medidas.get(nombre_medida)

        raise RelojException("No se pueden obtener medidas en modo de reposo")

    def adicionar_medida(self, nombre_medida: str, valor: float):
        self.medidas[nombre_medida] = valor
