#Leer dos números enteros de dos dígitos y determinar si la suma de los dos números origina un número par
try:
	numero = int(input("Ingrese un numero de dos digitos: "))
	numero1 = int(input("Ingrese otro numero de dos digitos: "))
	if numero > 9 and numero <= 99 and numero1 > 9 and numero1 <= 99:
		suma = numero + numero1
		if suma % 2 == 0:
			print(f"La suma {suma} es un numero par")
		else:
			print("La suma no es un numero par")
	else:
		print("Esta fuera de rango")
except ValueError:
	print("Valor errado")