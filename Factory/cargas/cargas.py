from abc import ABC


class Carga(ABC):
    """
    Carga que se recibe o se despacha de una empresa
    """

    def __init__(self, identificador, fecha_envio, valor):
        self.identificador = identificador
        self.fecha_envio = fecha_envio
        self.valor = float(valor)


class MateriaPrima(Carga):
    """
    Un tipo de carga formado por productos sin procesar,
    que serán usados por la empresa en la fabricación de otros productos
    """

    def __init__(self, identificador, fecha_envio, valor, proveedor):
        super().__init__(identificador, fecha_envio, valor)
        self.proveedor = proveedor


class ProductoTerminado(Carga):
    """
    Tipo de carga formada por los productos finales elaborados por la empresa.
    """

    def __init__(self, identificador, fecha_envio, valor, destino):
        super().__init__(identificador, fecha_envio, valor)
        self.destino = destino
