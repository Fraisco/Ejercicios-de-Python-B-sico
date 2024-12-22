try:
	lista = []
	cont = 0
	antes = -1
	siguiente = 1
	for i in range(1,20+1):
		fibo = antes + siguiente
		antes = siguiente
		siguiente = fibo
		if cont != 10:
			lista.append(siguiente)
			cont += 1
	print(lista)		
except ValueError:
	print("csjndjn")