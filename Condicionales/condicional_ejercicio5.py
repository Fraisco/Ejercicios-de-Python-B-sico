#Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
try:
	num = int(input("Ingrese un numero de dos digitos: "))
	if num > 10 and num <= 99:
		dig1 = num % 10
		dig2 = num // 10
		if dig1 % 2 == 0 and dig2 % 2 == 0:
			print(f"Ambos digitos del numero {num} son pares")
		else:
			print(f"Los digitos no son pares")
	else:
		print("No es de dos digitos")
except ValueError:
	print("Valor errado")