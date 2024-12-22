#Leer dos números enteros y determinar cuál es el mayor
try:
	numero = int(input("Ingrese un numero de dos digitos: "))
	if numero > 9 and numero <= 99:
		dig1 = numero % 10
		dig2 = numero // 10
		if dig1 > dig2:
			print(f"El digito {dig1} es mayor a {dig2}")
		elif:
			print(f"El digito {dig2} es mayor a {dig1}")
	else:
		print("Esta fuera de rango")
except ValueError:
	print("Valor errado")