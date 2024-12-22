#Leer un numero entero de dos digitos y determinar a cuanto es igual la suma de sus digitos
try:
	numero = int(input("Ingrese un numero de dos digitos: "))
	if numero >= 10:
		dig1 = numero % 10
		dig2 = numero // 10
		suma = dig1 + dig2
		print(f"La suma de los digitos {dig1} y {dig2} es igual a: {suma}")
except ValueError:
	print("Valor errado")