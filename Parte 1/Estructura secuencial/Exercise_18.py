class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, retencion_fuente):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.retencion_fuente = retencion_fuente

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * (1 - self.retencion_fuente)

    def mostrar_informacion(self):
        salario_bruto = self.calcular_salario_bruto()
        salario_neto = self.calcular_salario_neto()
        print(f"Código: {self.codigo}")
        print(f"Nombres: {self.nombres}")
        print(f"Salario Bruto: ${salario_bruto:.2f}")
        print(f"Salario Neto: ${salario_neto:.2f}")


# Ejemplo de uso
empleado1 = Empleado(
    codigo="EMP001",
    nombres="Juan Pérez",
    horas_trabajadas=160,
    valor_hora=50,
    retencion_fuente=10
)

empleado1.mostrar_informacion()
