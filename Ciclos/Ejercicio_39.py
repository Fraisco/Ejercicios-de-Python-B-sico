try:
	n = int(input("Ingrese el numero a comparar: "))
	antes = 0
	siguiente = 1
	for i in range(1,20+1):
		fibo = antes + siguiente
		antes = siguiente
		siguiente = fibo
		if n == fibo:
			print("Esta en la serie fibo")
		else:
			print("No esta en la serie")
except ValueError:
	print("csjndjn")
	