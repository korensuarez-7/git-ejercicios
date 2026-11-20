# Pedir un número al usuario
# input() SIEMPRE devuelve texto (str); por eso se envuelve con int() para convertirlo.
# Error común: int(input(...)) es correcto; input(int(...)) falla porque intenta
# convertir el mensaje "Please enter a number: " a número.

numero = int(input("Ingrese un número: "))
print(f"Usted escribió el número {numero}")
print(f"El doble es {numero * 2}")
