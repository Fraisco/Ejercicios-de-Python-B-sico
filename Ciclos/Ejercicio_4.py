try:
	n = int(input("Ingrese el numero: "))
	n2 = int(input("Ingrese el numero dos: "))
	if n > n2:
		for i in range(n,n2):
			print(f"Los numeros comprendidos entre {n} y {n2} son: {i}")
	elif n2 > n:
		for i in range(n2,n):
			print(f"Los numeros comprendidos entre {n} y {n2} son: {i}")
	else:
		print("Ambos numeros son iguales")
except ValueError:
	print("Errr")