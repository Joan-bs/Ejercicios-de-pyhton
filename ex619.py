# Calificacion final

parcial1 = float(input("Ingrese la calificacion del primer parcial: "))
parcial2 = float(input("Ingrese la calificacion del segundo parcial: "))
parcial3 = float(input("Ingrese la calificacion del tercer parcial: "))
final = float(input("Ingrese la calificacion del examen final: "))
trabajo = float(input("Ingrese la calificacion del trabajo final: "))

total_p = (parcial1 + parcial2 + parcial3) / 3
total = (total_p * 0.55) + (final * 0.3) + (trabajo * 0.15)
print(f"La calificacion final es: {total:.2f}")
