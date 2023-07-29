#9. Calcular la nómina para un empleado en el mes de Mayo del 2023 conociendo
#su pago por día de $250.-
mes= input("Ingresa el mes de nómina: ")
dias=int(input("Ingresa los días laborados: "))
pago=float(input("Ingresa el pago por día: "))

pagobruto=dias*pago
iva_trasladado=pago*0.16
subtotal=pagobruto+iva_trasladado
iva_retenido=(iva_trasladado/3)*2
isr_retenido=pagobruto*0.10
pago_neto=subtotal-iva_retenido-isr_retenido

print(f"Pago Bruto es: {pagobruto}")
print(f"IVA Trasladado es: {iva_trasladado}")
print(f"Subtotal es: {subtotal}")
print(f"IVA Retenido es: {iva_retenido}")
print(f"ISR Retenido es: {isr_retenido}")
print(f"Pago neto: {pago_neto}")

