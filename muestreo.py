# 1. Se debe realizar un muestreo con 50 personas para determinar el promedio de peso de los niños,
# jóvenes, adultos y viejos que existen en su zona habitacional. Se determinan las categorías así:
# Categoría: Niños, Jóvenes, Adultos, Viejos.
# Edad: 0-12, 14-29, 30-59, 60 en adelante.

muestreo = 5
edad = int(input("ingrese la edad "))
cat_1 = 0
sumaPeso = 0

for i in range(1, muestreo + 1):
    if edad >= 0 and edad <= 13:
        peso = float(input("Ingrese el peso: "))
        cat_1 += 1
        sumaPeso += peso

prom = sumaPeso / cat_1
print("El peso es: ", prom)
