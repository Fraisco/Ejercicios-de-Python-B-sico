try:
	print("********************************************************")
	print(" 			Menor numero primo      	   ")
	print("********************************************************")
	vector = []
	pos = 0
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	for i in range(len(vector)):
		repeat = False
		for j in range(i+1,len(vector)):
			if vector[i] == vector[j]:
				repeat = True
	if repeat == True:			
		print("Hay al menos un numero repetido en el vector")
	elif repeat == False:
		print("No hay numeros repetidos")
except ValueError:
	print("Errrrrr")
	