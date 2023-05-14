'''
Ejercicio #2 - Extra Curso de Python Básico
Saúl Gómez García
'''
#====ENTRADAS===

while True:
    try:
        Tamaño = int(input("¿Cuantos nombres quiere catalogar?"))   
    except ValueError:
        print("\nEscriba la cantidad en números enteros")
        continue
    break

ListaNombres =[]
SexoList =  []

for i in range(Tamaño):
    ListaNombres.append(input("Escriba el nombre #%d: "%(i+1)))
    while True:
        Sexo = input("¿Cuál el sexo del nombre #%d? (M/F):"%(i+1))
        if Sexo in ("M","m","F","f"):
            SexoList.append(Sexo)
            break
        else:
            print("Por favor, introduzca M o F como su sexo ")
            continue

GrupoA=[]
GrupoB=[]      

for i in range(Tamaño):
    if (SexoList[i] == 'F' and ListaNombres[i][0] < 'M') or (SexoList[i] =='M' and ListaNombres[i][0]>'N'):  
        GrupoA.append(ListaNombres[i])
    else:
       GrupoB.append(ListaNombres[i])

#====SALIDAS====
print(f"\nPertenecen al grupo A:") 
for x in range(len(GrupoA)): 
    print(GrupoA[x])

print(f"\nPertenecen al grupo B:") 
for x in range(len(GrupoB)): 
    print(GrupoB[x])