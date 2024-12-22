try:
	print("********************************************************")
	print("*                						              *")
	print("********************************************************")
	vector = []
	#Llenar el vector
	for i in range(10):
		n = int(input("Ingrese el valor para el vector: "))
		vector.append(n)
	print(vector)
	#Iterar el vector para realizar la condicional
	num = int(input("Ingrese un numero para ver si esta en la lista: "))
	cont = 0
	n = 0
	for i in range(len(vector)):
		n = vector[i] % 10
		if n == num:
			cont += 1
	print(f"Las veces que el numero leido y el ultimo digito de los de la listas son: {cont}")
except ValueError:
	print("Errrrrr")