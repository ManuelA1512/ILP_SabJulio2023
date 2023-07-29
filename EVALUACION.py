print("EJERCICIO DE EVALUACIÓN")
print("Seleccione la opción correcta")
aciertos=0
print("1. Herramienta de programación, parecido al lenguaje español utilizado para crear código.")
print("a) IDE  b) Pseudocódigo  c) Compilador  d) ANSI/ISO")
respuesta=input("Ingresa la opción de tu respuesta: ")
if respuesta=="b":
    aciertos+=1

print("\n2. Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados.")
print("a) Información  b) Datos  c) Programa  d) Código")
respuesta=input("Ingresa la opción de tu respuesta: ")
if respuesta=="a":
    aciertos+=1

print("\n3. Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo.")
print("a) IEEE b) IDE  c) ANSI/ISO  d) VSCode")
respuesta=input("Ingresa la opción de tu respuesta: ")
if respuesta=="c":
    aciertos+=1

print("\n4. Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema.")
print("a) Proceso  b) Solución  c) Función  d) Algoritmo")
respuesta=input("Ingresa la opción de tu respuesta: ")
if respuesta=="d":
    aciertos+=1

print("\n5. Conjunto de elementos que se relacionan para cumplir una función determinada")
print("a) Estructura  b) Datos  c) Operación  d) Sistema")
respuesta=input("Ingresa la opción de tu respuesta: ")
if respuesta=="d":
    aciertos+=1

print("\n6. Componente de un IDE que se encarga de traducir el código fuente a código máquina.")
print("a) Depurador  b) Editor de Texto  c) Terminal de Salida  d) Compilador/Intérprete")
respuesta=input("Ingresa la opción de tu respuesta: ")
if respuesta=="d":
    aciertos+=1

print("\n7. Elemento que se usa para almacenar una cantidad donde cambia su valor.")
print("a) Constante  b) Variable  c) Libreria  d) Tipo de Dato")
respuesta=input("Ingresa la opción de tu respuesta: ")
if respuesta=="b":
    aciertos+=1

print("\n8. Conjunto de símbolos, letras, números que no tienen un significado.")
print("a) Datos  b) Estructura  c) Información  d) Sistema")
respuesta=input("Ingresa la opción de tu respuesta: ")
if respuesta=="a":
    aciertos+=1

print("\n9. Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento.")
print("a) Filosofía  b) Sociología  c) Lógica  d) Argumentación")
respuesta=input("Ingresa la opción de tu respuesta: ")
if respuesta=="c":
    aciertos+=1

print("\n10. Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto.")
print("a) Evento  b) Estándar  c) Calidad  d) Productividad")
respuesta=input("Ingresa la opción de tu respuesta: ")
if respuesta=="b":
    aciertos+=1

print("\n11. Conjunto de elementos ordenados que componen y son la base de algo físico o no físico.")
print("a) Estructura  b) Sistema  c) Objeto  d) Virtual")
respuesta=input("Ingresa la opción de tu respuesta: ")
if respuesta=="a":
    aciertos+=1

print("\n12. Conjunto de instrucciones (código) que indican a la computadora tareas a realizar.")
print("a) Operaciones/Cálculos  b) Sintaxis  c) Programa de Computadora  d) Comando")
respuesta=input("Ingresa la opción de tu respuesta: ")
if respuesta=="c":
    aciertos+=1

calificacion=(aciertos*10)/12
print("\nLos aciertos que obtuviste fueron: ", aciertos, "/12 dando un total de: ", calificacion)