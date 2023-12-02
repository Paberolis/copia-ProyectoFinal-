from registro_usuario import registrar_usuario
from ver_usuarios import ver_usuarios
from restablecer_clave import restablecer_clave
from iniciar_sesion import iniciar_sesion
import cliente
from datetime import datetime

def mostrar_menu_principal():
    print("Bienvenido al sistema de inicio de sesión.")

    while True:
        print("Opciones:")
        print("1. Iniciar sesión")
        print("2. Registrar nuevo usuario")
        print("3. Ver Usuarios")
        print("4. Restablecer Clave")
        print("5. Informacion de Clientes")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            if iniciar_sesion():
                print("Inicio de sesión exitoso.")
                break
            else:
                print("Inicio de sesión fallido. Inténtelo nuevamente.")
        elif opcion == '2':
            registrar_usuario()
        elif opcion == '3':
            ver_usuarios()
        elif opcion == '4':
            restablecer_clave()
        elif opcion == '5':
            cliente.main_cliente()
        elif opcion == '6':
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == '__main__':
    mostrar_menu_principal()
