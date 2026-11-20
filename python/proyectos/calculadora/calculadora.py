# Calculadora en Python
print("Bienvenido a la calculadora")
print("----Opciones disponibles------")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Módulo")
print("7. Potencia")

opcion = int(input("Elija la operación que desea realizar:"))
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))


if opcion == 1:
    print("La suma es: ", num1 + num2)
elif opcion == 2:
    print("La resta es: ", num1 - num2)
elif opcion == 3:
    print("La multiplicación es: ", num1 * num2)
elif opcion == 4:
    if num2 == 0:
        print("No se puede dividir entre 0")
    else:
        print("La división es: ", num1 / num2)
elif opcion == 5:
    if num2 == 0:
        print("No se puede dividir entre 0")
    else:
        print("La división entera es: ", num1 // num2)
elif opcion == 6:
    if num2 == 0:
        print("No se puede dividir entre 0")
    else:
        print("El módulo es: ", num1 % num2)
elif opcion == 7:
    print("La potencia es: ", num1 ** num2)
else:
    print("Opción no válida")
