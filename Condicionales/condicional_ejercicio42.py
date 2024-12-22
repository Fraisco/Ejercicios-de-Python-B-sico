
try:
	numero = int(input("Ingrese un numero de dos digitos: "))
	if numero > 10 and numero <= 99:
		dig1 = numero % 10
		dig2 = numero // 10
		diferencia = dig1 - dig2
		if diferencia % 2 == 0:
			print("El resultado de la resta es par:", diferencia)
		else:
			print("No es par el resultado:", diferencia)
	else:
		print("Esta fuera de rango")
except ValueError:
	print("Valor errado")