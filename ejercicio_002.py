'''
Ejercicio #2 Curso de Python Básico
Saúl Gómez García
'''
#====ENTRADAS===
Nombre = input ("Por favor, introduce tu nombre:")
Sexo = input("Por favor introduce tu sexo (M/F):")

#====SALIDAS====

#El grupo A está formado por las mujeres con un nombre anterior a la M
#y los hombre con un nombre posterior a la N
if (Sexo[0]== 'F' and Nombre[0] < 'M') or (Sexo[0]=='M' and Nombre[0]>'N'):  
    print("\nPerteneces al grupo A")
#y el grupo B por el resto
else:
    print("\nPerteneces al grupo B")
