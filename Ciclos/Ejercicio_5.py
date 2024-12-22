try:
	n = int(input("Ingrese el numero: "))
	n1 = int(input("Ingrese el numero 2: "))
	if n > n1:
		for i in range(n1,n):
			if i % 10 == 4:
				print(f"Los numeros comprendidos entre {n} y {n1} son: {i}")
	if n < n1: 
		for i in range(n,n1):
			if i % 10 == 4:
				print(f"Los numeros comprendidos entre {n} y {n1} son: {i}")
except ValueError:
	print("Errr")