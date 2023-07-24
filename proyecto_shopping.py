import os
import getpass
import colorama
from colorama import Fore, Back, Style

colorama.init()


# Define constant
cont_indumentaria = 0
cont_perfumeria = 0
cont_comida = 0

""" STATUS """
print_advertencia = lambda txt: print(Fore.RED + txt, Fore.RESET)
print_completado = lambda txt: print(Fore.GREEN + txt, Fore.RESET)
print_aviso = lambda txt: print(Fore.YELLOW + txt, Fore.RESET)

clear = lambda x: os.system(x)


codUsuario = [1, 2, 3, 4, 5, 6]
usuarios = [
    ["admin@shopping.com", "12345", "Administrador"],
    ["LocalB@shopping.com", "BBB123", "duenoLocal"],
    ["LocalC@shopping.com", "CCC123", "duenoLocal"],
    ["LocalD@shopping.com", "DDD123", "duenoLocal"],
    ["LocalA@shopping.com", "AAA123", "duenoLocal"],
    ["LocalE@shopping.com", "XDXDXD", "Cliente"],
]
codLocal = [[0 for _ in range(2)] for _ in range(0, 50)]
# codLocal = [[codigo de local1, codigo de usuario],[codigo de local2, codigo de usuario]]
for i in range(50):
    codLocal[i][0] = i + 1


datosLocal = [
    ["" for _ in range(0, 4)] for _ in range(0, 50)
]  # [[nombre], [ubicacion], [rubro], estado]
""" Metodos de array """

print(datosLocal)


def busqueda_dicotomica(array, buscar):
    """Llamar primero a falso burbuja e ingresar dos parametros el primero array a a ordenar y segundo valor a buscar"""
    col = 1
    comienzo = 0
    fin = len(array) - 1
    encontro = False
    while not (encontro) and comienzo <= fin:
        medio = (comienzo + fin) // 2
        if buscar == array[medio][col]:
            encontro = True
        elif buscar < array[medio][col]:
            fin = medio - 1
        else:
            comienzo = medio + 1
    if encontro:
        print("Encontro:", array[medio][col])
    else:
        print("No encontro")


def falsaburbujaBI(datos_local, datos_usuario):
    for i in range(0, len(datos_local) - 1):
        for j in range(1, len(datos_local) - 1):
            if datos_local[i][0] < datos_local[j][0]:
                auxLocal = datos_local[i]
                auxCliente = datos_usuario[i][0]
                datos_local[i][0] = datos_local[j]
                datos_usuario[i] = datos_usuario[j][0]
                datos_local[j][0] = auxLocal
                datos_usuario[j][0] = auxCliente
    return datos_usuario


def busqueda_secuencialBI(array, f, buscar):
    """Ingresar array a buscar , Fila ,Elemento a buscar en el array"""
    data = ["False", [], []]
    index = 0
    limit = len(array) - 1
    encontrado = False
    while index <= limit and not (encontrado):
        if array[index][f] == buscar:
            encontrado = True
            data = ["True", array[index], index]
        else:
            index += 1
    return data


""" def buscar_indice(array, elemento): """


def busqueda_secuencialUNI(array, buscar):
    """Ingresar array a buscar , Fila ,Elemento a buscar en el array"""
    data = ["False", []]
    index = 0
    limit = len(array) - 1
    encontrado = False
    while index <= limit and not (encontrado):
        if array[index] == buscar:
            encontrado = True
            data = ["True", array]
        else:
            index += 1
    return data


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


def validar_email(email):
    emailpass = "False"
    while emailpass == "False" and email != "0":
        [STATUS, MSG] = validar_dominio(email)
        if STATUS == "True":
            [true, data] = busqueda_secuencialBI(usuarios, 0, email)
            # data = ['usuario', 'clave','tipo']
            if true == "True":
                emailpass = "True"
            else:
                print_advertencia("Este email no existe")
                email = input("")
        else:
            clear("cls")
            print_advertencia(MSG)
            email = input("")
    return [emailpass, data]


def validar_ingreso():
    email = input("Ingrese email: ")
    [true, data] = validar_email(email)
    if true == "True":
        i = 0
        password = " "
        while i <= 2 and password != data[1]:
            password = input(f"Ingrese contraseña, tiene {3-i} intentos : ")
            user = busqueda_secuencialUNI(data, password)
            # clave = "password"
            if user[0] != "True":
                i += 1
            else:
                return user[1]
        print_advertencia("Has superado el limite de intentos saliendo del programa...")
        input("Apretar cualquier tecla para cerrar")


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


def cliente_menu():
    print(
        """Menú principal:
        \n1. Registrarme
        \n2. Buscar descuentos en locales
        \n3. Solicitar descuento
        \n4. Ver novedades
        \n0. Salir"""
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

# funciones


def admin_menu():
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
            """crear_cuenta()"""
        case 3:
            """solic_descuento()"""
        case 4:
            gestion_novedades()
        case 5:
            """reporte_descuentos()"""


def mostrar_locales():
    print("¿desea ver los locales actuales?")
    opcion = yes_no()
    match opcion:
        case "Y":
            for i in range(50):
                if datosLocal[i][2] != 0:
                    print(f"código: {codLocal}")
                    print(f"nombre: {datosLocal[i][0]}")
                    print(f"ubicacion: {datosLocal[i][1]}")
                    print(f"rubro: {datosLocal[i][2]}")


def validacion_rubro(rubro, resultado):
    rubros = ["indumentaria", "perfumeria", "comida"]
    resultado = resultado
    index = 0
    bandera = False
    while not (bandera) and index < 3:
        if rubro == rubros[index]:
            bandera = True
            resultado = rubros[index]
        else:
            index += 1
    if bandera:
        return resultado
    else:
        return validacion_rubro(input("Ingrese un rubro correcto: "), resultado)


def validacion_usuario(usuario):
    try:
        if usuarios[usuario][2] == "duenoLocal":
            return usuarios[usuario][2]
    except:
        print(
            "El usuario ingresado no es un Dueño de local quisieras ingregar otro usuario? [Si] [No]"
        )
        opc = yes_no()
        if opc == "Y":
            print("////")
        else:
            return False


def mod_locales():
    """mostrar_locales()"""
    opcion = validar_tipo(
        input("ingrese el codigo del local que desea modificar: "), int, 0, 50
    )

    if datosLocal[opcion][2] != "0":
        datosLocal[opcion][0] = input("ingrese el nombre del local: ")
        datosLocal[opcion][0] = input("ingrese la ubicacion del local: ")
        datosLocal[opcion][0] = validacion_rubro(
            input("ingrese el rubro del local: "), ""
        )
    else:
        print("el codigo ingresado no pertenece a un local existente")


def crear_locales():
    opcion = validar_tipo(
        input("Ingrese codigo del local : "), int, 1, 50
    )  # codLocal[i][0]

    codusuario = validacion_usuario(
        validar_tipo(input("Ingrese codigo de usuario "), int, 0, 6)  # codLocal[i][1]
    )

    if datosLocal[opcion - 1][2] == "":
        nombrelocal = input("ingrese el nombre del local: ")
        ubicacionlocal = input("ingrese la ubicacion del local: ")
        rubrolocal = validacion_rubro(input("ingrese el rubro del local: "), "")
        if codusuario:
            datosLocal[opcion - 1][0] = nombrelocal
            datosLocal[opcion - 1][1] = ubicacionlocal
            datosLocal[opcion - 1][2] = rubrolocal
            datosLocal[opcion - 1][3] = "A"
            print(datosLocal)
    else:
        print("el codigo ingresado pertenece a un local existente")


crear_locales()






def mostrar_locales_desc():
    aux = [["indumentaria", 0], ["comida", 0], ["perfumeria", 0]]
    for i in range(0, len(datosLocal)):
        if datosLocal[i][0] == "indumentaria":
            aux[0][1] += 1
        elif datosLocal[i][0] == "comida":
            aux[1][1] += 1
        elif datosLocal[i][0] == "perfumeria":
            aux[2][1] += 1
    mayor(aux)


def mayor(rubros):
    falsoburbuja(rubros, 1)
    print(rubros, "Este tiene que venir ordeando")
    for t in range(0, len(rubros)):
        for i in range(0, len(datosLocal)):
            if rubros[t][0] == datosLocal[i][0]:
                """print(datosLocal[i][0])"""


def imprimir_datos(datos):
    # Encabezados
    print("{: <8} {: >7} {: >11} {: >8}".format(" Rubro", "Nombre", "Ubicacion","Estado"))
    print("{:-<7} {:-<8} {:->11} {:->8}".format("","","",""))
    # Datos
    for nombre, rubro, ubicacion,estado in datos:
        print("{: <12} {: >10} {: >10.2f}".format(rubro, nombre, ubicacion,estado))

def falsoburbuja(array, col):
    print(array)
    limit = len(array) - 1
    for i in range(0, limit):
        for j in range(i + 1, limit + 1):
            print(j)
            if array[i][col] > array[j][col]:
                aux = array[i]
                array[i] = array[j]
                array[j] = aux


def elim_locales(array):
    """mostrar_locales()"""
    opcion = validar_tipo(
        input("ingrese el codigo del local que desea eliminar: ", int, 0, 50)
    )
    codigo = busqueda_secuencialBI(array, 0, opcion)
    # codigo = [codLocal, indice]
    datosLocal[codigo[2]][0] = ""
    datosLocal[codigo[2]][1] = ""
    datosLocal[codigo[2]][2] = ""
    datosLocal[codigo[2]][3] = ""


def mapa_locales():
    map = [[0] * 5 for i in range(10)]
    falsoburbuja(datosLocal, codLocal)
    for p in range(50):
        for i in range(5):
            for j in range(10):
                map[i][j] = codLocal[p][1]
    return map


def gestion_locales():
    clear("cls")
    print(
        """
          a) Crear locales 
        \nb) Modificar local 
        \nc) Eliminar local 
        \nd) Mapa de locales   
        \ne) Volver"""
    )
    opcion = validar_tipo(input("Ingrese una opcion "), str, "a", "c")
    match opcion:
        case "a":
            crear_locales()
        case "b":
            mod_locales()
        case "c":
            elim_locales()
        case "d":
            mapa_locales()
    clear("cls")


def inicio():
    data = validar_ingreso()
    match data[2]:
        case "Administrador":
            admin_menu()
        case "DuenoLocal":
            owner_menu()
        case "Cliente":
            cliente_menu()


print()
