from tutorial.figura_geometrica import FiguraGeometrica

class Quadrado(FiguraGeometrica):

    def __init__(self):
        self.lado = 0

    def get_area(self):
        return self.lado ** 2

    def get_perimetro(self):
        return 4 * self.lado
