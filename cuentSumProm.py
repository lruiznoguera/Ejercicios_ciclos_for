# Lea n números, cuente, sume y promedie todos aquellos números de son menores que 25.

n = int(input("ingrese un número "))
cont = 0
suma = 0

for i in range(1, n + 1):
    num = int(input("Ingrese un número: "))
    if num < 25:
        cont = cont + 1
        suma = suma + num
    print(i, "número leído: ", num)

prom = suma / cont

print("La cantidad de números menores que 25 es ", cont)
print("La suma de números menores que 25 es ",  suma)
print("El promedio de los números menores que 25 es: ", prom)
