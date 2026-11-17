

# PARTE 3 - EJERCICIO 2
# CALCULADORA CON HERENCIA




class Operacion(object):

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular(self):
        return self.numero1 + self.numero2

    def mostrarResultado(self):
        print(f"{self.calcular():g}")



class Resta(Operacion):

    def calcular(self):
        return self.numero1 - self.numero2





def main():

    
    numero1 = float(input("Número 1: "))
    numero2 = float(input("Número 2: "))

    
    operacion1 = Operacion(numero1, numero2)
    operacion2 = Resta(numero1, numero2)

    
    print("\nOperación: Suma")
    print("Resultado de la suma:", end=" ")
    operacion1.mostrarResultado()

    
    print("\nOperación: Resta")
    print("Resultado de la resta:", end=" ")
    operacion2.mostrarResultado()


if __name__ == "__main__":
    main()
