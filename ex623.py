# Sum the digits in an integer
numero = int(input("Ingrese un numero entero: "))
d1 = numero % 10
numero = numero // 10
d2 = numero % 10
numero = numero // 10
d3 = numero % 10
suma = d1 + d2 + d3
print("La suma de los digitos es: ", suma)
