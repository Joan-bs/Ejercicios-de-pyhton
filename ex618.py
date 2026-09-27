# Area de un triangulo con coordenadas
import math

c1 = int(input("Ingrese la coordenada x del primer punto: "))
c2 = int(input("Ingrese la coordenada y del primer punto: "))
c3 = int(input("Ingrese la coordenada x del segundo punto: "))
c4 = int(input("Ingrese la coordenada y del segundo punto: "))
c5 = int(input("Ingrese la coordenada x del tercer punto: "))
c6 = int(input("Ingrese la coordenada y del tercer punto: "))

area = abs((c1*(c4-c6) + c3*(c6-c2) + c5*(c2-c4)) / 2)
print(f"El area del triangulo es: {area:.2f}")
