import os
import getpass

# import colorama
# from colorama import Fore, Back, Style
import pickle
import datetime
import io
import time


class Usuario:
    def __init__(self):
        self.codUsuario = 0
        self.nombreUsuario = ""
        self.claveUsuario = ""
        self.tipoUsuario = ""


class Locales:
    def __init__(self):
        self.codLocal = 0
        self.nombreLocal = ""
        self.UbicacionLocal = ""
        self.rubroLocal = ""
        codUsuario = 0
        estado = "A"


class Promociones:
    def __init__(self):
        self.codPromo = 0
        self.textoPromo = ""
        self.fechaDesdePromo = ""
        self.HastaPromo = ""
        self.diasSemana = [0] * 6
        self.estado = ""
        self.codLocal = 0


class Novedades:
    def __init__(self):
        self.codNovedad = 0
        self.textoNovedad = ""
        self.fechaDesdeNovedad = ""
        self.fechaHastaNovedad = ""
        self.tipoUsuario = ""
        self.estado = "A"


class Uso_Promociones:
    def __init__(self) -> None:
        self.codCliente = 0
        self.codPromo = 0
        self.fechaUsoPromo = ""


# colorama.init()


def abrirarchivos(nombre):
    if os.path.exists(nombre):
        archivo_logico = open(nombre, "r+b")
    else:
        archivo_logico = open(nombre, "w+b")
    return archivo_logico


def cerrar_archivos():
    print("Cerrando programa..")
    ARCHIVO_LOGICO_USUARIOS.close()
    ARCHIVO_LOGICO_LOCALES.close()
    ARCHIVO_LOGICO_PROMOCIONES.close()
    ARCHIVO_LOGICO_USOPROMOCIONES.close()
    ARCHIVO_LOGICO_NOVEDADES.close()


# Archivos fisicos
ARCHIVO_FISICO_USUARIOS = os.getcwd() + "/usuarios.dat"
ARCHIVO_FISICO_LOCALES = os.getcwd() + "/locales.dat"
ARCHIVO_FISICO_PROMOCIONES = os.getcwd() + "/promociones.dat"
ARCHIVO_FISICO_USOPROMOCIONES = os.getcwd() + "/usopromociones.dat"
ARCHIVO_FISICO_NOVEDADES = os.getcwd() + "/novedades.dat"

# Archivos logicos

ARCHIVO_LOGICO_USUARIOS = abrirarchivos(ARCHIVO_FISICO_USUARIOS)
ARCHIVO_LOGICO_LOCALES = abrirarchivos(ARCHIVO_FISICO_LOCALES)
ARCHIVO_LOGICO_PROMOCIONES = abrirarchivos(ARCHIVO_FISICO_PROMOCIONES)
ARCHIVO_LOGICO_USOPROMOCIONES = abrirarchivos(ARCHIVO_FISICO_USOPROMOCIONES)
ARCHIVO_LOGICO_NOVEDADES = abrirarchivos(ARCHIVO_FISICO_NOVEDADES)


def lj_usuarios(x):
    x.codUsuario = str(x.codUsuario).ljust(8)
    x.nombreUsuario = str(x.nombreUsuario).ljust(100)
    x.claveUsuario = str(x.claveUsuario).ljust(8)
    x.tipoUsuario = str(x.tipoUsuario).ljust(20)


def lj_locales(x):
    x.codLocal = str(x.codLocal).ljust(8)
    x.nombreLocal = str(x.nombreLocal).ljust(50)
    x.ubicacionLocal = str(x.rubroLocal).ljust(50)
    x.rubroLocal = str(x.rubroLocal).ljust(50)
    x.codUsuario = str(x.codUsuario).ljust(80)
    x.estado = str(x.estado).ljust(2)


def lj_promociones(x):
    x.codPromo = str(x.codPromo).ljust(8)
    x.textoPromo = str(x.textoPromo).ljust(200)
    x.fechaDesdePromo = str(x.fechaDesdePromo).ljust()
    x.HastaPromo = str(x.HastaPromo).ljust()
    x.diasSemana = [0] * 6
    x.estado = str(x.estado).ljust(10)
    x.codLocal = str(x.codLocal).ljust(8)


def lj_uso_promociones(x):
    x.codCliente = str(x.codCliente).ljust()
    x.codPromo = str(x.codPromo).ljust()
    x.fechaUsoPromo = str(x.fechaUsoPromo).ljust()


def ljnovedades(x):
    x.codNovedad = str(x.codNovedad).ljust()
    x.textoNovedad = str(x.textoNovedad).ljust()
    x.fechaDesdeNovedad = str(x.fechaDesdeNovedad).ljust()
    x.fechaHastaNovedad = str(x.fechaHastaNovedad).ljust()
    x.tipoUsuario = str(x.tipoUsuario).ljust()
    x.estado = str(x.estado).ljust()


def date():
    flag = True
    while flag:
        try:
            fecha = input("Ingresa una fecha en el formato DD/MM/AAAA: ")
            datetime.datetime.strptime(fecha, "%d/%m/%Y")
            print("Fecha valida")
            flag = False
        except ValueError:
            print("Fecha invalida")
    dia, mes, anio = fecha.split("/")
    return fecha


# Define constant
cont_indumentaria = 0
cont_perfumeria = 0
cont_comida = 0

""" STATUS """
# print_advertencia = lambda txt: print(Fore.RED + txt, Fore.RESET)
# print_completado = lambda txt: print(Fore.GREEN + txt, Fore.RESET)
# print_aviso = lambda txt: print(Fore.YELLOW + txt, Fore.RESET)


def savedata(data, ARCHIVO_LOGICO: io.BufferedRandom, ARCHIVO_FISICO):
    """(DATA - ARCHIVO_FISICO - ARCHIVO_LOGICO)"""
    t = os.path.getsize(ARCHIVO_FISICO)

    ARCHIVO_LOGICO.seek(t)

    pickle.dump(data, ARCHIVO_LOGICO)

    ARCHIVO_LOGICO.flush()


def verificar_admin():
    tamaño = os.path.getsize(ARCHIVO_FISICO_USUARIOS)
    if tamaño == 0:
        administrador = Usuario()
        administrador.codUsuario = 1
        administrador.nombreUsuario = "admin@shopping.com"
        administrador.claveUsuario = 12345
        administrador.tipoUsuario = "administrador"
        lj_usuarios(administrador)
        savedata(administrador, ARCHIVO_LOGICO_USUARIOS, ARCHIVO_FISICO_USUARIOS)


def busquedasecuencial(ARCHIVO_LOGICO: io.BufferedRandom, ARCHIVO_FISICO, callback):
    tamañoarchivo = os.path.getsize(ARCHIVO_FISICO)
    ARCHIVO_LOGICO.seek(0)
    encontrado = False

    while ARCHIVO_LOGICO.tell() < tamañoarchivo and encontrado == False:
        posicion = ARCHIVO_LOGICO.tell()
        regtemporal = pickle.load(ARCHIVO_LOGICO)
        encontrado = callback(regtemporal)

    return encontrado


def ordenarempleado(ARCHIVO_LOGICO: io.BufferedRandom, ARCHIVO_FISICO):
    ARCHIVO_LOGICO.seek(0)
    aux = pickle.load(ARCHIVO_LOGICO)
    Tamregistro = ARCHIVO_LOGICO.tell()
    tamarchivo = os.path.getsize(ARCHIVO_FISICO)
    cantreg = int(tamarchivo / Tamregistro)
    for i in range(0, cantreg - 1):
        for j in range(i + 1, cantreg):
            ARCHIVO_LOGICO.seek(i * cantreg, 0)
            auxi = pickle.load(ARCHIVO_LOGICO)
            ARCHIVO_LOGICO.seek(j * cantreg, 0)
            auxj = pickle.load(ARCHIVO_LOGICO)
            if auxi.legajo > auxj.legajo:
                ARCHIVO_LOGICO.seek(i * Tamregistro, 0)
                pickle.dump(auxi, ARCHIVO_LOGICO)
                ARCHIVO_LOGICO.seek(j * Tamregistro, 0)
                pickle.dump(auxj, ARCHIVO_LOGICO)


clear = lambda x: os.system(x)


# funcion de ingreso
def yes_no():
    opcion = input("ingrese una opcion (y/n): ").upper()
    while opcion != "Y" and opcion != "N":
        opcion = input("error, ingrese una opcion valida (y/n): ").upper()
    return opcion


def validar_tipo(opc, tipo, desde, hasta):
    try:
        opc = tipo(opc)
        while not (opc >= desde and opc <= hasta):
            print(f"opcion incorrecta, ingrese {desde} - {hasta}")
            opc = input("ingrese nuevamente: ")
            opc = tipo(opc)
    except:
        print("error debe ingresar un numero: ")
        opc = input("intente nuevamente: ")
        return validar_tipo(opc, tipo, desde, hasta)
    return opc


def validar_clave(val):
    i = 0
    aux = False
    while aux != True and i < 3:
        opc = input("ingrese la contraseña: ")
        if val[1] == opc:
            aux = True
        else:
            print(f"la contraseña es incorrecta")
        i += 1
    return aux


def inputclass(opc: str, length: int):
    while not (len(opc) < length):
        opc = input(f"Error, Ingrese nuevamente (hasta {length} caracteres): ")
    return opc.ljust(length)


def validar_dominio(email):
    data = ["", ""]
    tipos = ["@shopping.com"]
    dominio = " "
    longitud = len(email)
    for i in range(0, longitud):
        if email[i] == "@":
            dominio = "@"
        elif dominio[0] == "@":
            dominio += email[i]
    if tipos[0] == dominio:
        data = ["True", "Dominio existente"]
    elif dominio == " ":
        data = ["False", "Ingrese un email valido"]
    else:
        data = ["False", "Dominio inexistente, Ingrese un email valido"]
    return data


def validacion_rubro(rubro, resultado):
    rubro = str(rubro)
    rubros = ["indumentaria", "perfumeria", "comida"]
    resultado = resultado
    index = 0
    bandera = False
    while not (bandera) and index < 3:
        if rubro.lower() == rubros[index]:
            bandera = True
            resultado = rubros[index]
        else:
            index += 1
    if bandera:
        return resultado
    else:
        return validacion_rubro(input("Ingrese un rubro correcto: "), resultado)


def autoincremental():
    t = os.path.getsize(ARCHIVO_FISICO_USUARIOS)
    ARCHIVO_LOGICO_USUARIOS.seek(-t, 2)
    regtemporal = pickle.load(ARCHIVO_LOGICO_USUARIOS)

    return int(regtemporal.codUsuario) + 1


# prints
def construccion():
    print("en construcción...")
    clear("pause")


def admin_1():
    print(
        """a) Crear locales 
            \nb) Modificar local 
            \nc) Eliminar local 
            \nd) Mapa de locales   
            \ne) Volver"""
    )
    clear("pause")


def admin_4():
    print(
        """Gestion de novedades:
          \na. Crear novedades
          \nb. Modificar novedad
          \nc. Eliminar novedad
          \nd. Ver reporte de novedades
          \ne. Volver"""
    )
    clear("pause")


def owner_menu():
    print(
        """Menú principal:
          \n1. Gestión de descuentos
          \n2. Aceptar / Rechazar pedido de descuento
          \n3.  Reporte de uso de descuentos 
          \n0. Salir"""
    )
    clear("pause")


def owner_1():
    print(
        """a)  Crear descuento para mi local 
          \nb)  Modificar descuento de mi local 
          \nc) Eliminar descuento de mi local 
          \nd)  Volver"""
    )
    clear("pause")


def mostrar_menu():
    print(
        """Menú principal:
        \n1. Gestión de locales
        \n2. Crear cuentas de dueños de locales
        \n3. Aprobar / Denegar solicitud de descuento
        \n4. Gestión de novedades
        \n5. Reporte de utilización de descuentos
        \n0. Salir"""
    )
    clear("pause")


def menu_gestion_locales():
    print(
        """menú de gestión de locales:
        \na. Crear locales
        \nb. Modificar local
        \nc. Eliminar local
        \nd. Volver"""
    )
    clear("pause")


def gestion_novedades():
    print(
        """Gestion de novedades:
        \na. Crear novedades
        \nb. Modificar novedad
        \nc. Eliminar novedad
        \nd. Ver reporte de novedades 
        \ne. Volver"""
    )
    clear("pause")


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def mapa_locales():
    clear("cls")
    ordenado = burbuja_indices(datosLocal, codLocal)
    techo = "+---"
    techo = techo * 5 + "+"
    print(techo)
    aux = 0
    for t in range(0, 10):
        index = 0
        a = ""
        while index < 5:
            index += 1
            a += "|" + str(ordenado[aux][1]) + "|"
            aux += 1
        print(a)
        print(techo)
    clear("pause")
    clear("cls")


def gestion_locales():
    clear("cls")
    mostrar_locales_desc()
    a = """
        \nHa ingresado en el menu de Gestion de Locales
        \na) Crear locales 
        \nb) Modificar local 
        \nc) Eliminar local 
        \nd) Mapa de locales   
        \ne) Volver"""
    print(a)
    opcion = validar_tipo(input("Ingrese una opcion  "), str, "a", "e")
    while opcion != "e":
        match opcion:
            case "a":
                crear_locales()
            case "b":
                mod_locales()
            case "c":
                elim_locales()
            case "d":
                mapa_locales()
            case "e":
                print("Volviste al menu principal")
        mostrar_locales_desc()
        print(a)
        opcion = validar_tipo(input("Ingrese una opcion  "), str, "a", "e")
    clear("cls")


def admin_menu():
    clear("cls")
    print(
        """Menú principal:
          \n1. Gestión de locales
          \n2. Crear cuentas de dueños de locales
          \n3. Aprobar / Denegar solicitud de descuento
          \n4. Gestión de novedades
          \n5. Reporte de utilización de descuentos
          \n0. Salir"""
    )
    opcion = validar_tipo(input("Ingrese una opcion "), int, 0, 5)
    match opcion:
        case 1:
            gestion_locales()
        case 2:
            crear_cuenta()
        case 3:
            solic_descuento()
        case 4:
            gestion_novedades()
        case 5:
            """reporte_descuentos()"""


def cliente_menu():
    os.system("cls")
    a = "Menú principal:\n1. Buscar descuentos en locales\n2. Solicitar descuento\n3. Ver novedades\n0. Salir"
    print(a)
    opc = validar_tipo(input("Ingrese una opción: "), int, 0, 4)
    while opc != 0:
        match (opc):
            case (1):
                buscar_descuentos_locales()
            case (2):
                solicitar_descuento()
            case (3):
                print("Está en chapin")
            case (0):
                print("Ha salido")
        print(a)
        opc = validar_tipo(input("Ingrese una opción: "), int, 0, 4)
    clear("pause")


def registrarse_cliente():
    clear("cls")
    cliente = Usuario()
    encontrado = True

    while encontrado:
        email = inputclass(input("Ingrese email [0-Cancelar]:  "), 100)
        if email.strip() == "0":
            return

        password = inputclass(
            getpass.getpass("Ingrese su contraseña [0-Cancelar]: "), 8
        )

        if password.strip() == "0":
            return

        def searchUser(regtemporal):
            if (
                str(regtemporal.nombreUsuario).strip() == email.strip()
                and str(regtemporal.claveUsuario).strip() == password.strip()
            ):
                return True
            else:
                return False

        encontrado = busquedasecuencial(
            ARCHIVO_LOGICO_USUARIOS, ARCHIVO_FISICO_USUARIOS, searchUser
        )

    cliente.nombreUsuario = email
    cliente.claveUsuario = password
    cliente.codUsuario = autoincremental()
    cliente.tipoUsuario = "cliente"

    savedata(cliente, ARCHIVO_LOGICO_USUARIOS, ARCHIVO_FISICO_USUARIOS)
    print("Guardado existoso")

    os.system("pause")
    os.system("cls")

    cliente_menu()


def usuario_registrado():
    clear("cls")

    email = inputclass(input("Ingrese email: "), 100)
    password = inputclass(getpass.getpass("Ingrese su contraseña: "), 8)

    def login(regtemporal):
        if (
            str(regtemporal.nombreUsuario).strip() == email.strip()
            and str(regtemporal.claveUsuario).strip() == password.strip()
        ):
            return regtemporal.tipoUsuario
        else:
            return False

    tipo = busquedasecuencial(ARCHIVO_LOGICO_USUARIOS, ARCHIVO_FISICO_USUARIOS, login)

    # Hacer menu para la proxima
    match (tipo):
        case ("administrador"):
            admin_menu()
        case ("duenocliente"):
            owner_menu()
        case ("cliente"):
            cliente_menu()
        case (_):
            return "Error"


def menuprincipal():
    os.system("cls")
    # Verifica si el adminsitrador fue creado al iniciar el programa por primera vez
    menu = "Menú principal\n_____________________________\n1. Ingresar con usuario registrado\n2. Registrarse como cliente\n3. Salir"
    verificar_admin()

    print(menu)
    opc = validar_tipo(input("Ingrese una opción: "), int, 1, 3)
    while opc != 3:
        match (opc):
            case (1):
                usuario_registrado()
            case (2):
                registrarse_cliente()
            case (3):
                cerrar_archivos()
            case (_):
                return "Error inesperado"
        os.system("cls")
        print(menu)
        opc = validar_tipo(input("Ingrese una opción: "), int, 1, 3)
        
    cerrar_archivos()

    os.system("pause")


menuprincipal()
