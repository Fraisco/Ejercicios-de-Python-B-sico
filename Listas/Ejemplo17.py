try:
	print("********************************************************")
	print(" 		     	   ")
	print("********************************************************")
	vector = []
	cont = 0
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	for i in range(len(vector)):
		if vector[i] < 0:
			cont += 1
	print(f"Hay {cont} de numeros negativos en la lista")
except ValueError:
	print("Errror")