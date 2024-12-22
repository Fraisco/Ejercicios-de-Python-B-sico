# Leer un número entero y determinar si es múltiplo de 7.
try:
	numero = int(input("Ingrese un numero entero digitos: "))
	if numero % 7 == 0:
		print(f"El numero {numero} es multiplo de 7")
	else:
		print("No es multiplo de 7") 		
except ValueError:
	print("Valor errado")