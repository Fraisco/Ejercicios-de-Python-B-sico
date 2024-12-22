#Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito
try:
	print("********************************************************")
	print(" 	Los 10 multiplos desde 100 hasta 300      	   ")
	print("********************************************************")
	vector = []
	cont1 = 0
	#Llenar el vector
	for i in range(100,300+1,1):
		cont = 0
		var = i
		for j in range(2, i // 2 + 1):
			if var % j == 0:
				cont += 1
		if cont == 0 and var != 0 and var != 1:
			if cont1 != 10:
				vector.append(var)
				cont1 += 1
	print(vector)
except ValueError:
	print("Errrrrr")