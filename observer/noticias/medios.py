class SitioWeb:
    """
    Sitio en Internet donde se publican noticias.
    """

    def __init__(self, nombre):
        self.nombre = nombre

    def publicar_entrada(self, fecha, titular, descripcion):
        """
        A partir de los datos de la noticia crea una nueva entrada
        en el sitio web.
        """
        cadena_html = (
            "<p><strong>"
            + titular
            + "</strong></p>\n<br>\n"
            + "<p>"
            + fecha
            + "</p>\n<br>\n"
            + "<p>"
            + descripcion
            + "</p>"
        )
        # Simula publicar en la página web:
        print("NOTICIA EN SITIO WEB:\n")
        print(cadena_html + "\n")


class Twitter:
    """
    Cuenta en Twitter que publica el resumen de las noticias.
    """

    def __init__(self, cuenta):
        self.cuenta = cuenta

    def publicar_trino(self, descripcion):
        """
        A partir de la descripción de la noticia crea una nueva entrada
        en la red social.
        """
        trino = descripcion[0 : descripcion.find(".")]
        print("NOTICIA EN TWITTER: " + trino + "\n")
