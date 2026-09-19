# area y volumen de un cilindro
#int 5  float 5.0  str "5"

import math 

r = float(input("Introduce el radio del cilindro "))
h = float(input("Introduce la altura del cilindo "))

area = 2 * math.pi * r * (r + h)
volumen = math.pi * r**2 * h

print(f"El área del cilindro es: {area:.2f}")
print(f"El volumen del cilindro es: {volumen:.2f}")
print("El área del cilindro es:", area)