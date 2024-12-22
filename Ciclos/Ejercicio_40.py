try:
	n = int(input("Ingrese el numero a sumarle el factorial: "))
	antes = 0
	siguiente = 1
	aux = 0
	for i in range(1,20+1):
		fibo = antes + siguiente
		antes = siguiente
		siguiente = fibo
		print(siguiente)
		if n == siguiente:
			aux = 1
	if aux == 1:
		print("El numero pertenece a la serie: ", n)
except ValueError:
	print("Errr")