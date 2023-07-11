import os
import getpass
import colorama
from colorama import Fore, Back, Style
colorama.init()

""" STATUS """
advertencia = lambda txt : print(Fore.RED + txt, Fore.RESET)
completado = lambda txt : print(Fore.GREEN + txt,Fore.RESET)
aviso = lambda txt : print(Fore.YELLOW + txt,Fore.RESET)


codigo = [1, 2, 3, 4, 5, 6]
usuarios = [['admin@shopping.com', '12345', 'administrador'],
            ['LocalB@shopping.com', 'BBB123', 'duenoLocal'],
            ['LocalC@shopping.com', 'CCC123', 'duenoLocal'],
            ['LocalD@shopping.com', 'DDD123', 'duenoLocal'],
            ['LocalA@shopping.com', 'AAA123', 'duenoLocal'],
            ['LocalE@shopping.com', 'XDXDXD', 'Cliente']]


def busqueda_dicotomica(array,buscar):
    """ Llamar primero a falso burbuja e ingresar dos parametros el primero array a a ordenar y segundo valor a buscar  """
    col=1
    comienzo = 0
    fin=len(array)-1
    encontro= False
    while ( not(encontro) and comienzo <= fin):
        medio = (comienzo + fin) // 2
        if(buscar == array[medio][col]):
            encontro = True
        elif (buscar < array[medio][col]):
            fin = medio-1
        else:
            comienzo = medio +1
    if(encontro):
        print("Encontro:",array[medio][col])
    else:
        print("No encontro")

def falso_burbuja(array):
    """ Ingresar array a ordenar (Creciente) """
    k=0
    col = 1
    limit=len(array)
    for i in range (limit):
        for j in range (0,limit-i-1):
            if array[j][col] > array [j+1][col]:
               array[j],array[j+1] = array[j+1],array[j]


# Define constant
USUARIO_ADMIN = "admin@shopping.com"
CLAVE_ADMIN = "12345"
cont_indumentaria = 0
cont_perfumeria = 0
cont_comida = 0

clear = lambda x: os.system(x)





#funcion de ingreso
def yes_no():
    opcion = input('ingrese una opcion (y/n): ').upper()
    while opcion != 'Y' and opcion != 'N':
        opcion = input('error, ingrese una opcion valida (y/n): ').upper()
    return opcion

def validar_usuario(val,msg):
    aux = False
    while aux != True:
        opc = input(f'ingrese {msg}: ')
        if opc == val:
            aux = True
        else:
            print(f'el {msg} es incorrecto, intente nuevamente')
    return aux

def validar_clave(val,msg):
    i = 0
    aux = False
    while aux != True and i < 3:
        opc = input('ingrese la contraseña: ')
        if opc == val:
            aux = True
        else:
            print(f'la {msg} es incorrecta')
        i += 1
    return aux

def validar_tipo(opc,tipo,desde,hasta):
    try:
        opc = tipo(opc)
        while not(opc >= desde and opc <= hasta):
            print(f'opcion incorrecta, ingrese {desde} - {hasta}')
            opc = input('ingrese nuevamente: ')
            opc = tipo(opc)
    except:
        print('error debe ingresar un numero: ')
        opc = input('intente nuevamente: ')
        validar_tipo(opc,tipo,desde,hasta)
    return opc

def validar_ingreso():
    aux = False
    usuario = validar_usuario(USUARIO_ADMIN, 'usuario')
    if usuario:        
        clave = validar_clave(CLAVE_ADMIN, 'contraseña')
        if clave:
            aux = True
    return aux

# procedure
def construccion():
    print('en construcción...')
    clear('pause')

def mostrar_menu():
    print('Menú principal:\n1. Gestión de locales\n2. Crear cuentas de dueños de locales\n3. Aprobar / Denegar solicitud de descuento\n4. Gestión de novedades\n5. Reporte de utilización de descuentos\n0. Salir')

def menu_gestion_locales():
    print('menú de gestión de locales:\na. Crear locales\nb. Modificar local\nc. Eliminar local\nd. Volver')

def gestion_novedades():
    print('Gestion de novedades: \na. Crear novedades\nb. Modificar novedad\nc. Eliminar novedad\nd. Ver reporte de novedades \ne. Volver')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# funciones
def crear_locales():
    global cont_indumentaria, cont_perfumeria, cont_comida
    aux = 'Y'
    while aux == 'Y':
        clear('cls')
        nombre_local = input('ingrese el nombre del local: ')
        ubicacion_local = input('ingrese la ubicacion: ')
        rubro_local = validar_rubro()
        print(rubro_local)
        if rubro_local == 'i':
            cont_indumentaria += 1
        elif rubro_local == 'p':
            cont_perfumeria += 1
        else:
            cont_comida += 1
        print('¿desea cargar otro local?')
        aux = yes_no()
        mostrar_mayor()
        mostrar_menor()

def validar_rubro():
    rubro = input('ingrese el rubro (indumentaria (i) / perfumeria (p) / comida (c)): ')
    while rubro != 'i' and rubro != 'p' and rubro !='c':
        rubro = input('error, ingrese un rubro valido (indumentaria (i) / perfumeria (p) / comida (c)): ')
    return rubro

def validar_gestion_locales():
    clear('cls')  
    menu_gestion_locales()
    opcion = validar_tipo(input('ingrese una opcion: '),str,'a','d')
    match opcion:
        case 'a':
            crear_locales()
        case 'b':
            construccion()
        case 'c':
            construccion()
        case 'd':
            construccion()
    clear('cls')

def validar_novedades():
    clear('cls')  
    gestion_novedades()
    opcion = validar_tipo(input('ingrese una opcion: '),str,'a','e')
    match opcion:
        case 'a':
            construccion()
        case 'b':
            construccion()
        case 'c':
            construccion()
        case 'd':
            construccion()
        case 'e':
            print('volviste al menu')
    clear('cls')

def validar_menu():
    clear('cls')  
    mostrar_menu()
    opcion = validar_tipo(input('ingrese una opcion: '),str,'0','5')
    while opcion != '0':
        match opcion:
            case '1':
                validar_gestion_locales()
            case '2':
                construccion()
            case '3':
                construccion()
            case '4':
                validar_novedades()
            case '5':
                construccion() 
            case '0':
                print('has salido del programa')
        clear('cls')              
        mostrar_menu()
        opcion = validar_tipo(input('ingrese una opcion: '),str,'0','5')

def mostrar_mayor():
    rubro_mayor = ''
    contador_mayor = 0
    if cont_indumentaria > cont_comida and cont_indumentaria > cont_perfumeria:
        contador_mayor = str(cont_indumentaria)
        rubro_mayor = 'el rubro con mas locales fué: indumentaria, con '

    elif cont_comida > cont_indumentaria and cont_comida > cont_perfumeria:
        contador_mayor = str(cont_comida)
        rubro_mayor = 'el rubro con mas locales fué: comida, con '

    elif cont_perfumeria > cont_indumentaria and cont_perfumeria > cont_comida:
        contador_menor = str(cont_perfumeria)
        rubro_mayor = 'el rubro con mas locales fué: perfumeria, con '

    print(rubro_mayor, contador_mayor)



def mostrar_menor():
    rubro_menor = ''
    contador_menor = 0
    if cont_indumentaria < cont_comida and cont_indumentaria < cont_perfumeria:
        contador_menor = str(cont_indumentaria)
        rubro_menor = 'el rubro con menos locales fué: indumentaria, con '

    elif cont_comida < cont_indumentaria and cont_comida < cont_perfumeria:
        contador_menor = str(cont_comida)
        rubro_menor = 'el rubro con menos locales fué: comida, con '

    elif cont_perfumeria < cont_indumentaria and cont_perfumeria < cont_comida:
        contador_menor = str(cont_perfumeria)
        rubro_menor = 'el rubro con menos locales fué: perfumeria, con '

    print(rubro_menor, contador_menor)

def inicio():
    validar_menu() if validar_ingreso() else print('Alcanzó el límite de inicio de sesion')

inicio()

