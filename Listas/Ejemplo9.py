#Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito
try:
	print("********************************************************")
	print(" 			Mayor numero primo      	   ")
	print("********************************************************")
	vector = []
	mayor = 0
	repetido = 0
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	for i in range(len(vector)):
		if vector[i] > mayor:
			mayor = vector[i]
	for i in range(len(vector)):
		if vector[i] == mayor:
			repetido += 1
	print(f"El numero mayor {mayor} esta {repetido} cantidad veces repetido")		
except ValueError:
	print("Errror")