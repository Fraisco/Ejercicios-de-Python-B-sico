try:
	print("********************************************************")
	print(" 		     	   ")
	print("********************************************************")
	vector = []
	mayor = 0
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	for i in range(len(vector)):
		numero = vector[i]
		suma = 0
		while numero != 0:
			dig = numero % 10
			suma += dig
			numero //= 10
			if suma	> mayor:
				mayor = suma
	print(f"La suma mayor es: {mayor}")  
except ValueError:
	print("Errror")