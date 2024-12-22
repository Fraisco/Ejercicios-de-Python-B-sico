try:
	print("********************************************************")
	print(" 		     	   ")
	print("********************************************************")
	vector = []
	suma = 0
	promedio = 0
	cont = 0
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	for i in range(len(vector)):
		suma += vector[i]
	promedio = suma // 10
	for i in range(vector[i]):
		if vector[i] == promedio:
			cont = 1
	if cont == 1:
		print(f"El promedio se encuentra en la lista: {promedio}")
	elif cont == 0:
		print(f"El promedio no se encuentra en la lista: {promedio}")
except ValueError:
	print("Errror")