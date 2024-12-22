try:
	n = int(input("Ingrese el numero: "))
	for i in range(1,n+1):
		if n % i == 0:
			print(f"El divisor exacto de {n} es: {i}")
except ValueError:
	print("Errr")