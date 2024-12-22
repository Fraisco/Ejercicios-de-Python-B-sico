vector = []
mayor = 0
pos_min = 0
pos_mayor = 0
for i in range(4):
	n = int(input("Mensaje: "))
	vector.append(n)
print(vector)

for i in range(len(vector)):
	if vector[i] % 2 == 0:
		print(vector[i])
	if vector[i] % 2 != 0:
		print(vector[i])

for i in range(len(vector)):
	if vector[i] > mayor:
		mayor = vector[i]
		pos_mayor = i 
print("El numero mayor es: ",mayor, "esta en la posicion: ",pos_mayor)

menor = vector[0]
for i in range(len(vector)):
	if vector[i] < menor:
		menor = vector[i]
		pos_min = i
print("El numero menor es: ",menor, "esta en la posicion: ",pos_min)