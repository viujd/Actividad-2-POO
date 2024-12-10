class Almacen:
    def __init__(self, valor_compra, color_bolita):
        self.valor_compra = valor_compra
        self.color_bolita = color_bolita

    def calcular_descuento(self):
        if self.color_bolita == "BLANCO":
            descuento = 0
        elif self.color_bolita == "VERDE":
            descuento = 10
        elif self.color_bolita == "AMARILLO":
            descuento = 25
        elif self.color_bolita == "AZUL":
            descuento = 50
        else: 
            descuento = 100
        
        return descuento

    def calcular_valor_a_pagar(self):
        descuento = self.calcular_descuento()
        valor_pagar = self.valor_compra - (self.valor_compra * descuento / 100)
        return valor_pagar

    def mostrar_info(self):
        valor_pagar = self.calcular_valor_a_pagar()
        print(f"El cliente debe pagar: ${valor_pagar:.2f}")


valor_compra = 543450
color_bolita = "AZUL"

almacen = Almacen(valor_compra, color_bolita)
almacen.mostrar_info()

valor_compra = float(input("Ingrese el valor de la compra: "))
color_bolita = input("Ingrese el color de la bolita (BLANCO, VERDE, AMARILLO, AZUL, ROJO): ").upper()

almacen = Almacen(valor_compra, color_bolita)
almacen.mostrar_info()
