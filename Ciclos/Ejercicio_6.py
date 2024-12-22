try:
	n = int(input("Ingrese el numero de 3 digitos: "))
	dg1 = n % 10
	dg2 = (n // 10) % 10
	dg3 = n // 100
	if n >= 100:
		for i in range(1,dg1+1):
			print(i)
		print("\n")
		for i in range(1,dg2+1):
			print(i)
		print("\n")
		for i in range(1,dg3+1):
			print(i)
		print("\n")
	else:
		print("No es de 3 dígitos")	
except ValueError:
	print("Errr")