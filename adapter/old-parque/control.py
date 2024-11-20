from entidades import Individuo, Grupo


class ControlParque:
    """
    Controla la entrada a un parque de atracciones.
    """

    def __init__(self):
        self.__individuos = []
        self.__grupos = []

    def registrar_individuo(self, documento: str, nombre: str, edad: int) -> Individuo:
        individuo = Individuo(documento, nombre, edad)
        self.__individuos.append(individuo)
        return individuo

    def registrar_grupo(self, empresa: str, cantidad: int) -> Grupo:
        grupo = Grupo(empresa, cantidad)
        self.__grupos.append(grupo)
        return grupo

    def calcular_precio_individuo(self, individuo: Individuo) -> float:
        if individuo.edad < 12 or individuo.edad > 65:
            return 35000
        return 40000

    def calcular_precio_grupo(self, grupo: Grupo) -> float:
        precio_total = 38000 * grupo.cantidad
        if grupo.cantidad > 15:
            precio_total -= precio_total * 0.05
        return precio_total
