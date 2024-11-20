class Animal:
    """
     Ser vivo que habita o visita un parque natural
    """
    def __init__(self, especie, habitante, cantidad_estimada):
        self.especie = especie
        self.habitante = habitante
        self.cantidad_estimada = cantidad_estimada

    def dias_adaptacion(self):
        """
        Consultar el tiempo que se demora en adaptarse al hábitat
        :return: los días de adaptación requeridos
        """
        if self.especie == 'Felino':
            return 30
        elif self.especie == 'Mamífero':
            return 60
        else:
            return 20


class Planta:
    """
    Ser vegetal que se encuentra en un parque natural
    """
    def __init__(self, especie, beneficios, dimension):
        self.especie = especie
        self.beneficios = beneficios
        self.dimension = dimension

    def meses_adaptacion(self):
        """
        Consultar el tiempo que se demora en adaptarse al hábitat
        :return: los meses de adaptación requeridos
        """
        if self.especie == 'Conífera':
            return 20
        elif self.especie == 'Gramínea':
            return 2
        elif self.especie == 'Frutal':
            return 6
        else:
            return 12

    def calcular_cantidad(self, factor):
        """
        Consultar la cantidad estimada de esta planta en el parque
        :param factor: un factor estimado de dispersión
        """
        return self.dimension * factor
