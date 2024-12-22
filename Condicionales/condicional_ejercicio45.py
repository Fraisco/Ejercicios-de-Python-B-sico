#Leer un número entero y si es múltiplo de 4 determinar si su último dígito es primo
try:
	num = int(input("Ingrese un numero entero de 2 digitos: "))
	dig1 = num % 10
	dig2 = num // 10
	if num > 9 and num < 100:
		if num % 2 == 0:
			print(f"La suma de sus digitos es: {dig1 + dig2}")
		elif num % 5 == 0 and num < 30:
			print(f"El primer digito es {dig1}")
except ValueError:
	print("Error code: 21")