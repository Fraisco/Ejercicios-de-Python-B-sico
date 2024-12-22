try:
	print("********************************************************")
	print(" 		     	   ")
	print("********************************************************")
	vector = []
	cont = 0
	mayor = 0
	#Llenar el vector
	for i in range(5):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	suma = 0
	for i in range(len(vector)):
		numero = vector[i]
		while numero != 0:
			dig = numero % 10
			if dig % 2 == 0:
				suma+=dig
			numero //= 10
	print(f"La suma de los pares de todos los digitos de la lista: {suma}")
except ValueError:
	print("Errror")