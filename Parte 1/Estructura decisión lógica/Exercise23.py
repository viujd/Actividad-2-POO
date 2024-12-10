import math

class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_soluciones(self):
        if self.a == 0:
            raise ValueError("El coeficiente 'a' no puede ser cero en una ecuación de segundo grado.")

        discriminante = self.b**2 - 4 * self.a * self.c
        if discriminante > 0:
            x1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return (x1, x2)
        elif discriminante == 0:
            x = -self.b / (2 * self.a)
            return (x,)
        else:
            return ()

a = float(input("Ingrese el coeficiente A: "))
b = float(input("Ingrese el coeficiente B: "))
c = float(input("Ingrese el coeficiente C: "))


ecuacion = EcuacionSegundoGrado(a, b, c)

try:
    soluciones = ecuacion.calcular_soluciones()
    if len(soluciones) == 2:
        print(f"Las soluciones son: x1 = {soluciones[0]}, x2 = {soluciones[1]}")
    elif len(soluciones) == 1:
        print(f"La solución única es: x = {soluciones[0]}")
    else:
        print("La ecuación no tiene soluciones reales.")
except ValueError as e:
    print(e)
