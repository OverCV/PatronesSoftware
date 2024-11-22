from medios import SitioWeb, Twitter
from periodico import Periodico


def prueba_noticias():
    """
    Pruebas de un periódico que publica noticias.
    """
    periodico = Periodico("El comunicativo")
    sitio_web = SitioWeb("www.comunicativo.com")
    cuenta_twitter = Twitter("@comunicativo")

    periodico.__website = sitio_web
    periodico.__twitter = cuenta_twitter

    periodico.registrar_noticia(
        "14-oct-2023",
        "Eclipse anular",
        "En Colombia se podrá observar el Eclipse anular de sol. "
        "Se recomienda usar lentes especiales.",
    )


if __name__ == "__main__":
    prueba_noticias()
