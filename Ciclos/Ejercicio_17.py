try:
	x = int(input("Ingrese el  valor entero de x: "))
	y = int(input("Ingrese el  valor entero de y: "))
	promx = 0
	promy = 0
	sumax = 0
	sumay = 0
	for i in range(x+1):
		if i % 2 == 0:
			sumax += i
	promx = sumax / x
	for j in range(y+1):
		if j % 5 == 0:
			sumay += j
	promy = sumay / y
	if promx > promy:
		print(f"El promedio de los multiplos de 2: [{promx}], es mayor a el promedio de los multiplos de 5: [{promy}]")
	else:
		print(f"El promedio de los multiplos de 5: [{promy}], es mayor a el promedio de los multiplos de 2: [{promx}]")	
except ValueError:
	print("csjndjn")