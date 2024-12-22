#Leer un número entero y si es múltiplo de 4 determinar si su último dígito es primo
try:
	num = int(input("Ingrese un numero entero: "))
	dig = num % 10
	if num % 4 == 0:
		if dig == 2 or dig == 3 or dig == 5 or dig == 7 :
			print("El ultimo digito es primo")
		else:
			print("No es primo")
	else:
		print("No es multiplo de 4") 
except ValueError:
	print("Error code: 21")