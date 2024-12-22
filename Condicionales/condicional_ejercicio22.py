#Leer un número entero de tres dígitos y determinar si el primer dígito es igual al último
try:
	num = int(input("Ingrese un numero de tres digitos: "))
	if num >= 100 and num <= 999:
		dig1 = num % 10 
		dig3 = num // 100
		if dig1 == dig3:
			print("El primer y ultimo digito son iguales")
		else:
			print("No son iguales el primer y ultimo digito")
	else:
		print("Tiene que ser de tres digitos")				
except ValueError:
	print("Valor ingresado erroneo")