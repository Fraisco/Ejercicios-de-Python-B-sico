try:	
	numero = int(input("Ingrese el numero a factorizar: "))
	factorial = 1
	suma = 0
	cont = 0
	while numero > 0:
		dig = numero % 10
		cont+=1
		for i in range(1,dig+1):
			factorial *= i
			suma += factorial
		print(f"La sumatoria factorial de el digito {dig}: {suma}")
		factorial = 1
		numero//=10
except ValueError:
	print("Errrr")