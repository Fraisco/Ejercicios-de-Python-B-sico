#Leer un número entero menor que mil y determinar cuántos dígitos tiene
try:
	num = int(input("Ingrese un numero entero: "))
	if num < 1000:
		if num > 0 and num < 9:
			print("El numero es de un digito")
		elif num > 9 and num < 100:
			print("El numero es de dos digito")
		elif num > 99 and num < 1000:
			print("El numero es de tres digitos")
		else:
			print(" ")
	else:
		print("Fuera del limite")		
except ValueError:
	print("Error 213")