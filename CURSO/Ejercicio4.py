#4. Pedir la cantidad de grados y convertirlos a °C, °F y K.
grados=int(input("Ingrese la cantidad de grados: "))
CONSTANTE=273.15
print("\nDe Kelvin a Celsius")
C1=grados-CONSTANTE
print(C1)

print("\nDe Kelvin a Fahrenheit")
F1=((9*grados-CONSTANTE*9)/5)+32
print(F1)

print("\nDe Fahrenheit a Celsius")
C2=(grados*5-32*5)/9
print(C2)

print("\nDe Fahrenheit a Kelvin")
K1=(5*grados-32*5)/9+CONSTANTE
print(K1)

print("\nDe Celsius a Kelvin")
K2=grados+CONSTANTE
print(K2)

print("\nDe Celsius a Fahrenheit")
F2=((9*grados)/5)+32
print(F2)

