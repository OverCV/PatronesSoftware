from noticia import Noticia


class Periodico:
    """
    Medio informativo que publica noticias en medios escritos.
    """

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__website = None
        self.__twitter = None
        self.__noticias = []

    def registrar_noticia(self, fecha, titular, descripcion):
        """
        Publica una nueva noticia en diferentes medios
        (incluyendo medios de Internet).
        """
        noticia = Noticia(fecha, titular, descripcion)
        self.__noticias.append(noticia)

        # Publica en web y redes sociales
        self.publicar_web(noticia)
        self.publicar_twitter()

    def publicar_web(self, noticia: Noticia):
        self.__website.publicar_entrada(
            noticia.fecha, noticia.titular, noticia.descripcion
        )

    def publicar_twitter(self, noticia: Noticia):
        self.__twitter.publicar_trino(noticia.descripcion)
