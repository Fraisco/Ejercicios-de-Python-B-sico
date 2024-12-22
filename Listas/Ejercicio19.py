try:
	print("********************************************************")
	print("		Numero menor de un vector      	   ")
	print("********************************************************")
	vector = []
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	menor = vector[0]
	for i in range(len(vector)):
		if vector[i] < menor:
			menor = vector[i]
	print(f"El numero menor es {menor}")		
except ValueError:
	print("Errror")