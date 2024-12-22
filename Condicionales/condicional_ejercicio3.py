#Leer un numero y determinar si es negativo

try:
	num_neg = int(input("Ingrese un numero negativo: "))
	if num_neg < 0:
		print(f"Su numero ingresado {num_neg} es negativo")
	else:
		print(f"Su numero {num_neg} es positivo")
except ValueError:
	print("Valor errado")