cantNotas = int(input("ingrese la cantidad de notas "))
mayorNota = 0

for i in range(1, cantNotas + 1):
    nota = float(input("Ingrese nota "))
    if nota > mayorNota:
        mayorNota = nota

print("La mayor nota es: ", mayorNota)
