""" Leer un número entero de 2 dígitos y si termina en 1 mostrar en pantalla su primer dígito, si termina en 2 mostrar en pantalla la suma de sus dígitos y si termina en 3 mostrar en pantalla el producto de sus dos dígitos"""
try:
	num = int(input("Ingrese un numero entero: "))
	dig1 = num % 10
	dig2 = num // 10
	if num >= 10 and num <= 99:
		if num % 10 == 1:
			print(f"Primer digito: {dig1}")
		elif num % 10 == 2:
			print(f"Segundo digito: {dig2}")
		elif num % 10 == 3:
			print(f"El producto es: {dig1*dig2}")
		else:
			print(" ")
	else:
		print("Fuera del limite")		
except ValueError:
	print("Error 213")