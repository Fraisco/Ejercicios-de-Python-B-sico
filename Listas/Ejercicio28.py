try:
	print("********************************************************")
	print(" 		     	   ")
	print("********************************************************")
	vector = []
	cont = 0
	cont_1 = 0
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	for i in range(len(vector)):
		numero = vector[i]
		print(f"El numero {numero} de la posicion {i}")
		for j in range(1,numero+1):
			print(j)
		print("\n")
except ValueError:
	print("Errror")