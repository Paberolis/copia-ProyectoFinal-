import openpyxl
from datetime import datetime
import os

class Cliente:
    def __init__(self, usuario, nombre, apellido, fecha_nacimiento, correo, clave, ingreso):
        self.usuario = usuario
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.clave = clave
        self.ingreso = ingreso

def cargar_usuarios_desde_excel(ruta_archivo):
    usuarios = {}

    # Verificar si el archivo existe
    if not os.path.exists(ruta_archivo):
        print("No hay usuarios registrados.")
        return usuarios

    # Abrir el archivo Excel
    wb = openpyxl.load_workbook(ruta_archivo)
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

def obtener_ruta_basededatos():
    # Obtén la ruta del directorio actual del módulo
    ruta_modulo = os.path.dirname(os.path.abspath(__file__))

    # Combina la ruta del directorio del módulo con el nombre de archivo
    ruta_completa = os.path.join(ruta_modulo, "BasedeDatos.xlsx")

    return ruta_completa

def iniciar_sesion(intentos_maximos=3):
    # Obtener la ruta del archivo BasedeDatos.xlsx
    ruta_completa = obtener_ruta_basededatos()

    usuarios = cargar_usuarios_desde_excel(ruta_completa)
    intentos = 0

    while intentos < intentos_maximos:
        usuario = input("Usuario: ")
        clave = input("Clave: ")

        # Verificar si el usuario existe y la contraseña es válida
        cliente = usuarios.get(usuario)
        if cliente and cliente.clave == clave:
            print(f"Inicio de sesión exitoso. ¡Bienvenido/a, {usuario}!")
            return True
        else:
            intentos += 1
            print(f"Credenciales incorrectas. Intento {intentos}/{intentos_maximos}. Por favor, inténtelo de nuevo.")

    print("Se ha alcanzado el número máximo de intentos. Por favor, inténtelo más tarde.")
    return False

if __name__ == "__main__":
    iniciar_sesion()
