import openpyxl
from datetime import datetime
import os


def obtener_ruta_basededatos():
    # Obtén la ruta del directorio actual del módulo
    ruta_modulo = os.path.dirname(os.path.abspath(__file__))

    # Combina la ruta del directorio del módulo con el nombre de archivo
    ruta_completa = os.path.join(ruta_modulo, "BasedeDatos.xlsx")

    return ruta_completa


class Cliente:
    def __init__(self, usuario, nombre, apellido, fecha_nacimiento, correo, clave, ingreso):
        self.usuario = usuario
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.clave = clave
        self.ingreso = ingreso

def cargar_usuarios_desde_excel():
    ruta_completa = obtener_ruta_basededatos()
    usuarios = {}

    # Verificar si el archivo existe
    if not os.path.exists(ruta_completa):
        print("No hay usuarios registrados.")
        return usuarios

    # Abrir el archivo Excel
    wb = openpyxl.load_workbook(ruta_completa)
    ws = wb.active

    # Iterar sobre las filas en el archivo Excel
    for fila in ws.iter_rows(min_row=2, values_only=True):
        usuario = fila[0]
        nombre = fila[1]
        apellido = fila[2]
        fecha_nacimiento = fila[3]
        correo = fila[5]
        clave = fila[6]
        ingreso = fila[7]

        # Crear una instancia de la clase Cliente
        cliente = Cliente(usuario, nombre, apellido, fecha_nacimiento, correo, clave, ingreso)
        usuarios[usuario] = cliente

    return usuarios

def obtener_cliente_por_usuario(usuario, usuarios):
    return usuarios.get(usuario)

class Jovenes:
    @staticmethod
    def buscar_jovenes(usuarios, edad_limite):
        jovenes = []
        for usuario, cliente in usuarios.items():
            edad = calcular_edad(cliente.fecha_nacimiento)
            if edad < edad_limite:
                joven = {'Usuario': cliente.usuario, 'Nombre': cliente.nombre, 'Apellido': cliente.apellido, 'Edad': edad}
                jovenes.append(joven)
        return jovenes

class Adultos:
    @staticmethod
    def buscar_adultos(usuarios, edad_minima, edad_maxima):
        adultos = []
        for usuario, cliente in usuarios.items():
            edad = calcular_edad(cliente.fecha_nacimiento)
            if edad >= edad_minima and edad <= edad_maxima:
                adulto = {'Usuario': cliente.usuario, 'Nombre': cliente.nombre, 'Apellido': cliente.apellido, 'Edad': edad}
                adultos.append(adulto)
        return adultos

class Veteranos:
    @staticmethod
    def buscar_veteranos(usuarios, edad_limite):
        veteranos = []
        for usuario, cliente in usuarios.items():
            edad = calcular_edad(cliente.fecha_nacimiento)
            if edad > edad_limite:
                veterano = {'Usuario': cliente.usuario, 'Nombre': cliente.nombre, 'Apellido': cliente.apellido, 'Edad': edad}
                veteranos.append(veterano)
        return veteranos

def calcular_edad(fecha_nacimiento):
    nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    hoy = datetime.today()
    edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
    return edad

def mostrar_menu_cliente():
    print("Opciones:")
    print("1. Ver Usuario")
    print("2. Ver Jóvenes (menores de 25 años)")
    print("3. Ver Adultos (entre 26 y 50 años)")
    print("4. Ver Veteranos (mayores de 50 años)")
    print("5. Volver")

def main_cliente():
    while True:
        # Cargar usuarios desde el archivo Excel
        usuarios = cargar_usuarios_desde_excel()

        mostrar_menu_cliente()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Ver detalles de un usuario
            usuario_a_buscar = input("Ingrese su nombre de usuario: ")
            cliente_encontrado = obtener_cliente_por_usuario(usuario_a_buscar, usuarios)
            if cliente_encontrado:
                print(f"Detalles del usuario {usuario_a_buscar}:")
                print(f"  Nombre: {cliente_encontrado.nombre}")
                print(f"  Apellido: {cliente_encontrado.apellido}")
                print(f"  Nacimiento: {cliente_encontrado.fecha_nacimiento}")
                print(f"  Correo electrónico: {cliente_encontrado.correo}")
                print(f"  Ingreso: {cliente_encontrado.ingreso}")
            else:
                print(f"No se encontró el usuario {usuario_a_buscar}.")
        elif opcion == '2':
            # Ver jóvenes
            jovenes = Jovenes.buscar_jovenes(usuarios, 25)
            if jovenes:
                print("Usuarios Jóvenes:")
                for joven in jovenes:
                    print(f"  Usuario: {joven['Usuario']}, Nombre: {joven['Nombre']}, Apellido: {joven['Apellido']}, Edad: {joven['Edad']}")
            else:
                print("No hay jóvenes registrados.")
        elif opcion == '3':
            # Ver adultos
            adultos = Adultos.buscar_adultos(usuarios, 26, 50)
            if adultos:
                print("Usuarios Adultos:")
                for adulto in adultos:
                    print(f"  Usuario: {adulto['Usuario']}, Nombre: {adulto['Nombre']}, Apellido: {adulto['Apellido']}, Edad: {adulto['Edad']}")
            else:
                print("No hay adultos registrados.")
        elif opcion == '4':
            # Ver veteranos
            veteranos = Veteranos.buscar_veteranos(usuarios, 50)
            if veteranos:
                print("Usuarios Veteranos:")
                for veterano in veteranos:
                    print(f"  Usuario: {veterano['Usuario']}, Nombre: {veterano['Nombre']}, Apellido: {veterano['Apellido']}, Edad: {veterano['Edad']}")
            else:
                print("No hay veteranos registrados.")
        elif opcion == '5':
            # Volver al menú principal
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main_cliente()
