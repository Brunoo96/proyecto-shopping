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


""" codLocal = [[0 for _ in range(2)] for _ in range(0, 50)]
for i in range(50):
    codLocal[i][0] = i + 1 """
# codLocal = [[codigo de local1, codigo de usuario],[codigo de local2, codigo de usuario]]


datosLocal = [
    ["" for _ in range(0, 4)] for _ in range(0, 50)
]  # [[rubro], [nombre], [ubicacion], estado]
""" Metodos de array """


codUsuario = [1, 2, 3, 4, 5, 6]
usuarios = [
    ["admin@shopping.com", "12345", "Administrador"],
    ["LocalA@shopping.com", "AAA123", "duenoLocal"],
    ["LocalB@shopping.com", "BBB123", "duenoLocal"],
    ["LocalC@shopping.com", "CCC123", "duenoLocal"],
    ["LocalD@shopping.com", "DDD123", "duenoLocal"],
    ["LocalE@shopping.com", "XDXDXD", "Cliente"],
]


""" datosLocal = [
    ["Indumentaria", "Paz", "Rosario", "A"],
    ["Perfumeria", "Letra", "Bermudez", "A"],
    ["", "", "", ""],
    ["Indumentaria", "Per", "Perez", "A"],
    ["Comida", "McDonalds", "Alvarez", "A"],
    ["Indumentaria", "Nike", "Rosario", "A"],
    ["Comida", "Mostaza", "Bermudez", "A"],
    ["Perfumeria", "Lata", "Perez", "B"],
] """


codLocal = [[0 for _ in range(0, 2)] for _ in range(0, 50)]


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
        """print("Encontro:", array[medio][col])"""
        return True
    else:
        """print("No encontro")"""
        return False


def falsoburbuja(array, col):
    """Paramaetros :Array(Ordenar), Columna(Ordenar)"""
    limit = len(array) - 1
    for i in range(0, limit):
        for j in range(i + 1, limit + 1):
            if array[i][col] > array[j][col]:
                aux = array[i]
                array[i] = array[j]
                array[j] = aux


def burbuja_indices(arreglo, codigos):
    n = len(arreglo)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if arreglo[i][1] > arreglo[i + 1][1]:
                # Ordenar el arreglo de strings
                arregloAux = arreglo[i]
                arreglo[i] = arreglo[i + 1]
                arreglo[i + 1] = arregloAux
                # Ordenar el arreglo de índices correspondientes

                codigosAux = codigos[i]
                codigos[i] = codigos[i + 1]
                codigos[i + 1] = codigosAux

                swapped = True


def busqueda_secuencialBI(array, f, buscar):
    """Ingresar array a buscar , Fila ,Elemento a buscar en el array"""
    data = ["False", [], []]
    index = 0
    limit = len(array) - 1
    encontrado = False
    while index <= limit and not (encontrado):
        if array[index][f] == buscar:
            encontrado = True
            data = ["True", array[index]]
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


def validar_nombre(nombre):
    aux = datosLocal[:]
    falsoburbuja(aux, 1)
    encontro = busqueda_dicotomica(aux, nombre)
    if not (encontro):
        return nombre
    else:
        print("el nombre está ocupado")
        return validar_nombre(input("Ingrese el nombre nuevamente: "))


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
    if usuarios[usuario - 1][2] == "duenoLocal":
        return usuarios[usuario - 1][1]
    else:
        print_advertencia(
            "El usuario ingresado no es un Dueño de local quisieras ingregar otro usuario?"
        )
        opc = yes_no()
        while opc == "Y":
            return validacion_usuario(
                validar_tipo(
                    input("Ingrese nuevamente un codigo de usuario: "), int, 1, 6
                )
            )
        return False


# [[rubro], [nombre], [ubicacion], estado]
def mod_locales():
    bool = True
    aux = "Y"

    cod = validar_tipo(
        input("ingrese el codigo del local que desea modificar: "), int, 1, 50
    )

    while bool and aux == "Y":
        print("Que desea modificar ? \n 1-Rubro \n 2-Nombre \n 3-Ubicacion")
        opcion = input("")
        match opcion:
            case "1":
                datosLocal[cod - 1][0] = validacion_rubro(
                    input("ingrese el rubro del local: "), ""
                )
                print_completado("Guardado Exitoso")
            case "2":
                datosLocal[cod - 1][1] = validar_nombre(
                    input("ingrese el nombre del local: ")
                )
                print_completado("Guardado Existoso")
            case "3":
                datosLocal[cod - 1][2] = input("ingrese la ubicacion del local: ")
                print_completado("Guardado Existoso")
            case _:
                print("asd")
        print("desea modificar algo más?")
        aux = yes_no()
    print(datosLocal)
    clear("pause")
    clear("cls")


# [[rubro], [nombre], [ubicacion], estado]
def crear_locales():
    opcion = validar_tipo(
        input("Ingrese codigo del local : "), int, 1, 50
    )  # codLocal[i][0]

    codusuario = validacion_usuario(
        validar_tipo(input("Ingrese codigo de usuario "), int, 1, 6)
    )  # codLocal[i][1]

    if datosLocal[opcion - 1][2] == "" and codusuario:
        rubrolocal = validacion_rubro(input("ingrese el rubro del local: "), "")
        nombrelocal = validar_nombre(input("ingrese el nombre del local: "))
        ubicacionlocal = input("ingrese la ubicacion del local: ")
        if codusuario:
            datosLocal[opcion - 1][0] = rubrolocal
            datosLocal[opcion - 1][1] = nombrelocal
            datosLocal[opcion - 1][2] = ubicacionlocal
            datosLocal[opcion - 1][3] = "A"
            codLocal[opcion - 1][1] = codusuario
    print_aviso("Volvera al menu principal")
    input("")
        


def elim_locales():
    opcion = validar_tipo(
        input("ingrese el codigo del local que desea eliminar: "), int, 0, 50
    )
    print_advertencia("El local va ser dado de baja esta seguro de este movimiento? ")

    opcyesno = yes_no()
    # codigo = [codLocal, indice]
    if opcyesno == "Y":
        print_aviso(f"el local {opcion} se ha dado de baja")
        datosLocal[opcion - 1][3] = "B"
    else:
        print_aviso("El local no se dio de baja")
    clear("pause")


""" Fomat y Ljust """


def mostrar_locales_desc():
    """Rubro con menos locales o mas"""
    aux = [["indumentaria", 0], ["comida", 0], ["perfumeria", 0]]
    locales_activos = [["" for _ in range(0, 4)] for _ in range(0, 50)]
    for i in range(0, len(datosLocal)):
        if datosLocal[i][0].lower() == "indumentaria" and datosLocal[i][3] == "A":
            aux[0][1] += 1
        elif datosLocal[i][0].lower() == "comida" and datosLocal[i][3] == "A":
            aux[1][1] += 1
        elif datosLocal[i][0].lower() == "perfumeria" and datosLocal[i][3] == "A":
            aux[2][1] += 1
    falsoburbuja(aux, 1)

    """ Guarda Locales en otro array ya ordenados para la muestra """
    dat_loc_ord = datosLocal[:]
    falsoburbuja(dat_loc_ord, 0)
    index = 0
    for l in range(0, 3):
        for k in range(0, len(datosLocal)):
            if dat_loc_ord[k][0].lower() == aux[l][0] and dat_loc_ord[k][3] != "B":
                locales_activos[index] = dat_loc_ord[k]
                index += 1


def mapa_locales():
    burbuja_indices(datosLocal, codLocal)
    """ print(datosLocal, codLocal) """
    num_columnas = 5
    for fila in range(10):
        for columna in range(5):
            indice = fila * num_columnas + columna
            """ print(f"+-+\n|{codLocal[indice][0]}|") """

    a = ""
    techo = "+--"
    techo = techo * 5 + "+"
    casa = " "
    print(codLocal)
    print(techo)
    for i in range(0, 5):
        a += "|" + str(codLocal[i][0]) + "|"
    print(a)
    for i in range(1, 50):
        if (i % 5) == 0:
            print(techo)
            print(a)


def gestion_locales():
    a = """
        a) Crear locales 
        \nb) Modificar local 
        \nc) Eliminar local 
        \nd) Mapa de locales   
        \ne) Volver"""
    clear("cls")
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


def inicio():
    data = validar_ingreso()
    match data[2]:
        case "Administrador":
            admin_menu()
        case "DuenoLocal":
            owner_menu()
        case "Cliente":
            cliente_menu()


inicio()
