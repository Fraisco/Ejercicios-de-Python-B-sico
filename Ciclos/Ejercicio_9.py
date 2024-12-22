try:
	for i in range(25+1,205+1):
		if i % 10 == 6:
			print(i)
except ValueError:
	print("Errr")