class AnalizadorDeEsferas:
    def __init__(self, pesos):
      
        self.esferas = {"A": pesos[0], "B": pesos[1], "C": pesos[2], "D": pesos[3]}

    def encontrar_diferente(self):
      
        a, b, c, d = self.esferas.values()

        if a == b and b == c:
            diferente = "D"
            peso_diferente = d
        elif a == b and b == d:
            diferente = "C"
            peso_diferente = c
        elif a == c and c == d:
            diferente = "B"
            peso_diferente = b
        elif b == c and c == d:
            diferente = "A"
            peso_diferente = a
        else:
            return "Error: No se puede determinar con los datos proporcionados."

       
        peso_comun = a if a == b else b 
        comparacion = "mayor" if peso_diferente > peso_comun else "menor"

        return f"La esfera diferente es {diferente} y es {comparacion} que las otras tres."


if __name__ == "__main__":
    
    pesos = [
        float(input("Peso de la esfera A: ")),
        float(input("Peso de la esfera B: ")),
        float(input("Peso de la esfera C: ")),
        float(input("Peso de la esfera D: "))
    ]

    analizador = AnalizadorDeEsferas(pesos)
    resultado = analizador.encontrar_diferente()
    print(resultado)
