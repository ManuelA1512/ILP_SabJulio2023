#7. Pedir el nivel del agua en metros de una cisterna
nivel=int(input("Introduce el nivel del agua en la cisterna: "))
if (nivel<0):
    print("Fuga en la cisterna.")
elif(nivel==0):
    print("Encender Bomba de Agua.")
elif(nivel>0 and nivel<2):
    print("Acelerar Bomba de Agua.")
elif(nivel>2 and nivel<4):
    print("Bomba Trabajando!")
elif(nivel>4 and nivel<6):
    print("Desacelerar Bomba.")
elif(nivel==6):
    print("Apagar Bomba")
elif(nivel>6):
    print("Desbordamiento de Agua en Cisterna")

