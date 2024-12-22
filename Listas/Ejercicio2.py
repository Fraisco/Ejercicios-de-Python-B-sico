try:
	print("********************************************************")
	print(" 			Mayor numero par       	   ")
	print("********************************************************")
	
	lista = []
	mayor_par = 0
	pos = 0
	for i in range(10):
		numero = int(input("Ingrese el numero: "))
		lista.append(numero)
	for i in range(len(lista)):
		if lista[i] % 2 == 0:
			if lista[i] > mayor_par:
				mayor_par = lista[i]
				pos = i
	print(f"mayor par es: {mayor_par} en la posicion: {pos}")
except ValueError:
	print("csjndjn")