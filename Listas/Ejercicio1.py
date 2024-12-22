try:
	print("********************************************************")
	print("*               los primeros 10 elementos              *")
	print("********************************************************")
	lista = []
	a = 0
	b = 1
	lista.append(a)
	lista.append(b)
	for i in range(10 - 2):
		suma = a + b 
		a = b
		b = suma
		lista.append(b)
	print(lista)
except ValueError:
	print("Errrrrr")