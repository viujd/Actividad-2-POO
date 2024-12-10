import math
class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        return 3 * self.lado

    def calcular_altura(self):
        return (math.sqrt(3) / 2) * self.lado

    def calcular_area(self):
        altura = self.calcular_altura()
        return (self.lado * altura) / 2

    def mostrar_informacion(self):
        perimetro = self.calcular_perimetro()
        altura = self.calcular_altura()
        area = self.calcular_area()

        print(f"Lado: {self.lado}")
        print(f"Perímetro: {perimetro:.2f}")
        print(f"Altura: {altura:.2f}")
        print(f"Área: {area:.2f}")

triangulo = TrianguloEquilatero(lado=12)
triangulo.mostrar_informacion()
