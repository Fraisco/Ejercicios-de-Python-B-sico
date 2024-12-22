#. Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus dígitos
try:
	numero = int(input("Ingrese un numero de tres digitos: "))
	if numero >= 100:
		dig1 = numero % 10
		dig2 = (numero // 10) % 10 
		dig3 = numero // 100
		suma = dig1 + dig2 + dig3
		print(f"La suma de los digitos {dig1} y {dig2} más {dig3} es igual a: {suma}")
	else:
		print("El numero no está en el rango")
except ValueError:
	print("Valor errado")