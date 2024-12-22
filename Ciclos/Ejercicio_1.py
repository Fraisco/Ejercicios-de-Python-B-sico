try:
	n = int(input("Ingrese el numero: "))
	for i in range(n+1):
		print(i)
except ValueError:
	print("Errr")