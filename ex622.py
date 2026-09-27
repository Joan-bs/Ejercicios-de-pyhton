# Encontrar numero de años
minutos = int(input("Ingrese el numero de minutos: "))
min_h = 60
h_d = 24
d_a = 365
min_d = min_h * h_d
min_a = min_d * d_a
años = minutos // min_a
min_restantes = minutos % min_a
días = min_restantes // min_d
print(f"{minutos} minutos son {años} años y {días} días.")