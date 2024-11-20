import unittest
from robots.entidades import Robot

class TestRobot(unittest.TestCase):
    def test_robot_solo_avanza(self):
        robot = Robot("1", False, False)
        descripcion = robot.descripcion_funciones()
        self.assertEqual("El robot avanza ", descripcion)
    
    def test_robot_avanza_levanta(self):
        robot = Robot("2", True, False)
        descripcion = robot.descripcion_funciones()
        self.assertEqual("El robot avanza  levanta objetos ", descripcion)
    
    def test_robot_avanza_detecta(self):
        robot = Robot("1", False, True)
        descripcion = robot.descripcion_funciones()
        self.assertEqual("El robot avanza  detecta barreras ", descripcion)
    
    def test_robot_avanza_levanta_detecta(self):
        robot = Robot("1", True, True)
        descripcion = robot.descripcion_funciones()
        self.assertEqual("El robot avanza  levanta objetos  detecta barreras ", descripcion)    
    