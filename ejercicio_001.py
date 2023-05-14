'''
Saúl Gómez García
Ejercicío #1
Curso Básico de Python
'''

#CONSTANTES
AÑO_ACTUAL = 2023

#===ENTRADAS===

nombre = input("¿Cuál es tu nombre? ")
apellido1 = input("¿Cuál es tu primer apellido? ")
apellido2 = input("¿Cuál es tu segundo apellido? ")

año_nac = int(input("¿En qué año naciste? "))   
mes_dia = input("¿En qué mes y día naciste? (en el siguiente formato \"mm-dd\")")


#Concatenación de nombre y conteo de vocales y letras
nombre_completo = nombre + " " + apellido1 + " " + apellido2
nombre_caract = nombre + apellido1 + apellido2 #variable sin espacios
nc_min= nombre_completo.lower()
nc_may= nombre_completo.upper()
VocalesNombre = len([char for char in nombre_completo if char in "aeiouAEIOUáéíóúÁÉÍÓÚ"])
LetrasNombre = len(nombre_completo) - nombre_completo.count(' ')

#Separación de los dígitos de la fecha para manipular individualmente
lista_md = mes_dia.split("-")
mes, dia = lista_md

#Cáculo de la edad
edad = AÑO_ACTUAL - año_nac

#====SALIDAS====

print("\nEstos son los resultados \n")

print("Este es tu nombre completo en mayúsculas: " + nc_may)
print("Este es tu nombre completo en minúsculas: " + nc_min)
print(f"Esta es tu fecha de nacimiento \"{dia}-{mes}-{año_nac}\"")
print(f"Esta es tu edad: {edad}")
print(f"Tu nombre completo tiene {VocalesNombre} vocales")
print(f"Tu nombre completo tiene {LetrasNombre} letras")
print(f"¿Tu edad es un carácter de tipo número? {isinstance(edad, int)}")

#Este print dará FALSE si se usa nombre_completo porque Python no considera los espacios en blanco como alfanuméricos, 
#   por eso se usa la variable nombre_caract con solo las letras
print(f"¿Tu nombre completo es un caracter de tipo alfanumérico? {nombre_caract.isalnum()}") 

print(f"Tu edad en 10 años será {edad + 10}")
print(f"La media de tu edad actual y edad en 20 años es {(edad + edad + 20)/2}")

#====FIN====
   
