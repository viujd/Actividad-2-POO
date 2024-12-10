class Estudiante:
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato_social):
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato_social = estrato_social

    def calcular_pago_matricula(self):
        pago_matricula = 50000  
        if self.patrimonio > 2000000 and self.estrato_social > 3:
            pago_matricula += self.patrimonio * 0.03
        
        return pago_matricula

    def mostrar_info(self):
        pago_matricula = self.calcular_pago_matricula()
        print(f"El estudiante con número de inscripción {self.numero_inscripcion} y nombre {self.nombres} debe pagar: ${pago_matricula:.2f}")
ejemplo=Estudiante("006T01", "Juan Pablo", 1500000, 4)
ejemplo.mostrar_info()

numero_inscripcion = input("Ingrese el número de inscripción: ")
nombres = input("Ingrese los nombres del estudiante: ")
patrimonio = float(input("Ingrese el patrimonio del estudiante: "))
estrato_social = int(input("Ingrese el estrato social del estudiante: "))

es = Estudiante(numero_inscripcion, nombres, patrimonio, estrato_social)
es.mostrar_info()
