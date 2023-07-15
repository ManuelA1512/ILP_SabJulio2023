#5. Obtener valores para: a, b y c. Calcular la fórmula general.
a=int(input("Ingresa el valor para a: "))
b=int(input("Ingresa el valor para b: "))
c=int(input("Ingresa el valor para c: "))
raiz1=pow(b*b-(4*a*c),1/2)
x1=(-b-raiz1)/(2*a)
print("La primera solución es: ",x1)

x2=(-b+raiz1)/(2*a)
print("La segunda solución es: ",x2)


