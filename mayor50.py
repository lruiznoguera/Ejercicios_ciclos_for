# Lea n números y diga cuántos de ellos son mayores que 50

n = int(input("Cuántos números desea evaluar "))
cont = 0

for i in range(1, n+1):
    num = int(input("Ingrese un número: "))
    if num > 50:
        cont = cont + 1
    print(i, "número leído: ", num)

print("La cantidad de números mayores que 50 es: ", cont)
