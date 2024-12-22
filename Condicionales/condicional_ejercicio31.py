#Leer un número entero y determina si es igual a 10
try:
	numero = int(input("Ingrese un numero entero: "))
	if numero == 10:
		print("Es igual a 10")
	else:
		print("No es 10")		
except ValueError:
	print("Valor errado")