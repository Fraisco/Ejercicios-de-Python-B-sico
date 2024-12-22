#Leer un número entero de tres dígitos y determinar cuántos dígitos primos tiene
try:
	num = int(input("Ingrese un numero de tres digitos: "))
	if num >= 100 and num <= 999:
		dig1 = num % 10
		dig2 = (num // 10) % 10 
		dig3 = num // 100
		cont = 0
		if dig1 == 2 or dig1 == 3 or dig1 == 5 or dig1 == 7:
			cont += 1
		if dig2 == 2 or dig2 == 3 or dig2 == 5 or dig2 == 7:
			cont += 1
		if dig3 == 2 or dig3 == 3 or dig3 == 5 or dig3 == 7:
			cont += 1 	
		print(f"Hay {cont} de digitos primos")
	else:
		print("No se encuentra en el rango de 3 digitos")		
except ValueError:
	print("Valor ingresado erroneo")