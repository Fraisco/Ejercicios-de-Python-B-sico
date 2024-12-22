#Leer un número entero de tres dígitos y determinar si alguno de sus dígitos es igual a la suma de los otros dos.
try:
	num = int(input("Ingrese un numero de 2 dígitos: "))
	dig = num % 10
	if num > 0 and num < 100:
		if num % 4 == 0:
			print(f"Como es multiplo de 4, la mitad del numero es {num // 2} ")
		elif num % 5 == 0:
			print(f"Como es multiplo de 5, El numero al cuadrado es {num ** 2}")
		elif num % 6 == 0:
			print(f"Como es multiplo de 6, el primer digito es: {dig}")
		else:
			print("No hay multiplo válido")
	else:
		print("El numero es mayor a 100")
except ValueError:
		print("Valor errado")