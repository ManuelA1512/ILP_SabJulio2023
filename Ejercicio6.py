#6. Pedir un número y decir si es par o impar.
num=float(input("Introduce el número: "))
resto=num%2
if (resto==0):
    print("El número es par")
else:
    print("El número es impar")
