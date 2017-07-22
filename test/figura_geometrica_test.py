
from unittest import TestCase
from tutorial.figura_geometrica import FiguraGeometrica

# O nome da classe deve iniciar com a palavra Test.
class TestFiguraGeometrica(TestCase):

    # Iniciando a variável que será usada globalmente.
    def setUp(self):
        TestCase.setUp(self)
        self.fig = FiguraGeometrica()

    # Retorna uma NotImplementedError. O nome do método deve começar com test.
    def test_get_area(self):
        self.assertRaises(NotImplementedError, self.fig.get_area)

    # Retorna uma NotImplementedError. O nome do método começa com test.
    def test_get_perimetro(self):
        self.assertRaises(NotImplementedError, self.fig.get_perimetro)
