class Individuo:
    """
    Persona que asiste a un parque de atracciones
    """

    def __init__(self, documento: str, nombre: str, edad: int):
        self.documento = documento
        self.nombre = nombre
        self.edad = edad


class Grupo:
    """
    Grupo de personas de una empresa que visita un parque.
    """

    def __init__(self, empresa: str, cantidad: int):
        self.empresa = empresa
        self.cantidad = cantidad
