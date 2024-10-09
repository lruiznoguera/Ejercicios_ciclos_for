# Calcule el promedio de n números

n = int(input("Ingrese un número: "))
suma = 0

for i in range(1, n + 1):
    num = int(input("Ingrese un número: "))
    suma = suma + num
    print(i, "número leído: ", num)

promedio = suma / n

print("El promedio de los números leídos es: ", promedio)
