#Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales
try:
	numero = int(input("Ingrese un numero de dos digitos: "))
	if numero > 10 and numero <= 99:
		dig1 = numero % 10
		dig2 = numero // 10
		if dig1 == dig2:
			print("Los digitos son iguales")
		else:
			print("Los digitos no son iguales")
	else:
		print("Esta fuera de rango")
except ValueError:
	print("Valor errado")