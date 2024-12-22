try:
	print("********************************************************")
	print(" 		     	   ")
	print("********************************************************")
	vector = []
	cont = 0
	mayor = 0
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	for i in range(len(vector)):
		numero = vector[i]
		cont = 0
		while numero != 0:
			dig = numero % 10
			cont += 1
			numero //= 10
		if 	mayor < cont:
			mayor = cont
			pos = i
	print(f"El numero con mayor digitos esta en la posicion [{pos}]") 
except ValueError:
	print("Errror")