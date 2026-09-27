# Comisiones
import math

sueldo = float(input("Ingrese el sueldo base: "))
v1 = float(input("Ingrese el valor de la venta 1: "))
v2 = float(input("Ingrese el valor de la venta 2: "))
v3 = float(input("Ingrese el valor de la venta 3: "))
comisiones = (v1 * 0.10) + (v2 * 0.10) + (v3 * 0.10)

print (f"El sueldo base es: {sueldo}")
print (f"Las comisiones son: {comisiones:.2f}")
print (f"El total a pagar es: {sueldo + comisiones:.2f}")