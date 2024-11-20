import unittest
from controles import ControlCompetencia


class TestControlCompetencia(unittest.TestCase):
    def test_competencia_con_ingredientes(self):
        control = ControlCompetencia()
        competencia = control.crear_competencia(
            # nombre="Rayo Veloz", "Velocidad", None, 50000, 5, 0, "Papa,Sandia"
            nombre="Rayo Veloz",
            tipo="Velocidad",
            descripcion=None,
            valor_premio=50000,
            puntos=5,
            limite_ingredientes=0,
            ingredientes=["Papa", "Sandia"],
        )

        self.assertEqual("Rayo Veloz", competencia.get_nombre())
        self.assertEqual("Velocidad", competencia.get_tipo())
        self.assertIsNone(competencia.get_descripcion())
        self.assertEqual("delantal", competencia.get_premio())
        self.assertEqual(5, competencia.get_puntos())
        self.assertEqual(["Papa", "Sandia"], competencia.get_ingredientes())

    def test_competencia_sin_ingredientes(self):
        control = ControlCompetencia()
        competencia = control.crear_competencia(
            "Ingenio", None, None, 100000, 6, 0, None
        )

        self.assertEqual("Ingenio", competencia.get_nombre())
        self.assertIsNone(competencia.get_tipo())
        self.assertIsNone(competencia.get_descripcion())
        self.assertEqual("cuchillo", competencia.get_premio().get_descripcion())
        self.assertEqual(6, competencia.get_puntos())
        self.assertIsNone(competencia.get_ingredientes())
