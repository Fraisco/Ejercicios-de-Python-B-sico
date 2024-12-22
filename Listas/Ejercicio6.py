try:
	print("********************************************************")
	print("						")
	print("********************************************************")
	n1 = int(input("Ingrese un numero entero: "))
	n2 = int(input("Ingrese otro numero entero: "))
	cont1 = 0
	lista = []
	lista_primo = []	
	if n2 > n1:
		for i in range(n1, n2+1):
			lista.append(i)
		for i in range(len(lista)):
			var = lista[i]
			cont = 0
			for j in range(2, var // 2 + 1):
				if var % j == 0:
					cont += 1
			if cont == 0 and var != 0 and var != 1:
				if cont1 != 10:
					lista_primo.append(var)
					cont1 += 1
		print(lista_primo)
	elif n1 > n2:
		for i in range(n2, n1+1):
			lista.append(i)
		for i in range(len(lista)):
			var = lista[i]
			cont = 0
			for j in range(2, var // 2 + 1):
				if var % j == 0:
					cont += 1
			if cont == 0 and var != 0 and var != 1:
				if cont1 != 10:
					lista_primo.append(var)
					cont1 += 1
		print(lista_primo)
except ValueError:
	print("csjndjn")