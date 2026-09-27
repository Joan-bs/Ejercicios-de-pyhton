# Calcular propina

subtotal = float(input("Ingrese el subtotal de la cuenta: "))
propina = float(input("Ingrese el porcentaje de propina: "))
propina_total = subtotal * (propina / 100)

print(f"La propina es de: {propina_total}")
print(f"El total a pagar es: {subtotal + propina_total}")
