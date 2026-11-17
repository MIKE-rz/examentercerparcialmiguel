

# PARTE 1 - ACTIVIDAD 1



# 1. ¿Cuál es el nombre de la clase?
# La clase se llama Producto.

# 2. ¿Cuáles son sus propiedades?
# nombre, precio y total.

# 3. ¿Cuáles son sus métodos?
# __init__(), calcularTotal() y mostrarTotal().

# 4. ¿Qué función cumple __init__?
# Inicializa el objeto y guarda sus propiedades.

# 5. ¿Para qué se utiliza self?
# Para hacer referencia al objeto actual y acceder a sus propiedades y métodos.

# 6. ¿En qué instrucción se crea un objeto?
# producto1 = Producto("Cuaderno", 35)

# 7. ¿Cuál es el nombre del objeto?
# producto1.

# 8. ¿Cómo se llama a calcularTotal()?
# producto1.calcularTotal(3)

# 9. ¿Qué valores recibe el constructor cuando se crea el objeto?
# nombre = "Cuaderno" y precio = 35.

# 10. ¿Qué resultado mostrará el programa?
# Producto: Cuaderno
# Total: $105.00



# PARTE 1 - ACTIVIDAD 2



class Rectangulo(object):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def mostrarArea(self):
        print(f"El área del rectángulo es: {self.calcularArea()}")



rectangulo1 = Rectangulo(8, 5)


rectangulo1.mostrarArea()



# PARTE 1 - ACTIVIDAD 3



# 1. ¿Cuál es la clase padre?
# Operacion.

# 2. ¿Cuál es la clase hija?
# Multiplicacion.

# 3. ¿Cómo se indica la herencia?
# Se indica colocando la clase padre entre paréntesis:
# class Multiplicacion(Operacion):

# 4. ¿Qué propiedades utiliza la clase hija?
# numero1 y numero2.

# 5. ¿Por qué puede utilizarlas sin definir su propio __init__?
# Porque hereda el constructor de la clase Operacion.

# 6. ¿Por qué los métodos calcular() tienen resultados distintos?
# Porque Multiplicacion redefine el método calcular()
# y realiza una multiplicación en lugar de una suma.

# 7. ¿Qué valores se imprimen?
# 12
# 32

# 8. ¿Qué sucedería si eliminamos calcular() de Multiplicacion?
# Utilizaría el método calcular() de la clase padre
# y realizaría una suma, dando como resultado 12.
