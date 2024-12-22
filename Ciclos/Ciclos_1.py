try:
	inicio = int(input("Ingrese el valor para el inicio: "))
	fin = int(input("Ingrese el valor del fin del ciclo: "))
	mas_o_menos = int(input("Ingrese el valor que incremente o descremento: "))
	if inicio < fin:
		for i in range(inicio,fin+1,mas_o_menos):
			print(i)
	elif fin < inicio:
		for i in range(inicio,fin-1,mas_o_menos):
			print(i)
	else:
		print("Son valores iguales del inicio y fin")
except ValueError:
	print("Errrr")

	