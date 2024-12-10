class Empresa:
    def __init__(self, ventas_depto1, ventas_depto2, ventas_depto3, salario_vendedores):
        self.ventas_depto1 = ventas_depto1
        self.ventas_depto2 = ventas_depto2
        self.ventas_depto3 = ventas_depto3
        self.salario_vendedores = salario_vendedores

    def calcular_salario(self):
        total_ventas = self.ventas_depto1 + self.ventas_depto2 + self.ventas_depto3
        porcentaje_ventas = total_ventas * 0.33
        
        if self.ventas_depto1 > porcentaje_ventas:
            salario1 = self.salario_vendedores * 1.2  
        else:
            salario1 = self.salario_vendedores

        if self.ventas_depto2 > porcentaje_ventas:
            salario2 = self.salario_vendedores * 1.2  
        else:
            salario2 = self.salario_vendedores
      
        if self.ventas_depto3 > porcentaje_ventas:
            salario3 = self.salario_vendedores * 1.2  
        else:
            salario3 = self.salario_vendedores
        
        return salario1, salario2, salario3

    def mostrar_info(self):
        salario1, salario2, salario3 = self.calcular_salario()
        print(f"Salario vendedores depto. 1: {salario1:.2f}")
        print(f"Salario vendedores depto. 2: {salario2:.2f}")
        print(f"Salario vendedores depto. 3: {salario3:.2f}")


ejemplo=Empresa(4200000, 250000, 3300000, 380320)
ejemplo.mostrar_info()

ventas_depto1 = float(input("Ingrese las ventas del departamento 1: "))
ventas_depto2 = float(input("Ingrese las ventas del departamento 2: "))
ventas_depto3 = float(input("Ingrese las ventas del departamento 3: "))
salario_vendedores = float(input("Ingrese el salario de los vendedores: "))

empresa = Empresa(ventas_depto1, ventas_depto2, ventas_depto3, salario_vendedores)
empresa.mostrar_info()
