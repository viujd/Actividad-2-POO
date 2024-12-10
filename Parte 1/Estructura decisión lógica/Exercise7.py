class comparador:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def comparar(self):
        if self.A > self.B:
            return "A es mayor que B"
        elif self.A == self.B:
            return "A es igual a B"
        else:
            return "A es menor que B"

    def mostrar_resultado(self):
        resultado = self.comparar()
        print(resultado)

print("Ejmeplo de libro con A=20 y B=25")
ejemplolibro=comparador(20,25)
ejemplolibro.mostrar_resultado()

A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))

comparador = comparador(A, B)
comparador.mostrar_resultado()
