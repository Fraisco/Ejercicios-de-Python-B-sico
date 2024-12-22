try:
	print("********************************************************")
	print("*                						              *")
	print("********************************************************")
	vector = []
	cont = False
	#Llenar el vector
	for i in range(10):
		n = int(input("Ingrese el valor para el vector: "))
		vector.append(n)
	print(vector)
	#Iterar el vector para realizar la condicional
	num = int(input("Ingrese un numero para ver si esta en la lista: "))
	for i in range(len(vector)):
		if vector[i] == num:
			cont = True
	if cont == True:
		print("El numero se encuentra en la lista")
	else: 
		print("No se encuentra en la lista") 
except ValueError:
	print("Errrrrr")