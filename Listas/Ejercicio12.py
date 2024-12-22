try:
	print("********************************************************")
	print(" 		     	   ")
	print("********************************************************")
	vector = []
	suma = 0
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	for i in range(len(vector)):
		suma += vector[i]
	print(f"El promedio de la suma de todos los datos es de: {suma // 10}")	
except ValueError:
	print("Errror")