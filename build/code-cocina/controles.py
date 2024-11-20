from entidades import Competencia, Premio


class ControlCompetencia:
    def __init__(self):
        self.premios = {
            10000: Premio(10000, "bono"),
            50000: Premio(50000, "delantal"),
            100000: Premio(100000, "cuchillo"),
            200000: Premio(200000, "olla"),
        }

    def crear_competencia(
        self,
        nombre: str,
        tipo: str,
        descripcion: str,
        valor_premio: float,
        puntos: float,
        limite_ingredientes: int,
        lista_ingredientes: list[str] | None,
    ):
        premio: Premio = self.premios[valor_premio]

        ingredientes = None
        if lista_ingredientes is not None:
            ingredientes = lista_ingredientes.split(",")

        competencia = Competencia(
            nombre,
            tipo,
            descripcion,
            premio,
            puntos,
            limite_ingredientes,
            ingredientes,
        )

        return competencia
