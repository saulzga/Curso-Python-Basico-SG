'''
Saúl Gómez García
Ejercicio #4 EXTRA
Curso Básico de Python
'''

#ENTRADAS
print("\n====DIMENSIONES DE MATRIZ 1===\n")
RowsM1 = int(input("Introduzca el número de FILAS que usará la matriz #1: "))
ColumsM1 = int(input("Introduzca el número de COLUMNAS que usará la matriz #1: "))

Matriz1=[]
print("\n====DATOS DE MATRIZ 1===")
print("\nIntroduzca los valores de izquierda a derecha empezando desde la primera fila\nPresione Enter despúes de cada valor")
for i in range(RowsM1):
    primera =[]
    for j in range(ColumsM1):
        primera.append(int(input()))
    Matriz1.append(primera)

print("\n====DIMENSIONES DE MATRIZ 2===\n")
RowsM2 = int(input("Introduzca el número de FILAS que usará la matriz #2: "))
ColumsM2 = int(input("Introduzca el número de COLUMNAS que usará la matriz #2: "))

Matriz2=[]
print("\n====DATOS DE MATRIZ 2===")
print("\nIntroduzca los valores de izquierda a derecha empezando desde la primera fila\nPresione Enter despúes de cada valor")
for i in range(RowsM2):
    segunda =[]
    for j in range(ColumsM2):
        segunda.append(int(input()))
    Matriz2.append(segunda)

MatrizP=[]
for i in range(RowsM1):
    producto =[]
    for j in range(ColumsM2):
        producto.append(0)
    MatrizP.append(producto)

Tupla1=tuple(map(tuple,Matriz1))
Tupla2=tuple(map(tuple,Matriz2))


#SALIDAS
print("\n===PRIMERA MATRIZ===\n")
for i in range(RowsM1):
    for j in range(ColumsM1):
        print(Tupla1[i][j], end=" ")
    print()

print("\n===SEGUNDA MATRIZ===\n")
for i in range(RowsM2):
    for j in range(ColumsM2):
        print(Tupla2[i][j], end=" ")
    print()

print("\n===MATRIZ PRODUCTO===\n")
for i in range(len(Tupla1)):
    for j in range(len(Tupla2[0])):
        for k in range(len(Tupla2)):
            MatrizP[i][j] += Tupla1[i][k] * Tupla2[k][j]

for r in MatrizP:
    print(*r)
    