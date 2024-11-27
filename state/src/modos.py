from state.src.control import ModoReloj, RelojException


class ModoNormal(ModoReloj):
    def mostrar_mensaje(self, mensaje: str, tipo_mensaje: str):
        print(mensaje)

    def obtener_medida(self, nombre_medida: str) -> float:
        return self.reloj.medidas.get(nombre_medida)


class ModoEjercicio(ModoReloj):
    def mostrar_mensaje(self, mensaje: str, tipo_mensaje: str):
        if tipo_mensaje == "llamada":
            print(mensaje)

    def obtener_medida(self, nombre_medida: str) -> float:
        return self.reloj.medidas.get(nombre_medida)


class ModoReposo(ModoReloj):
    def mostrar_mensaje(self, mensaje: str, tipo_mensaje: str):
        if tipo_mensaje == "alarma":
            print(mensaje)

    def obtener_medida(self, nombre_medida: str) -> float:
        raise RelojException("No se pueden obtener medidas en modo reposo")
