'''
Saúl Gómez García
Ejercicio #5
Curso Básico de Python
'''
frutas = {
    "Platano": 1.75, 
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
    }

FrutaBuscada = input ("introduzca el nombre de la fruta que quiere: ")
if FrutaBuscada in frutas:
    Kilos = int(input ("¿Cuántos Kilos quiere? "))
    Total= Kilos*frutas[FrutaBuscada]
    print(f'El total es: {Total}')
else:
    print("Fruta no disponible")