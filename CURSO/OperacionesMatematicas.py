#Ejemplo 2. Operaciones matemáticas

#Importar librerias o Bibliotecas: Son archivos que contienen funciones 
import math 

#ENTRADAS DE DATOS
#Declarar o crear variables
n1= 10.4785
n2= 2.6932

#PROCESOS
suma=n1+n2
resta=n1-n2
multiplicacion=n1*n2
division= n1/n2

potencia1=n1**n2
potencia2=pow(n1,n2)

cuadrado= pow(n1, 2)
cubo=pow(n1, 3)


raiz_cuadrada1= math.sqrt(9)
raiz_cuadrada2= pow(9, 1/2)
raiz_cubica=pow(27, 1/3)
residuo= n1%n2

#SALIDA DE DATOS
print("La suma es igual a: ",round(suma,2))
print("La suma es igual a: "+str(suma)) #CONCATENACIÓN (Unir 2 o más textos en una sola cadena)
print(f"La suma es igual a: {suma}")

print("La resta es igual a: ",resta)
print("La multiplicación es igual a: ", multiplicacion)
print("La división es igual a: ", division)

print("El resultado de la potencia 1 es igual a: ",potencia1)
print("El resultado de la potencia 2 es igual a: ", potencia2)

print("El resultado del cuadrado es igual a: ", cuadrado)
print("El resultado del cubo es igual a: ", cubo)
print("El resultado de la raíz cuadrada es igual a: ", raiz_cuadrada1)
print("El resultado de la raíz cuadrada es igual a: ", raiz_cuadrada2)
print("El resultado de la raiz cúbica es igual a: ", raiz_cubica)
print(f"El módulo o residuo: {residuo}")





