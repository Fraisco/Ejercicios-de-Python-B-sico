try:
	inicio = int(input("Ingrese el valor para el inicio: "))
	fin = int(input("Ingrese el valor del fin del ciclo: "))
	mas_o_menos = int(input("Ingrese el valor que incremente o descremento: "))
	if inicio > 0 and fin <= 200:
		for i in range(inicio,fin+1,mas_o_menos):
			if i % 2 == 0:	
				print(i)
			elif i % 2 != 0:
				print(i)
	else:
		print("Los valores son incorrectos")
except ValueError:
	print("Errrr")

	