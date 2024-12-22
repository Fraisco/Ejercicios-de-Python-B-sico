try:
	print("********************************************************")
	print("				       	   ")
	print("********************************************************")
	
	lista = []
	mayor_par = 0
	pos = 0
	for i in range(10):
		numero = int(input("Ingrese el numero: "))
		lista.append(numero)
	for i in range(len(lista)):
		if lista[i] % 10 == 4:
			pos = i
			print(f"Los terminados 4 en la posicion: {pos}")
except ValueError:
	print("csjndjn")