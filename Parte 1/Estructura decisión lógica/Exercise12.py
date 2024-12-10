class Trabajador:
    def __init__(self, nombre, horas_trabajadas, valor_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        if self.horas_trabajadas <= 40:
            salario = self.horas_trabajadas * self.valor_hora
        else:
            horas_extras = self.horas_trabajadas - 40
            if horas_extras > 8:
                horas_extras_excedentes = horas_extras - 8
                salario = (40 * self.valor_hora) + (8 * 2 * self.valor_hora) + (horas_extras_excedentes * 3 * self.valor_hora)
            else:
                salario = (40 * self.valor_hora) + (horas_extras * 2 * self.valor_hora)
        return salario

    def mostrar_resultado(self):
        salario = self.calcular_salario()
        print(f"El trabajador {self.nombre} devengó: ${salario}")

trabajador = Trabajador("ELIAS JOSE", 53, 4000)
trabajador.mostrar_resultado()

nombre = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = int(input("Ingrese el número de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))

trabajador = Trabajador(nombre, horas_trabajadas, valor_hora)
trabajador.mostrar_resultado()
