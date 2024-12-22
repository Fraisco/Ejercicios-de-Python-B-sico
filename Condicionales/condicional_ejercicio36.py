# Leer un número entero de 4 dígitos y determinar si tiene más dígitos pares o impares
try:
	num = int(input("Ingrese un numero de cuatros digitos: "))
	if num >= 1000 and num <= 9999:
		dig1 = num % 10
		dig2 = (num // 10) % 10 
		dig3 = (num // 100) % 10
		dig4 = num // 1000
		cont = 0
		cont1 = 0
		if dig1 % 2 != 0:
			cont += 1
		if dig1 % 2 == 0:
			cont1 += 1
		if dig2 % 2 != 0:
			cont += 1
		if dig2 % 2 == 0:
			cont1 += 1
		if dig3 % 2 != 0:
			cont += 1 
		if dig3 % 2 == 0:
			cont1 += 1
		if dig4 % 2 != 0:		
			cont += 1
		if dig4 % 2 == 0:
			cont1 += 1
			if cont > cont1:
				print(f"Hay {cont} de digitos impares")
			elif cont1 > cont:
				print(f"Hay {cont1} de digitos pares")
			else:
				print("No hay digitos pares mayor que impares o al contrario")
	else:
		print("No se encuentra en el rango de 3 digitos")		
except ValueError:
	print("Valor ingresado erroneo")