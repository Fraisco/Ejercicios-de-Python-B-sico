try:
	numero = int(input("Ingrese el numero a sumar: "))
	suma = 0
	cont = 0
	while numero != 0:
		dg1 = numero % 10
		suma += dg1
		numero //= 10
		print(dg1)
except ValueError:
	print("Errr")