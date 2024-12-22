try:
	print("********************************************************")
	print(" 		     	   ")
	print("********************************************************")
	vector = []
	#Llenar el vector
	for i in range(3):
		n = int(input(f"Ingrese el valor para [{i}]: "))
		vector.append(n)
	print(vector)
	for i in range(len(vector)):
		numero = vector[i]
		print(f"Del numero {numero}:") 
		while numero != 0:
			dig = numero % 10
			print(f"Para el {dig}: ")
			for i in range(1, dig+1):
				print(i)
			print(" ")
			numero //= 10
		
except ValueError:
	print("Errror")