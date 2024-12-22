try:
	cont = 0
	for i in range(1000+1):
		numero1 = str(i)
		invertido = numero1[::-1]
		invertido1 = int(invertido)
		if i == invertido1:
			cont = cont + 1
	print(f"Y hay: {cont} numeros capicúo" )
except ValueError:
	print("Errr")