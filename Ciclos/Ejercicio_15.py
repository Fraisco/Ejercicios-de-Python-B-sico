try:
	cont = 0
	for i in range(80):
		if cont <= 20 and i % 3 == 0:
			print(f"el numero {i} es multiplo de 3")
			cont+=1
except ValueError:
	print("csjndjn")