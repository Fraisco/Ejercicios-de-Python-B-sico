try:
	print("********************************************************")
	print(" 		     	   ")
	print("********************************************************")
	vector = []
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	cont_1 = 0
	for i in range(len(vector)):
		var = vector[i]
		cont = 0
		for j in range(2, var // 2 + 1):
			if var % j == 0:
				cont += 1
		if cont == 0 and var != 0 and var != 1:
			if var % 10 == 3:
				cont_1 += 1
	print(f"Hay {cont_1} cantidad de veces ")
except ValueError:
	print("Errror")