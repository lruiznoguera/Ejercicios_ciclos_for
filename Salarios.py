# Escriba un algoritmo y programa en python que calcule, a partir de los "n" salarios de los empleados de una compañía
# 1. Salario más alto
# 2. Salario más bajo
# 3. Promedio de los salarios ingresados

n = int(input("Ingrese la cantidad de empleados "))
suma = 0
mayor = 0
cont = 0

for i in range(1, n + 1, 1):
    cont += 1
    salario = float(input(f"Ingrese el salario {cont}: "))
    menor = suma
    suma += salario
    print(menor)

    if salario < menor:
        menor = salario
        print(menor)

    if salario > mayor:
        mayor = salario

promedio = suma / n

print("El salario más bajo es: ", menor)
print("El salario más alto es: ", mayor)
print("El promedio de los salarios es: ", promedio)
