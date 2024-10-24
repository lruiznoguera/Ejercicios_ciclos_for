n = int(input("Ingrese la serie: "))
suma = 0

for i in range(1, n + 1, 1):
    if i % 2 == 0:
        suma = suma - (i - 1) / i
        print(f"{-i - 1} / {i}")
    else:
        suma = suma + (i - 1) / i
        print(f"{i - 1} / {i}")

print(suma)
