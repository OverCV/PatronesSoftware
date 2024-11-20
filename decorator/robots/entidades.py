class Robot:
    """
    Robot que puede extenderse con diferentes funcionalidades.

    Sus operaciones "funcionar" y "descripcionFunciones" necesitan
    condicionales para saber qué funcionalides tiene y así poder
    ejectuar las acciones (que se simulan con print)
    o retornar la información necesaria.
    """

    def __init__(
        self,
        id,
        levanta_objetos,
        detecta_barreras,
    ):
        self.__id = id
        self.__levanta_objetos = levanta_objetos
        self.__detecta_barreras = detecta_barreras

    def funcionar(self):
        print("Avanzando... ")

        if self.__levanta_objetos:
            print("Levantando objetos... ")

        if self.__detecta_barreras:
            print("Detectando barreras...")

    def descripcion_funciones(self):
        funciones = "El robot avanza "

        if self.__levanta_objetos:
            funciones += " levanta objetos "

        if self.__detecta_barreras:
            funciones += " detecta barreras "

        return funciones
