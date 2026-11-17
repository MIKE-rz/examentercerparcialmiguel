

# PARTE 2 - EJERCICIO 1
# COBRO DE ESTACIONAMIENTO

class Estacionamiento(object):

    def __init__(self, horas):
        self.horas = horas

    def calcularPago(self):

        if self.horas >= 1 and self.horas <= 2:
            total = self.horas * 15

        elif self.horas >= 3 and self.horas <= 5:
            total = self.horas * 12

        else:
            total = self.horas * 10

        return total

    def mostrarRecibo(self):

        print("RECIBO DE ESTACIONAMIENTO")
        print(f"Horas: {self.horas}")
        print(f"Total a pagar: ${self.calcularPago():.2f}")






def main():

    while True:
        try:
            horas = int(input("Horas estacionadas: "))

            if horas > 0:
                break
            else:
                print("Error: ingresa un número mayor que cero.")

        except ValueError:
            print("Error: debes ingresar un número entero.")

    estacionamiento1 = Estacionamiento(horas)

    estacionamiento1.mostrarRecibo()


if __name__ == "__main__":
    main()
