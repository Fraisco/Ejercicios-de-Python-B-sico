#Leer un numero entero de dos digitos menor a 20 y determinar si es primo
try:
	numero = int(input("Ingrese un numero de dos digitos: "))
	if numero > 10 and numero <= 20:
		if numero == 11 or numero == 13 or numero == 17 or numero == 19:
			print(f"El numero {numero} es primo")
		else:
			print("El numero no es primo")
	else:
		print("Esta fuera de rango")
except ValueError:
	print("Valor errado")