'''
Saúl Gómez García
Ejercicio #4
Curso Básico de Python
'''
#Almacenar las matrices dadas e
Tupla1=((1, 2, 3), (4, 5, 6))
Tupla2=((-1, 0), (0, 1), (1, 1))

#Crea una matriz de la misma dimensión del producto de las dos primeras
#y las pone en 0 para poder sobre escribir posteriormente los valores
MatrizP=[]
for i in range(len(Tupla1)):
    producto =[]
    for j in range(len(Tupla2[0])):
        producto.append(0)
    MatrizP.append(producto)

#SALIDAS
print("\n===PRIMERA MATRIZ===\n")
for i in range(len(Tupla1)):
    for j in range(len(Tupla1[0])):
        print(Tupla1[i][j], end=" ")
    print()

print("\n===SEGUNDA MATRIZ===\n")
for i in range(len(Tupla2)):
    for j in range(len(Tupla2[0])):
        print(Tupla2[i][j], end=" ")
    print()

print("\n===MATRIZ PRODUCTO===\n")
for i in range(len(Tupla1)):
    for j in range(len(Tupla2[0])):
        for k in range(len(Tupla2)):
            MatrizP[i][j] += Tupla1[i][k] * Tupla2[k][j]

for r in MatrizP:
    print(*r)
    