import getpass
import random

import os
import io
import pickle

import datetime

# import colorama

# from colorama import Fore, Back, Style


# colorama.init()


from faker import Faker

from rich import print

# print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())


class Usuario:
    def __init__(self):
        self.codUsuario = 0
        self.nombreUsuario = ""
        self.claveUsuario = ""
        self.tipoUsuario = ""
        """ DuenoDeLocal administrador cliente """


class Locales:
    def __init__(self):
        self.codLocal = 0
        self.nombreLocal = ""
        self.UbicacionLocal = ""
        self.rubroLocal = ""
        self.codUsuario = 0
        self.estado = "A"


class Promociones:
    def __init__(self):
        self.codPromo = 0
        self.textoPromo = ""
        self.fechaDesdePromo = ""
        self.HastaPromo = ""
        self.diasSemana = [0] * 6
        self.estado = ""
        # estado (‘pendiente’, ‘aprobada’, ‘rechazada’) string(10)
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
    x.codUsuario = str(x.codUsuario).ljust(40)
    x.estado = str(x.estado).ljust(2)


def lj_promociones(x):
    x.codPromo = str(x.codPromo).ljust(8)
    x.textoPromo = str(x.textoPromo).ljust(200)
    x.fechaDesdePromo = str(x.fechaDesdePromo).ljust(10)
    x.HastaPromo = str(x.HastaPromo).ljust(10)
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


# print_advertencia = lambda txt: print(Fore.RED + txt, Fore.RESET)
# print_completado = lambda txt: print(Fore.GREEN + txt, Fore.RESET)
# print_aviso = lambda txt: print(Fore.YELLOW + txt, Fore.RESET)


def savedata(data, ARCHIVO_LOGICO: io.BufferedRandom, ARCHIVO_FISICO: str, formatter):
    """(DATA - ARCHIVO_FISICO - ARCHIVO_LOGICO)"""
    try:
        formatter(data)

        t = os.path.getsize(ARCHIVO_FISICO)

        ARCHIVO_LOGICO.seek(t)

        pickle.dump(data, ARCHIVO_LOGICO)

        ARCHIVO_LOGICO.flush()

    except:
        print("Error inesperado")


def updatedata(data, ARCHIVO_LOGICO: io.BufferedRandom, PosPuntero: str, formatter):
    try:
        formatter(data)

        ARCHIVO_LOGICO.seek(PosPuntero)

        pickle.dump(data, ARCHIVO_LOGICO)

        ARCHIVO_LOGICO.flush()

    except:
        print("Error inesperado")


def verificar_admin():
    tamaño = os.path.getsize(ARCHIVO_FISICO_USUARIOS)
    if tamaño == 0:
        administrador = Usuario()

        administrador.codUsuario = 1
        administrador.nombreUsuario = "admin@shopping.com"
        administrador.claveUsuario = 12345
        administrador.tipoUsuario = "administrador"

        savedata(
            administrador, ARCHIVO_LOGICO_USUARIOS, ARCHIVO_FISICO_USUARIOS, lj_usuarios
        )


def busquedasecuencial(
    ARCHIVO_LOGICO: io.BufferedRandom, ARCHIVO_FISICO: str, callback
) -> bool:
    tamañoarchivo = os.path.getsize(ARCHIVO_FISICO)
    ARCHIVO_LOGICO.seek(0)
    encontrado = False

    while ARCHIVO_LOGICO.tell() < tamañoarchivo and encontrado == False:
        posicion = ARCHIVO_LOGICO.tell()
        regtemporal = pickle.load(ARCHIVO_LOGICO)
        encontrado = callback(regtemporal, posicion)

    return encontrado


def ordenarempleado(ARCHIVO_LOGICO: io.BufferedRandom, ARCHIVO_FISICO: str):
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


def busquedadico(data, ARCHIVO_LOGICO: io.BufferedRandom, ARCHIVO_FISICO: str):
    """Data:valor a entcontrar , ARCHIVO_LOGICO , ARCHIVO_FISICO"""

    data = str(data).split()

    ARCHIVO_LOGICO.seek(0, 0)

    aux = pickle.load(ARCHIVO_LOGICO_LOCALES)

    tamregi = ARCHIVO_LOGICO.tell()

    cantreg = int(os.path.getsize(ARCHIVO_FISICO) / tamregi)

    desde = 0

    hasta = cantreg - 1

    medio = (desde + hasta) // 2

    ARCHIVO_LOGICO.seek(medio * tamregi, 0)

    retemp = pickle.load(ARCHIVO_LOGICO)
    while str(retemp.nombreLocal).split() != data and desde < hasta:
        if data < str(retemp.nombreLocal).split():
            hasta = medio - 1
        else:
            desde = medio + 1
        medio = (desde + hasta) // 2

    if str(retemp.nombreLocal).split() == data:
        return True
    else:
        return False


clear = lambda x: os.system(x)


def locales():
    def randomm():
        numero_aleatorio = random.randint(1, 40)
        if numero_aleatorio < 13:
            return "indumentaria"
        elif numero_aleatorio > 13 and numero_aleatorio < 26:
            return "comida"
        else:
            return "perfumeria"

    fake = Faker()
    index = 0
    for i in range(0, 20):
        NuevoLocal = Locales()

        NuevoLocal.codLocal = inputclass(str(index), 8)
        NuevoLocal.nombreLocal = inputclass(fake.name(), 50)
        NuevoLocal.UbicacionLocal = inputclass(fake.address(), 50)
        NuevoLocal.rubroLocal = inputclass(randomm(), 50)
        NuevoLocal.codUsuario = inputclass(str(random.randint(5, 8)), 40)
        NuevoLocal.estado = inputclass("A", 2)

        print(
            f"\n codLocal:{NuevoLocal.codLocal},\n nombre:{NuevoLocal.nombreLocal},\n ubicacion: {NuevoLocal.UbicacionLocal},\n rubro: {NuevoLocal.rubroLocal}"
        )
        print(NuevoLocal.codUsuario)
        index += 1
        savedata(NuevoLocal, ARCHIVO_LOGICO_LOCALES, ARCHIVO_FISICO_LOCALES, lj_locales)


# funcion de ingreso
def yes_no() -> str:
    opcion = input("ingrese una opcion (y/n): ").upper()
    print("")
    while opcion != "Y" and opcion != "N":
        opcion = input("error, ingrese una opcion valida (y/n): ").upper()
        print("")
    return opcion


def validar_tipo(opc, tipo, desde: int, hasta: int):
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


def validacion_rubro(rubro: str):
    rubro = str(rubro)
    while (
        rubro.lower() != "perfumeria"
        and rubro.lower() != "comida"
        and rubro.lower() != "indumentaria"
    ):
        rubro = input("Ingrese un rubro correcto [indumentaria,comida,perfumeria]: ")
    return rubro


def autoincremental(ARCHIVO_LOGICO: io.BufferedRandom, ARCHIVO_FISICO, callback):
    t = os.path.getsize(ARCHIVO_FISICO)
    ARCHIVO_LOGICO.seek(0)
    regtemporal = pickle.load(ARCHIVO_LOGICO)
    uno = ARCHIVO_LOGICO.tell()

    ARCHIVO_LOGICO.seek(-uno, 2)
    regtemporal = pickle.load(ARCHIVO_LOGICO)
    print(regtemporal.codUsuario)

    return callback(regtemporal)


# --------------------------------------- Construccion
def construccion():
    clear("cls")
    print_aviso("en construcción...")
    print("")
    clear("pause")


def mostrar_menu():
    print(
        """Menú principal:
          \n1. Gestión de descuentos
            a) Crear descuento para mi local
            b) Modificar descuento de mi local
            c) Eliminar descuento de mi local
            d) Volver
          \n2. Aceptar / Rechazar pedido de descuento
          \n3. Reporte de uso de descuentos 
          \n0. Salir"""
    )

    clear("pause")


# ---------------------------------------- Funciones del Administrador -------------------------------- #


def admin_menu():
    os.system("cls")

    auxp = "Menú principal:\n1. Gestión de locales\n2. Crear cuentas de dueños de locales\n3. Aprobar / Denegar solicitud de descuento\n4. Gestión de novedades\n5. Reporte de utilización de descuentos\n0. Salir"

    print(auxp)

    opcion = validar_tipo(input("Ingrese una opcion "), int, 0, 5)
    match opcion:
        case 1:
            gestion_locales()
        case 2:
            crear_cuenta_dueno()
        case 3:
            aprobar_denegar_descuento()
        case 4:
            gestion_novedades()
        case 5:
            """reporte_descuentos()"""


def gestion_locales():
    clear("cls")
    a = """\nHa ingresado en el menu de Gestion de Locales\na) Crear locales \nb) Modificar local \nc) Eliminar local \nd) Mapa de locales   \ne) Volver"""

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
        print(a)

        opcion = validar_tipo(input("Ingrese una opcion  "), str, "a", "e")
    clear("cls")


def crear_locales():
    NuevoLocal = Locales()
    local = "-1"
    encontrado = True

    def autoincrementarlocal(regtemp):
        return int(regtemp.codLocal) + 1

    def searchUserDueñoLocal(regtemporal, p):
        if (
            str(codduenolocal).split() == str(regtemporal.codUsuario).split()
            and str(regtemporal.tipoUsuario).split() == "duenolocal"
        ):
            return regtemporal.codUsuario
        else:
            return False

    while local != "0":
        local = inputclass(input("Ingrese un nombre de local [0 para salir]: "), 50)
        while not (busquedadico(local, ARCHIVO_LOGICO_LOCALES, ARCHIVO_FISICO_LOCALES)):
            local = inputclass(input("Ingrese un nombre de local [0 para salir]: "), 50)

        ubicacion = inputclass()
        rubro = validacion_rubro(input("Ingrese el rubro del local: "))

        codduenolocal = int(input("Ingrese un código de un dueño de local: "))
        while not (
            busquedasecuencial(
                codduenolocal,
                ARCHIVO_LOGICO_USUARIOS,
                ARCHIVO_FISICO_USUARIOS,
                searchUserDueñoLocal,
            )
        ):
            codduenolocal = int(input("Ingrese un código de un dueño de local: "))

        NuevoLocal.codLocal = autoincremental(
            ARCHIVO_LOGICO_LOCALES, ARCHIVO_FISICO_LOCALES, autoincrementarlocal
        )
        NuevoLocal.nombreLocal = local
        NuevoLocal.UbicacionLocal = ubicacion
        NuevoLocal.rubroLocal = rubro
        NuevoLocal.codUsuario = codduenolocal


def pantalla_mod_locales(regtemp: Locales):
    def pantalla_local():
        print(
            f"\nNombre: {regtemp.nombreLocal} ",
            f"\nUbicacion: {regtemp.UbicacionLocal}",
            f"\nRubro: {regtemp.rubroLocal}",
        )

    clear("cls")
    opcScreen = "Y"

    pantalla_local()

    opc = input(
        "\n1-Nombre\n2-Ubicacion\n3-Rubro\n0-Salir\nIngrese lo que desea modificar: "
    )
    while opcScreen == "Y":
        match (opc):
            case ("1"):
                nombre = inputclass(input("Ingrese el nuevo nombre del local: "), 50)
                regtemp.nombreLocal = nombre
                print("Desea modificar otro campo del local?")
                opcScreen = yes_no()
            case ("2"):
                ubicacion = inputclass(
                    input("Ingrese la nueva ubicación del local: "), 50
                )
                regtemp.UbicacionLocal = ubicacion
                print("Desea modificar otro campo del local?")
                opcScreen = yes_no()
            case ("3"):
                rubro = inputclass(
                    validacion_rubro(input("Ingrese el nuevo rubro: ")), 50
                )
                regtemp.rubroLocal = rubro
                print("Desea modificar otro campo del local?")
                opcScreen = yes_no()
            case ("0"):
                return

        clear("cls")
        if opcScreen == "Y":
            pantalla_local()
            opc = input(
                "\n1-Nombre\n2-Ubicacion\n3-Rubro\nIngrese lo que desea modificar: "
            )

    clear("cls")
    print("Su local actualizado")
    pantalla_local()


""" Parametrizar esta funcion """


def mod_locales():
    def searchcod(regtemp, pos):
        if str(codLocal) == str(regtemp.codLocal).strip():
            return [regtemp, pos]
        else:
            return False

    codLocal = validar_tipo(
        input("Ingrese un código de local [0 para salir]: "), int, 0, 99999
    )

    if codLocal == 0:
        return

    localInfo = busquedasecuencial(
        ARCHIVO_LOGICO_LOCALES, ARCHIVO_FISICO_LOCALES, searchcod
    )
    local = localInfo[0]
    localPuntero = localInfo[1]

    while not (local) and codLocal != 0:
        codLocal = validar_tipo(
            "No se encontró ningún local con ese código, ingrese nuevamente [0 para salir]: ",
            int,
            0,
            99999,
        )
        localInfo = busquedasecuencial(
            ARCHIVO_LOGICO_LOCALES, ARCHIVO_FISICO_LOCALES, searchcod
        )
        local = localInfo[0]
        localPuntero = localInfo[1]

    if codLocal == 0:
        return

    pantalla_mod_locales(local)
    print("\nDesea guardar estos cambios ? [Y-Si, N-No]\n")
    opc = yes_no()
    if opc == "Y":
        updatedata(
            local,
            ARCHIVO_LOGICO_LOCALES,
            localPuntero,
            lj_locales,
        )
        print("Guardado exitoso UwU 😊")


mod_locales()


def crear_cuenta_dueno():
    nuevoUsuario = Usuario()
    encontro = True

    def autoincrementarcliente(regtem) -> int:
        return int(regtem.codUsuario) + 1

    def searchUser(regtemporal, p):
        if str(regtemporal.nombreUsuario).strip() == emailUsuario.strip():
            return True
        else:
            return False

    while encontro:
        emailUsuario = str(inputclass("ingrese el nombre de usuario: ", 100))

        encontro = busquedasecuencial(
            ARCHIVO_LOGICO_USUARIOS, ARCHIVO_FISICO_USUARIOS, searchUser
        )

    claveUsuario = inputclass("ingrese la clave: ", 8)

    TipoUsuario = "DuenoDeLocal"

    nuevoUsuario.codUsuario = autoincremental(
        ARCHIVO_LOGICO_USUARIOS, ARCHIVO_FISICO_USUARIOS, autoincrementarcliente
    )
    nuevoUsuario.nombreUsuario = emailUsuario
    nuevoUsuario.claveUsuario = claveUsuario
    nuevoUsuario.tipoUsuario = TipoUsuario

    savedata(
        nuevoUsuario, ARCHIVO_LOGICO_USUARIOS, ARCHIVO_FISICO_USUARIOS, lj_usuarios
    )


def test():
    objetos = []
    estados = ["pendiente", "rechazado", "aprobado"]
    for _ in range(20):
        objeto = {
            "precio": random.randint(1, 100),  # Precio aleatorio entre 1 y 100
            "estado": random.choice(estados),  # Estado aleatorio de la lista de estados
        }
        objetos.append(objeto)

    return objetos


""" def busquedasecuencialtest(array,callback):
    index = 0
    encontrado = False
    while index < len(array) and encontrado == False:
        callback()
        index += 1 """


def mostrar_descuentos_pendientes(registro):
    longitud = len(registro)
    if longitud > 0:
        for i in range(0, longitud):
            print(registro[i].codLocal)
            print(registro[i].estado)
            print(registro[i].codPromo)
    else:
        print("No hay archivos")


def aprobar_denegar_descuento():
    regPendientes: list[Promociones] = []

    def SearchState(regtemp, p):
        if str(regtemp.estado).strip() == "pendiente":
            regPendientes.append(regtemp)
        return False

    busquedasecuencial(
        ARCHIVO_LOGICO_PROMOCIONES, ARCHIVO_FISICO_PROMOCIONES, SearchState
    )

    mostrar_descuentos_pendientes(regPendientes)

    """ cod = input("Ingrese el cod de local que quiere aprobar/rechazar: ")
    while  cod  != "*":
        try:
            cod = int(cod)
            encontrado = False

            for i in range (0,len(regPendientes)): 
                if (cod == int(regPendientes[i].codLocal)):
                    encontrado = True

            if(encontrado):
                busquedasecuencial(ARCHIVO_LOGICO_PROMOCIONES, ARCHIVO_FISICO_PROMOCIONES, ModifyState)
            
        except:
            cod = input("Ingrese el cod de local que quiere aprobar/rechazar correctamente: ") """


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


# --------------------------------------- Funciones del Cliente ---------------------------------------------------------------------------------------------------------------------


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

    def autoincrementarcliente(regtem) -> int:
        return int(regtem.codUsuario) + 1

    while encontrado:
        email = inputclass(input("Ingrese email [0-Cancelar]:  "), 100)
        if email.strip() == "0":
            return

        password = inputclass(
            getpass.getpass("Ingrese su contraseña [0-Cancelar]: "), 8
        )

        if password.strip() == "0":
            return

        def searchUser(regtemporal, p):
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
    cliente.codUsuario = autoincremental(
        ARCHIVO_LOGICO_USUARIOS, ARCHIVO_FISICO_USUARIOS, autoincrementarcliente
    )
    cliente.tipoUsuario = "cliente"

    savedata(cliente, ARCHIVO_LOGICO_USUARIOS, ARCHIVO_FISICO_USUARIOS, lj_usuarios)

    print("Guardado existoso")

    os.system("pause")
    os.system("cls")

    cliente_menu()


def usuario_registrado():
    clear("cls")

    email = inputclass(input("Ingrese email: "), 100)
    password = inputclass(getpass.getpass("Ingrese su contraseña: "), 8)

    def login(regtemporal, p):
        print(regtemporal)
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


# --------------------------------------- Menu Principal ---------------------------------------------------------------------------------------------------------------------


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


# menuprincipal()


def mostrarUsuarios():
    t = os.path.getsize(ARCHIVO_FISICO_USUARIOS)
    ARCHIVO_LOGICO_USUARIOS.seek(0)
    while ARCHIVO_LOGICO_USUARIOS.tell() < t:
        regtemporal = pickle.load(ARCHIVO_LOGICO_USUARIOS)
        print(regtemporal.codUsuario)


# mostrarUsuarios()


""" def savePromos():
    estados = ["pendiente", "rechazado", "aprobado"]
    x = Promociones()
    t = os.path.getsize(ARCHIVO_FISICO_PROMOCIONES)
    ARCHIVO_LOGICO_PROMOCIONES.seek(0)
    for i in range(0, 20):
        x.codPromo = i
        x.textoPromo = "null"
        x.fechaDesdePromo = "null"
        x.HastaPromo = "null"
        x.diasSemana = [0] * 6
        x.estado = random.choice(estados)
        # estado (‘pendiente’, ‘aprobada’, ‘rechazada’) string(10)
        x.codLocal = i
        savedata(
            x, ARCHIVO_LOGICO_PROMOCIONES, ARCHIVO_FISICO_PROMOCIONES, lj_promociones
        )

savePromos() """


def mostrarLocales():
    ARCHIVO_LOGICO_LOCALES.seek(0)
    t = os.path.getsize(ARCHIVO_FISICO_LOCALES)
    while ARCHIVO_LOGICO_LOCALES.tell() < t:
        regTemp = pickle.load(ARCHIVO_LOGICO_LOCALES)
        print(regTemp.codLocal)


# mostrarLocales()
