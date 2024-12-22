try:
	print("********************************************************")
	print("	*Divisores exactos*")
	print("********************************************************")
	vector = []
	cont = 0
	#Llenar el vector
	for i in range(10):
		n = int(input("Ingrese el valor para el vector: "))
		vector.append(n)
	print(vector)
	#Iterar el vector para realizar la condicional
	num = int(input("Ingrese un numero para dividorlo entre los valores de la lista: "))
	for i in range(len(vector)):	
		if vector[i] % num == 0:
			cont += 1
	print(f"Hay {cont} cantidad de divisores exactos entre el numero y los valores de la lista")
except ValueError:
	print("Errrrrr")