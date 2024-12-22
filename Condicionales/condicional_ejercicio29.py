#Leer un número entero de cinco dígitos y determinar si es un número capicúo. Ej. 15651, 59895
try:
	numero = int(input("Ingrese un numero entero: "))
	if numero >= 10: 
		numero1 = str(numero)
		invertido = numero1[::-1]
		invertido1 = int(invertido)
		if numero == invertido1:
			print("Es capicuo")
		else:
			print("No es capicuo")
	else:
		print("No esta en el rango")
except ValueError:
	print("Valor errado")