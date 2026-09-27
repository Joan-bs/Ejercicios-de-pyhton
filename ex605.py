# Coste del viaje

distancia = float(input("Ingrese la distancia del viaje en kilómetros: "))
km_galon = float(input("Ingrese el km por galon: "))
galon = float(input("Ingrese el precio del galon: "))

coste_total = (distancia / km_galon) * galon

print(f"El coste total del viaje es: {coste_total}")