try:
	numero = int(input("Ingrese el valor de un numero entero: "))
	numero2 = int(input("Ingrese el valor del un numero entero: "))
	if numero > numero2:
		for i in range(numero2,numero+1):
			if i % 5 == 0:
				print(i)
	elif numero2 > numero:
		for i in range(numero,numero2+1):
			if i % 5 == 0:
				print(i)
	else:
		print("Son el mismo numero")
except ValueError:
	print("csjndjn")