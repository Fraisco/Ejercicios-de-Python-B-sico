try:
	num = int(input("Ingrese un numero entero: "))
	cont = 0
	while num != 0:
		dig = num % 10
		cont += 1
		print(dig)
		num //= 10
except ValueError:
	print("Errr")