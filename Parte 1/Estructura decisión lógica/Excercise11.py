class Comparador:
    def __init__(self, N1, N2, N3):
        self.N1 = N1
        self.N2 = N2
        self.N3 = N3

    def encontrar_mayor(self):
        if self.N1 > self.N2 and self.N1 > self.N3:
            mayor = self.N1
        elif self.N2 > self.N3:
            mayor = self.N2
        else:
            mayor = self.N3
        return mayor

    def mostrar_resultado(self):
        mayor = self.encontrar_mayor()
        print(f"El valor mayor entre: {self.N1}, {self.N2}, y {self.N3} es: {mayor}")


N1 = int(input("Ingrese el primer número: "))
N2 = int(input("Ingrese el segundo número: "))
N3 = int(input("Ingrese el tercer número: "))

comparador = Comparador(N1, N2, N3)
comparador.mostrar_resultado()
