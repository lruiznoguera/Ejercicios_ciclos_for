n = int(input("Ingrese un número: "))
suma = 0

for i in range(1, n + 1, 1):
    suma += i / (i ** i)
    print(f"{i} / {i ** i}")

print(suma)
