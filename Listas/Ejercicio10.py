try:
	print("********************************************************")
	print("                         **                             ")
	print("********************************************************")
	vector = []
	pos = 0
	#Llenar el vector
	for i in range(5):
		n = int(input("Ingrese el valor para el vector: "))
		vector.append(n)
	print(vector)
	#Iterar el vector para realizar la condicional
	for i in range(len(vector)):
		if vector[i] >= 100:
			pos = i
			print(f"Los valores mayores de 3 digitos estan: {pos} posicion") 
except ValueError:
	print("Errrrrr")