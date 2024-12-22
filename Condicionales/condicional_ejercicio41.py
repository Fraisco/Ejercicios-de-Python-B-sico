#. Leer dos números enteros de dos dígitos y determinar si la diferencia entre los dos es un número primo
try:
	numero = int(input("Ingrese un numero de dos digitos: "))
	if numero > 10 and numero <= 99:
		dig1 = numero % 10
		dig2 = numero // 10
		diferencia = dig1 - dig2
		if diferencia == 2 or diferencia == 3 or diferencia == 5 or diferencia == 7:
			print("El resultado de la resta es primo:", diferencia)
		else:
			print("No es primo el resultado:", diferencia)
	else:
		print("Esta fuera de rango")
except ValueError:
	print("Valor errado")