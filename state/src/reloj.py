from state.src.modos import ModoEjercicio, ModoNormal, ModoReposo


class Reloj:
    def __init__(self, material: str):
        self.material = material
        self.estado_actual = ModoNormal(self)  # Estado inicial
        self.color_fondo = "blanco"
        self.medidas = {}

    def mostrar_mensaje(self, mensaje: str, tipo_mensaje: str):
        self.estado_actual.mostrar_mensaje(mensaje, tipo_mensaje)

    def cambiar_modo(self, nuevo_modo: str):
        if nuevo_modo == "normal":
            self.estado_actual = ModoNormal(self)
        elif nuevo_modo == "ejercicio":
            self.estado_actual = ModoEjercicio(self)
        elif nuevo_modo == "reposo":
            self.estado_actual = ModoReposo(self)

    def obtener_medida(self, nombre_medida: str) -> float:
        return self.estado_actual.obtener_medida(nombre_medida)

    def adicionar_medida(self, nombre_medida: str, valor: float):
        self.medidas[nombre_medida] = valor
