#Leer un número entero de dos dígitos y determinar si un dígito es múltiplo del otro.
try:
	numero = int(input("Ingrese un numero de dos digitos: "))
	if numero > 10 and numero <= 99:
		dig1 = numero % 10
		dig2 = numero // 10
		if dig1 % dig2 == 0 or dig2 % dig1 == 0:
			print("Los digitos son multiplos entre sí")
		else:
			print("Los digitos no son multiplos entre si")
	else:
		print("Esta fuera de rango")
except ValueError:
	print("Valor errado")