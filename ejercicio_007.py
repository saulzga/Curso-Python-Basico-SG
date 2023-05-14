'''
Saúl Gómez García
Ejercicio #7
Curso Básico de Python
'''

Frase =input ("Escriba una frase: ")

diccionario = {}

for i in Frase.split(" "):
    Palabras = Frase.split(" ")
    for j in range(len(Palabras)):
        Longitud = len(Palabras[j])
        diccionario[Palabras[j]] = Longitud

print("\nA continuación se muestran las palabras de su frase, seguida de la longitud de cada una \n")
print(diccionario)
