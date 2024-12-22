#Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus dígitos

try:
	num = int(input("Ingrese un numero de tres digitos: "))
	if num >= 100 and num <= 999:
		dig1 = num % 10
		dig2 = (num // 10) % 10 
		dig3 = num // 100
		if dig1 == dig2 or dig1 == dig3 or dig2 == dig3:
			print("Hay dos digitos que son iguales")
		else:
			print("No hay digitos que sean iguales")
	else:
		print("No se encuentra en el rango de 3 digitos")		
except ValueError:
	print("Valor ingresado erroneo")