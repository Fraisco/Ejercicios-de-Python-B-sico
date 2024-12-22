try:
	print("********************************************************")
	print(" 			Cuadrado del numero      	   ")
	print("********************************************************")
	vector = []
	mayor_primo = 0
	pos = 0
	#Llenar el vector
	for i in range(10):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	for i in range(len(vector)):
		cuadrado_numero = 0	
		cuadrado_numero = vector[i] ** 2
		print(f"El cuadrado de {vector[i]} es: {cuadrado_numero}")
except ValueError:
	print("Errrrrr")