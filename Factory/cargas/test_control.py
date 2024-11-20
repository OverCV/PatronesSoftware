from unittest import TestCase
from control import SeccionCarga


seccion_carga = SeccionCarga()
datos_carga1 = ["1", "10-10-2023", "2000000", "Aceros S.A."]
seccion_carga.registrar_carga("m", datos_carga1)
datos_carga2 = ["2", "10-10-2023", "5000000", "Constructoras"]
seccion_carga.registrar_carga("p", datos_carga2)
datos_carga3 = ["3", "09-09-2023", "3000000", "Constructoras"]
seccion_carga.registrar_carga("p", datos_carga3)
valor_dia = seccion_carga.valor_total_dia("10-10-2023")
assert 7000000 == valor_dia


def test_calcular_valor_sin_cargas(self):
    seccion_carga = SeccionCarga()
    valor_dia = seccion_carga.valor_total_dia("11-11-2023")
    self.assertEqual(0, valor_dia)
    # class TestSeccionCarga(TestCase):


#     def test_calcular_valor_dos_cargas(self):
