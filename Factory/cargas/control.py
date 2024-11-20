from cargas import MateriaPrima, ProductoTerminado


class SeccionCarga:
    """
    Sección de la empresa que controla la recepción o despacho de cargas del día.
    """

    def __init__(self):
        self.cargas = []

    def registrar_carga(self, tipo_carga, datos_carga):
        cargas = {
            "m": MateriaPrima(*datos_carga),
            "p": ProductoTerminado(*datos_carga),
        }
        carga = cargas[tipo_carga]

        self.cargas.append(carga)

    def valor_total_dia(self, fecha):
        valor_dia = 0
        for carga in self.cargas:
            if carga.fecha_envio == fecha:
                valor_dia += carga.valor

        return valor_dia
