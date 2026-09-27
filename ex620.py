# Pago mensual
nombre = input("Ingrese su nombre: ")
ventas = float(input("Ingrese el total de ventas del mes: "))
comision = ventas * 15
sueldo = 350 + comision
impuesto = sueldo * 0.25
neto = sueldo - impuesto
print(f"El sueldo mensual de {nombre} es: {sueldo:.2f}")
print(f"El impuesto a pagar es: {impuesto:.2f}")
print(f"El sueldo neto a recibir es: {neto:.2f}")