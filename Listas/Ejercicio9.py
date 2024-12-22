try:
	print("********************************************************")
	print("*                						              *")
	print("********************************************************")
	vector = []
	cont = 0
	#Llenar el vector
	for i in range(10):
		n = int(input("Ingrese el valor para el vector: "))
		vector.append(n)
	print(vector)
	#Iterar el vector para realizar la condicional
	for i in range(len(vector)):
		 
except ValueError:
	print("Errrrrr")