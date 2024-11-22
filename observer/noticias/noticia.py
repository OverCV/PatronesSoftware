class Noticia:
    """
    Noticia que se publica en un periódico o en redes sociales.
    """

    def __init__(self, fecha, titular, descripcion):
        # RECORD
        self.fecha = fecha
        self.titular = titular
        self.descripcion = descripcion
