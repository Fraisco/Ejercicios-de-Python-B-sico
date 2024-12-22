try:
	print("********************************************************")
	print(" 			      	   ")
	print("********************************************************")
	vector = []
	pos = 0
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	for i in range(len(vector)):
		if vector[i] % 5 == 0:
			print(f"El numero {vector[i]} esta en la posicion: {i}")
except ValueError:
	print("Errrrrr")