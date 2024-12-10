import math
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def calcular_semiperimetro(self):
        return self.calcular_perimetro() / 2

    def calcular_area(self):
        s = self.calcular_semiperimetro()
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def mostrar_informacion(self):
        perimetro = self.calcular_perimetro()
        semiperimetro = self.calcular_semiperimetro()
        area = self.calcular_area()

        print(f"Lados: {self.lado1}, {self.lado2}, {self.lado3}")
        print(f"Perímetro: {perimetro:.2f}")
        print(f"Semiperímetro: {semiperimetro:.2f}")
        print(f"Área: {area:.2f}")


triangulo = Triangulo(lado1=8, lado2=12, lado3=6)
triangulo.mostrar_informacion()
