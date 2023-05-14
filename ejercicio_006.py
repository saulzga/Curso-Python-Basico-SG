'''
Saúl Gómez García
Ejercicio #6
Curso Básico de Python
'''

Pi = 3.1416

radio = int(input ("introduzca el valor del radio en metros: "))

def AreaCirculo (x):
    return Pi*x*x

def VolumenCirculo (r):
    return 4/3*AreaCirculo(r)*r

print(f'El valor del área es: {AreaCirculo(radio)} metros cuadrados')
print(f'El valor del volumen es: {VolumenCirculo(radio)} metros cúbicos')