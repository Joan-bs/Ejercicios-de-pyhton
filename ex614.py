# Inversiones


inversion1 = float(input("Ingrese el monto de la primera inversion: "))
inversion2 = float(input("Ingrese el monto de la segunda inversion: "))
inversion3 = float(input("Ingrese el monto de la tercera inversion: "))

total = inversion1 + inversion2 + inversion3

print (f"La primera inversion representa: {((inversion1/total)*100):.2f}% del total")
print (f"La segunda inversion representa: {((inversion2/total)*100):.2f}% del total")
print (f"La tercera inversion representa: {((inversion3/total)*100):.2f}% del total")