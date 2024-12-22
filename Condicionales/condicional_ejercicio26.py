#Leer un número entero de cuatro dígitos y determinar a cuanto es igual la suma de sus dígitos
try:
	num = int(input("Ingrese un numero de cuatros digitos: "))
	if num >= 1000 and num <= 9999:
		dig1 = num % 10
		dig2 = (num // 10) % 10 
		dig3 = (num // 100) % 10
		dig4 = num // 1000
		print(dig1,dig2,dig3,dig4)
		suma = dig1 + dig2 + dig3 +	dig4
		print("La suma de sus digitos es igual a: %d"%suma)
	else:
		print("No se encuentra en el rango de 4 digitos")		
except ValueError:
	print("Valor ingresado erroneo")