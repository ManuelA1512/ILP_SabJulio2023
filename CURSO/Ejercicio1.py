#1. Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.
#ENTRADA DE DATOS
#PROCESOS Y SALIDAS

calif1=float(input("Ingrese la primera calificación: "))
calif2=float(input("Ingrese la segunda calificación: "))
calif3=float(input("Ingrese la tercera calificación: "))
promedio=(calif1+calif2+calif3)/3
print("El promedio de las 3 calificaciones es: ", round(promedio, 2))
if promedio>=6:
    print("El alumno está APROBADO.")
else:
    print("El alumno está REPROBADO.")
