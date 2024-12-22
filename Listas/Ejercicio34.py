try:
	print("********************************************************")
	print(" 		     	   ")
	print("********************************************************")
	vector = []
	cont = 0
	cont_1 = 0
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	suma = 0
	for i in range(len(vector)):
		numero = vector[i]
		while numero != 0:
			dig = numero % 10
			if dig % 10 == 2:
				suma += dig
			numero //= 10
	print("La suma de los digitos 2 es: ",suma)
except ValueError:
	print("Errror")