# Leer un número entero de tres dígitos y determinar cuántos dígitos pares tiene
try:
	num = int(input("Ingrese un numero de tres digitos: "))
	if num >= 100 and num <= 999:
		dig1 = num % 10
		dig2 = (num // 10) % 10 
		dig3 = num // 100
		cont = 0
		if dig1 % 2 == 0:
			cont += 1
		if dig2 % 2 == 0:
			cont += 1
		if dig3 % 2 == 0:
			cont += 1 	
		print(f"Hay {cont} de digitos pares")
	else:
		print("No se encuentra en el rango de 3 digitos")		
except ValueError:
	print("Valor ingresado erroneo")