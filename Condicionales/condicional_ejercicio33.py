#Leer un número entero y determinar si termina en 7
try:
	numero = int(input("Ingrese un numero entero digitos: "))
	if numero % 10 == 7:
		print(f"El numero {numero} termina en 7")
	else:
		print("No termina en 7") 		
except ValueError:
	print("Valor errado")