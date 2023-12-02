import re
import os
import openpyxl
import datetime


class Cliente:
    def __init__(self, usuario, datos):
        self.usuario = usuario
        self.datos = datos

    @classmethod
    def crear_desde_registro(cls, usuario, datos):
        return cls(usuario, datos)

usuarios = {}

def es_alfanumerico(clave):
    return bool(re.match("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+$", clave))

def es_correo_valido(correo):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", correo))

def es_fecha_valida(fecha):
    return bool(re.match(r"\d{2}/\d{2}/\d{4}", fecha))

def calcular_edad(fecha_nacimiento):
    nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    hoy = datetime.datetime.now()
    edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
    return edad

def guardar_en_excel(usuario, datos, ruta_guardado=None):
    if ruta_guardado is None:
        # Obtén la ruta del directorio actual
        ruta_guardado = os.path.dirname(os.path.abspath(__file__))

    # Combina la ruta del directorio actual con el nombre de archivo
    ruta_completa = os.path.join(ruta_guardado, "BasedeDatos.xlsx")

    # Si el archivo no existe, crea uno nuevo con encabezados
    if not os.path.exists(ruta_completa):
        wb = openpyxl.Workbook()
        ws = wb.active
        encabezados = ["USUARIO", "NOMBRE", "APELLIDO", "NACIMIENTO", "EDAD", "MAIL", "CLAVE", "INGRESO"]
        ws.append(encabezados)
        wb.save(ruta_completa)

    # Abre el archivo existente
    wb = openpyxl.load_workbook(ruta_completa)
    ws = wb.active

    # Extrae los datos del usuario
    usuario_nuevo = [usuario, datos['datos'][0], datos['datos'][1], datos['datos'][2], datos['datos'][3], datos['datos'][4], datos['datos'][5], datos['fecha_registro']]

    # Agrega una nueva fila con los datos del usuario a partir de la segunda fila
    ws.append(usuario_nuevo)

    # Guarda el archivo
    wb.save(ruta_completa)

def registrar_usuario():
    nuevo_usuario = input("Nuevo usuario: ")

    if nuevo_usuario in usuarios:
        print("El usuario ya existe. Por favor, elige otro nombre de usuario.")
        nuevo_usuario = input("Nuevo usuario: ")

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    while True:
        fecha_nacimiento = input("Ingrese su fecha de nacimiento dd/mm/aaaa: ")
        if es_fecha_valida(fecha_nacimiento):
            break
        else:
            print("El formato de fecha es incorrecto. Debe ser dd/mm/aaaa. Inténtalo de nuevo.")

    while True:
        edad = input("Ingrese su edad: ")
        if edad.isdigit():
            break
        else:
            print("La edad debe ser un número entero. Inténtalo de nuevo.")

    while True:
        nuevo_correo = input("Ingrese su correo electrónico: ")
        if es_correo_valido(nuevo_correo):
            break
        else:
            print("El correo electrónico debe tener un formato válido. Inténtalo de nuevo.")

    while True:
        nueva_clave = input("Nueva clave: ")
        if es_alfanumerico(nueva_clave):
            break
        else:
            print("La contraseña debe ser alfanumérica (contener letras y números). Inténtalo de nuevo.")

    # Obtener la fecha actual
    fecha_registro = datetime.datetime.now().strftime("%d/%m/%Y")

    datos_usuario = {'datos': (nombre, apellido, fecha_nacimiento, edad, nuevo_correo, nueva_clave), 'fecha_registro': fecha_registro}
    usuarios[nuevo_usuario] = datos_usuario

    # Crear instancia de Cliente y guardar en archivo Excel
    cliente_nuevo = Cliente.crear_desde_registro(nuevo_usuario, datos_usuario)
    guardar_en_excel(nuevo_usuario, datos_usuario)

    print(f"Usuario {cliente_nuevo.usuario} registrado con éxito en la fecha {fecha_registro}.")

if __name__ == "__main__":
    registrar_usuario()
