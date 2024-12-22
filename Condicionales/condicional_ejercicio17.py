#Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito
try:
	numero = int(input("Ingrese un numero de tres digitos: "))
	if numero >= 100:
		dig1 = numero % 10
		dig2 = (numero // 10) % 10 
		dig3 = numero // 100
		print(dig1,dig2,dig3)
		if dig1 > dig2 and dig3:
			print(f"El dig1 es mayor en la posición 3")
		elif dig2 > dig3 and dig1:
			print(f"El dig2 es mayor en la posición 2")
		elif dig3 > dig2 and dig1:
			print(f"El dig3 es mayor en la posición 1")
		else:
			print(f"El dig3 es el mayor en la posicion 3")	
	else:
		print("El numero no está en el rango")
except ValueError:
	print("Valor errado")