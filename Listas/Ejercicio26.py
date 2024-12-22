try:
	print("********************************************************")
	print(" 		     	   ")
	print("********************************************************")
	vector = []
	vector_copia = []
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	for i in range(len(vector)):
		factorial = 1
		numero = vector[i]
		pos = i
		for j in range(1,numero+1):
				factorial*=j
		vector_copia.append(factorial)
	print(f"El factorial de la lista anterior es: {vector_copia}")
except ValueError:
	print("Errror")