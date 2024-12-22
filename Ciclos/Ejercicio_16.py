try:
	suma = 0
	prom = 0
	numero = int(input("Ingrese el numero: "))
	for i in range(numero+1):
		if i % 3 == 0:
			suma+=i
	prom = suma / numero
	print(f"El promedio de los multiplos de 3 es: {prom}, ya que su suma es: {suma}")		
except ValueError:
	print("csjndjn")