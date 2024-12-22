#Leer dos números enteros y determinar cuál es múltiplo de cuál
try:
	num = int(input("Ingrese un numero entero: "))
	num1 = int(input("Ingrese otro numero entero: "))
	if num % num1 == 0:
		print("El primer numero es multiplo del segundo")
	else:
		print("El segundo numero es multiplo del primero")			
except ValueError:
	print("Valor ingresado erroneo")