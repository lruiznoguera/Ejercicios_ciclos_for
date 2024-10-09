# 3. En un centro de verificación de automóviles se desea saber el promedio de puntos contaminantes
# de los primeros 25 automóviles que lleguen. Así mismo se desea saber los puntos contaminantes
# del carro que menos contaminó y del que más contaminó.

mayor = 0
suma = 0

for i in range(1, 5 + 1):
    puntosConta = float(input("ingrese los puntos contaminantes "))
    suma = suma + puntosConta
    menor = suma

    if puntosConta < menor:
        menor = puntosConta

    if puntosConta > mayor:
        mayor = puntosConta

promedio = suma / 5

print("El promedio de puntos contaminantes de los primeros 5 automóviles es: ", promedio)
print("Los puntos contaminantes del carro que menos contaminó son: ", menor)
print("Los puntos contaminantes del carro que más contaminó son: ", mayor)
