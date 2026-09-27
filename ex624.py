# Tabla de multiplicar de un numero n
num = int(input("Ingrese un numero entre 1 y 10: "))
if num >= 1 and num <= 10:
    print (f"Tabla de multiplicar del numero {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
else:
    print("El numero ingresado no esta entre 1 y 10.")
