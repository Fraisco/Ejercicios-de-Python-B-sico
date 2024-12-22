#Leer tres números enteros (de dos dígitos) y determinar cuál es el mayor. Usar solamente dos variables
try:
	num1 = int(input("Ingrese el primer numero: "))
	num2 = int(input("Ingrese el segundo numero: "))
	if (num1 > 9 and num1 < 100) and (num2 > 9 and num2 < 100):
		num1 = num1 * 100
		num1 = num1 + num2
		num2 = int(input("Ingrese el nuevo valor para el segundo numero: "))
		if num2 > 9 and num2 < 100:
			if ((num1 // 100) > num2) and ((num1 // 100) > (num1 % 100)):
				print("numero 1 es mayor")
			elif ((num1 % 100) > num2) and ((num1 % 100) > (num1 // 100)):
				print("numero 2 es mayor")
			elif (num2 > (num1 // 100)) and (num2 > (num1 // 100)):
				print("numero 3 es mayor")
			else:
				print("Todos son iguales")
		else:
			print("El nuevo valor del segundo no es de 2 digitos")
	else:
		print("No es de dos digitos los numeros ingresados") 
except ValueError:
	print("Valor errado")