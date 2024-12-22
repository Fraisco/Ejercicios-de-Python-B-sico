try:
	n = int(input("Ingrese el numero: "))
	for i in range(n+1):
		if i % 2 == 0:
			print(i)
except ValueError:
	print("Errr")