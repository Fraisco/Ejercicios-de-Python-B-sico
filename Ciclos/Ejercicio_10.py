try:
	suma = 0
	n = int(input("Ingrese el numero: "))
	for i in range(1,n+1):
		suma+=i
	print ("La suma es de: ",suma)
except ValueError:
	print("Errr")