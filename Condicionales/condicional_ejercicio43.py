#. Leer dos números enteros de dos dígitos y determinar si la diferencia entre los dos numeros es un divisor exacto de los numeros
try:
	numero = int(input("Ingrese un numero de dos digitos: "))
	if numero > 10 and numero <= 99:
		dig1 = numero % 10
		dig2 = numero // 10
		diferencia = dig1 - dig2
		if dig1 % diferencia == 0 or diferencia % dig1 == 0:
			print(f"La diferencia de {diferencia} es divisor exacto de {dig1}")
		elif dig2 % diferencia == 0 or  diferencia % dig2 == 0:
			print(f"La diferencia de {diferencia} es divisor exacto de {dig2}")
		else:
			print("La diferencia de los digitos no es divisor de los dos digitos")	
	else:
		print("Esta fuera de rango")
except ValueError:
	print("Valor errado")