cantNotas = int(input("ingrese la cantidad de notas "))
menorNota = 5

for i in range(1, cantNotas + 1):
    nota = float(input("Ingrese nota "))
    if nota < menorNota:
        menorNota = nota

print("La menor nota es: ", menorNota)
