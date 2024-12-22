try:	
	numero = int(input("Ingrese el numero a factorizar: "))
	factorial = 1
	suma = 0
	for i in range(1,numero+1):
		factorial*=i
		suma+=factorial
	print(f"El factorial de {numero} es: {factorial}")
	print(f"El promedio de la {suma} es: {suma // numero}")
except ValueError:
	print("Errrr")