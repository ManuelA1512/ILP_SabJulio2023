#2. Calcular el área y perímetro de un círculo.
#AREA
#A=Pi*radio*radio
radio=float(input("Ingrese el radio del círculo: "))
PI=3.1416
area=PI*radio*radio
print("El área del círculo es de: ", round(area,2))

#PERIMETRO
#perimetro=pi*diametro
#perimetro=pi*2r
perimetro=PI*2*radio
print("El perímetro del círculo es de: ", round(perimetro,2))
