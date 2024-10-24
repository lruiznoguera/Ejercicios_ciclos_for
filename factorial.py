# Calcule el factorial de un número. (n!= 1*2*3*...*n)

n = int(input("ingrese un número "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("El factorial de ", n, "es: ", fact)
