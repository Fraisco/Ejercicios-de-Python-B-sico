#Leer un numero y determinar si el numero ingresado por el usuario termina en 4
try:
	N = int(input("Ingrese un numero: "))
	if N == 4 or N % 10 == 4:
		print(f"Tu numero {N} termina en 4")
	else:
		print("El numero ingresado no termina en 4|")
except ValueError:
	print("Error de valor ingresado")