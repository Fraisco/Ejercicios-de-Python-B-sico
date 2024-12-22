try:
	lista = []
	cont = 0
	for i in range(10):
		numero = int(input("Ingrese el numero: "))
		lista.append(numero)
	for i in range(len(lista)):
		if lista[i] % 3 == 0:
			cont += 1
	print(lista)
	print(f"Hay {cont} de valores que son multiplos de 3")
except ValueError:
	print("csjndjn")