class Premio:
    """
    Premio que se otorga en una competencia de cocina.
    """

    def __init__(self, valor, descripcion):
        self.__valor: float = valor
        self.__descripcion: str = descripcion

    def get_valor(self) -> float:
        return self.__valor

    def get_descripcion(self) -> str:
        return self.__descripcion


class Competencia:
    """
    Competencia de cocina con diferente información para los participantes..
    """

    def __init__(
        self,
        nombre: str,
        tipo: str,
        descripcion: str,
        puntos: float,
        limite_ingredientes: int,
        ingredientes: list[str],
        premio: Premio,
    ):
        self.__nombre: str = nombre
        self.__tipo: str = tipo
        self.__descripcion: str = descripcion
        self.__premio: float = premio
        self.__puntos: int = puntos
        self.__limite_ingredientes: list[str] = limite_ingredientes
        self.__ingredientes: Premio = ingredientes

    def get_nombre(self) -> str:
        return self.__nombre

    def get_tipo(self) -> str:
        return self.__tipo

    def get_descripcion(self) -> str:
        return self.__descripcion

    def get_premio(self) -> Premio:
        return self.__premio

    def get_puntos(self) -> int:
        return self.__puntos

    def get_ingredientes(self) -> list[str]:
        return self.__ingredientes

    def get_limite_ingredientes(self) -> int:
        return self.__limite_ingredientes
