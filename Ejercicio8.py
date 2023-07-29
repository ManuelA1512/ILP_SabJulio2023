"""
8. Obtener un número y determinar lo siguiente:
a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE
b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
c) en otro caso imprimir No Válido
"""
numero=int(input("Ingrese el número: "))
j=0


if (numero<0 and numero>-100):
    for i in range(-1, -100, -2):
        print(i)

elif (numero>0 and numero<100):
    while(j<100):
        print(j)
        j+=2
else:
    print("No válido")




