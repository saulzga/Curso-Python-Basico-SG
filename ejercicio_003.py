'''
Saúl Gómez García
Ejercicio #3
Curso de Python Básico
'''

print("\n====CREE UNA NUEVA CONTRASEÑA===\n")
while True:
    PSW1 = input("Por favor introduzca su nueva contraseña: ")
    PSW2 = input("Repita su nueva contraseña: ")
    if PSW1==PSW2:
        print("\n¡Contraseña creada exitosamente!")
        break
    else:
        print("\n¡Las contraseñas no coinciden, intente nuevamente!\n")
        continue

print("\n====UTILICE SU CONTRASEÑA====\n")
while True:
    password = input("Por favor introduzca su contraseña: ")   
    if PSW1== password:
        print("\n¡CONTRASEÑA CORRECTA!\n")
        break
    else:
        print("\n¡CONTRASEÑA INCORRECTA! \nIntente de nuevo\n")
        continue
    