#Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito
try:
	print("********************************************************")
	print(" 			Mayor numero primo      	   ")
	print("********************************************************")
	vector = []
	mayor_primo = 0
	pos = 0
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	for i in range(len(vector)):
		var = vector[i]
		cont = 0
		for j in range(2, vector[i] // 2 + 1):
			if var % j == 0:
				cont += 1
		if cont == 0 and var != 0 and var != 1:
			if var > mayor_primo:
				mayor_primo = var
				pos = i
	print(f"El numero mayor primo {mayor_primo} esta en la posicion: [{pos}]")
except ValueError:
	print("Errrrrr")