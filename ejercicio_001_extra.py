'''
Saúl Gómez García
Ejercicío #1
Curso Básico de Python
'''

#CONSTANTES
AÑO_ACTUAL = 2023

#LIBRERÍAS
from datetime import datetime # librería para fecha

#===ENTRADAS===

nombre = input("¿Cuál es tu nombre? ")
apellido1 = input("¿Cuál es tu primer apellido? ")
apellido2 = input("¿Cuál es tu segundo apellido? ")

#Loop que hace que el usuario introduzca su año en dígitos y no letras
#También evita que el usuario introduzca más de 4 dígitos
while True:
    try:
        año_nac = int(input("¿En qué año naciste? "))   
    except ValueError:
        print("\nUnicamente escriba los cuatros números de su año de nacimiento")
        continue
    else:
        if año_nac > 9999:
            print("\n Su año solo puede contener 4 dígitos")
            continue
    break

#Loop que hace que el usuario introduzca su fecha solo en el formato solicitado (mm-dd)
while True:
    mes_dia = input("¿En qué mes y día naciste? (en el siguiente formato \"mm-dd\")")
    try:
        fecha = datetime.strptime(mes_dia, '%m-%d').strftime('%m-%d')
    except ValueError:
        print("Formato de fecha incorrecto")
        continue
    break

#Concatenación de nombre y conteo de vocales y letras
nombre_completo =[nombre, apellido1, apellido2]
nc_min= [x.lower() for x in nombre_completo]
nc_may= [x.upper() for x in nombre_completo]
VocalesNombre = len([char for char in ''.join(nombre_completo) if char in "aeiouAEIOUáéíóúÁÉÍÓÚ"])
LetrasNombre = len(''.join(nombre_completo))

#Separación de los dígitos de la fecha para manipular individualmente
lista_md = fecha.split("-")
mes, dia = lista_md
mes_int = int(mes)
dia_int = int(dia)

#Cáculo de la edad cumplida en ese año
edad = AÑO_ACTUAL - año_nac

#variables de dia y mes actual para calcular años cumplidos al día
dia_act = datetime.now().day
mes_act = datetime.now().month


#====SALIDAS====

print("\nEstos son los resultados \n")

print(f"Este es tu nombre completo en mayúsculas: ",  *nc_may)
print(f"Este es tu nombre completo en minúsculas: ",  *nc_min)
print(f"Esta es tu fecha de nacimiento \"{dia}-{mes}-{año_nac}\"")

#Condicional adicional para verificar la edad exacta al día actual
if mes_act == mes_int:                                  #validando durante el mes de su cumpleaños
    if dia_act < dia_int:
        edad_act = edad - 1                             #edad actual cuando no ha pasado su cumpleaños
        print(f"Esta es tu edad: {edad_act} ")
    else:
        if dia_int == dia_act:
            edad_act=edad
            print (f"¡Feliz Cumpleaños {edad_act}! ")  #edad actual el día de su cumpleaños
        else:
            edad_act=edad
            print(f"Esta es tu edad: {edad_act}")      #edad actual después del día de su cumpleaños
else:
    if mes_act < mes_int:                              #edad actual antes del mes de su cumpleaños
        edad_act = edad - 1
        print(f"Esta es tu edad: {edad_act}")
    else:                                              #edad acutal después del mes de su cumpleaños
        edad_act = edad
        print(f"Esta es tu edad: {edad_act}")

print(f"Tu nombre completo tiene {VocalesNombre} vocales")
print(f"Tu nombre completo tiene {LetrasNombre} letras")
print(f"¿Tu edad es un carácter de tipo número? {isinstance(edad_act, int)}")
print(f"¿Tu nombre completo es un caracter de tipo alfanumérico? {''.join(nombre_completo).isalnum()}") 
print(f"Tu edad en 10 años será {edad_act + 10}")
print(f"La media de tu edad actual y edad en 20 años es {(edad_act + edad_act + 20)/2}")

#====FIN====
   
