class Esfera:
    def __init__(self, peso):
        self.peso = peso

class ComparadorEsferas:
    def __init__(self, esferas):
        self.esferas = esferas

    def determinar_mas_pesada(self):
        pesos = [esfera.peso for esfera in self.esferas]
        if all(peso == pesos[0] for peso in pesos):
            return None  
        mas_pesada = max(self.esferas, key=lambda esfera: esfera.peso)
        return mas_pesada

peso_a = float(input("Ingrese el peso de la esfera A: "))
esfera_a = Esfera(peso_a)

peso_b = float(input("Ingrese el peso de la esfera B: "))
esfera_b = Esfera(peso_b)

peso_c = float(input("Ingrese el peso de la esfera C: "))
esfera_c = Esfera(peso_c)

comparador = ComparadorEsferas([esfera_a, esfera_b, esfera_c])
mas_pesada = comparador.determinar_mas_pesada()

if mas_pesada:
    print(f"La esfera de mayor peso tiene un peso de {mas_pesada.peso}.")
else:
    print("Todas las esferas tienen el mismo peso.")
