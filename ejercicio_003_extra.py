'''
Saúl Gómez García
Ejercicio #3 EXTRA
Curso de Python Básico
'''
from getpass import getpass

print("\n====CREE UNA NUEVA CONTRASEÑA===\n*los carácteres son invisibles mientras escribe*\n")
while True:
    PSW1 = getpass(prompt="Por favor introduzca su nueva contraseña:")
    PSW2 = getpass(prompt="Repita su nueva contraseña:")
    if PSW1==PSW2:
        print("\n¡Contraseña creada exitosamente!")
        break
    else:
        print("\n¡Las contraseñas no coinciden, intente nuevamente!\n")
        continue

print("\n====UTILICE SU CONTRASEÑA====\n*los carácteres son invisibles mientras escribe*\n")
intentos=0
while True:
    password = getpass(prompt="Por favor introduzca su contraseña:")   
    if PSW1== password:
        print("\n¡CONTRASEÑA CORRECTA!\n")
        break
    else:
        print("\n¡CONTRASEÑA INCORRECTA! \nIntente de nuevo\n")
        intentos += 1
        if intentos > 5:
            print("\n¡5 INTENTOS ERRONEOS, CUENTA BLOQUEADA!")
            break
        continue
    