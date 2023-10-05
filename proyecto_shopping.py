import getpass
import random

import os
import io
import pickle
import time
import datetime
import math

# import colorama
""" while True:   
    size = os.get_terminal_size()
    print(f"Ancho de la terminal: {size.columns} columnas")
    print(f"Alto de la terminal: {size.lines} filas")
 """

# from colorama import Fore, Back, Style


# colorama.init()


from faker import Faker

#from rich import print

# print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

# print_advertencia = lambda txt: print(Fore.RED + txt, Fore.RESET)
# print_completado = lambda txt: print(Fore.GREEN + txt, Fore.RESET)
# print_aviso = lambda txt: print(Fore.YELLOW + txt, Fore.RESET)
clear = lambda x: os.system(x)

#-------------------------------------------------------Classes----------------------------------------------------
class Session:
    def __init__(self):
        self.codUsuario= 0
        self.nombreUsuario= ""
        self.tipoUsuario= ""


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
        self.codLocal = 0
        # estado (‘pendiente’, ‘aprobada’, ‘rechazada’) string(10)


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


#---------------------------------------Archivos----------------------------------------
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

#------------------------------------------------Session-----------------#
NowSession = Session()
#------------------------------------------------Formateadores-----------------------------------------------------------
def lj_usuarios(x):
    x.codUsuario = str(x.codUsuario).ljust(8).lower()
    x.nombreUsuario = str(x.nombreUsuario).ljust(100).lower()
    x.claveUsuario = str(x.claveUsuario).ljust(8).lower()
    x.tipoUsuario = str(x.tipoUsuario).ljust(20).lower()

def saveSession(session:Usuario):
    NowSession.codUsuario = str(session.codUsuario).strip()
    NowSession.nombreUsuario = str(session.nombreUsuario).strip()
    NowSession.tipoUsuario = str(session.tipoUsuario).strip()

def lj_locales(x):
    x.codLocal = str(x.codLocal).ljust(8).lower()
    x.nombreLocal = str(x.nombreLocal).ljust(50).lower()
    x.ubicacionLocal = str(x.rubroLocal).ljust(50).lower()
    x.rubroLocal = str(x.rubroLocal).ljust(50).lower()
    x.codUsuario = str(x.codUsuario).ljust(40).lower()
    x.estado = str(x.estado).ljust(2)


def lj_promociones(x):
    x.codPromo = str(x.codPromo).ljust(8).lower()
    x.textoPromo = str(x.textoPromo).ljust(200).lower()
    x.fechaDesdePromo = str(x.fechaDesdePromo).ljust(10).lower()
    x.HastaPromo = str(x.HastaPromo).ljust(10).lower()
    x.diasSemana = [0] * 6
    x.estado = str(x.estado).ljust(10).lower()
    x.codLocal = str(x.codLocal).ljust(8).lower()


def lj_uso_promociones(x):
    x.codCliente = str(x.codCliente).ljust().lower()
    x.codPromo = str(x.codPromo).ljust().lower()
    x.fechaUsoPromo = str(x.fechaUsoPromo).ljust().lower()


def ljnovedades(x):
    x.codNovedad = str(x.codNovedad).ljust().lower()
    x.textoNovedad = str(x.textoNovedad).ljust().lower()
    x.fechaDesdeNovedad = str(x.fechaDesdeNovedad).ljust().lower()
    x.fechaHastaNovedad = str(x.fechaHastaNovedad).ljust().lower()
    x.tipoUsuario = str(x.tipoUsuario).ljust().lower()
    x.estado = str(x.estado).ljust().lower()

#-------------------------------- Services -------------------------------------

#Funcion para obetener todos los locales
def findBusinessA()-> list[Locales]:
    localesActivos = []
    
    def Searchlocalactivo(regtemp,pos):
        if str(regtemp.estado).strip() == 'A':
            localesActivos.append(regtemp)
            return False

    busquedasecuencial(ARCHIVO_LOGICO_LOCALES, ARCHIVO_FISICO_LOCALES, Searchlocalactivo)

    return localesActivos 

#Funcion para obenter todos los locales activos
def findBusiness() -> list[Locales]:
    localesActivos = []

    def Searchlocal(regtemp:Locales,pos):
        localesActivos.append(regtemp)

        return False
        
    busquedasecuencial(ARCHIVO_LOGICO_LOCALES, ARCHIVO_FISICO_LOCALES, Searchlocal)

    return localesActivos 

def findBusinessById(id):
    localesActivos = []
    
    def Searchlocalbycod(regtemp,pos):
        if str(regtemp.codUsuario).strip() == id :
            localesActivos.append(regtemp)
        return False

    busquedasecuencial(ARCHIVO_LOGICO_LOCALES, ARCHIVO_FISICO_LOCALES, Searchlocalbycod)

    return localesActivos 
     


#-------------------------------- Funciones - Views -----------------------------------------------

def testSchema(colsDate:list[str],data:list[str]):
    #cols=["CodLocal","Nombre","Estado"]
    # Obtener el tamaño de la terminal
    tamano_terminal = os.get_terminal_size()
    
    # Extraer el número de columnas y filas
    columnas, filas = tamano_terminal.columns, tamano_terminal.lines
    #print(columnas,"Columnas")

    numberColsDate= len(colsDate)

    #Espacio para separar los datos
    space = ((columnas-numberColsDate) // numberColsDate)
    
    #Agregar espacio
    for i in range(0,numberColsDate):
        colsDate[i]= text_center(colsDate[i],space)
    
    techo  = "-"*columnas
    pared= ""
    header= "|"

    for i in range(0,numberColsDate):
        mid = (space-len(colsDate[i]))/2
        header += colsDate[i] + "|"
        
    print(techo)
    print(header)
    print(techo)
    for i in range(0,len(data)):
        pared+="|"
        for t  in range(0,numberColsDate):
            pared+=text_center(text_format(data[i][t],space),space) +"|"
        pared+="\n"
        pared+=techo
        
    print(pared)
        


    #print("| DATO | ")
    
def charge(load:int, hz=2):
    flagi = True
    charge= "Cargando"
    index = 0
    points =0
    
    while index  < load :        
        clear("cls")
        charge+="."
        points+=1
        if(points == 4):
            points=0
            charge="Cargando"
        print(charge)
        time.sleep(1/hz)
        index += 1/hz
        
#-------------------------------- Funciones - Utils -----------------------------------------------
#Funcion para emparejar el texto en la pantalla 
def text_center(data,space):
    mid = (space- len(data)) / 2
    parte_decimal = mid - int(mid)
    if(str(parte_decimal) == "0.0"):
        mid=int(mid)
        return (" "*mid)+data+(" "*mid)
    else:
        mid = int(mid)
        return (" "*mid)+" "+data+(" "*mid)    

#Funcion para cortar la longitud del texto
def text_format(data:str,length:int):
    aux = ""
    if(len(data) > length):
        for i in range(0,length-3):
            if(data[i]=="\n"):
                aux+=""
            else:  
                aux+=data[i]
    else:
        aux=data
    return aux

#Funcion para guardar en los archivos (Guarda a lo ultimo del archivo)
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

#Funcion para modificar una data de los archivos
def updatedata(data, ARCHIVO_LOGICO: io.BufferedRandom, PosPuntero: str, formatter):
    try:
        formatter(data)

        ARCHIVO_LOGICO.seek(PosPuntero)

        pickle.dump(data, ARCHIVO_LOGICO)

        ARCHIVO_LOGICO.flush()

    except:
        print("Error inesperado")

#Funcion para convertir una clase a array bidimensional 
def Class_to_Bidimensional(registro:list,callback) -> list:
    aux=[]
    flag = True
    index = 0
    while flag :
        try:
            aux.append(callback(registro,index))
            index+=1
        except:
            flag = False
    if(len(aux)):
        for i in range(0,len(aux)):
            for t in range(0,len(aux[0])):
                aux[i][t] = str(aux[i][t]).strip()
    return aux
            
#Funcion para mostrar los locales en modo schema    
def pantalla_locales(locales:list[Locales]):
    def upperCase(cadena):
        aux = ""
        for i in range (0,len(cadena)):
            if(i ==0):
                aux +=cadena[0].upper()
            else:
                aux +=cadena[i]
        return aux
    
    def formater(locales:list,i:int):
        return [locales[i].codUsuario,locales[i].codLocal,upperCase(locales[i].nombreLocal),upperCase(locales[i].UbicacionLocal),upperCase(locales[i].rubroLocal),locales[i].estado] 
    lenght = len(locales)

    def sort(auxi,auxj,logica):
        if(auxi[2] > auxj[2]):
            logica()
            
    locales_bidi=Class_to_Bidimensional(locales,formater)

    falso_burbuja_array(locales_bidi,sort)

    cols=["CodUsuario","CodLocal","Nombre","Ubicacion","Rubro","Estado"]

    testSchema(cols,locales_bidi)

#Funcion para verificar si ya existe una administrador
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

#Funcion para buscar un elemento en especifico
def busquedasecuencial(
    ARCHIVO_LOGICO: io.BufferedRandom, ARCHIVO_FISICO: str, callback
) :
    tamañoarchivo = os.path.getsize(ARCHIVO_FISICO)
    ARCHIVO_LOGICO.seek(0)
    encontrado = False

    while ARCHIVO_LOGICO.tell() < tamañoarchivo and encontrado == False:
        posicion = ARCHIVO_LOGICO.tell()
        regtemporal = pickle.load(ARCHIVO_LOGICO)
        encontrado = callback(regtemporal, posicion)

    return encontrado

#Test de funcion para mostrar locales
def mostrarLocales():
    ARCHIVO_LOGICO_LOCALES.seek(0)
    t = os.path.getsize(ARCHIVO_FISICO_LOCALES)
    while ARCHIVO_LOGICO_LOCALES.tell() < t:
        regTemp = pickle.load(ARCHIVO_LOGICO_LOCALES)
        print(regTemp.nombreLocal,"22")
        print(regTemp)
        #pantalla_locales([regTemp])

#Funcion para ordenar un archivo completo
def falso_burbuja(ARCHIVO_LOGICO: io.BufferedRandom, ARCHIVO_FISICO: str,callback):
    tamarchivo = os.path.getsize(ARCHIVO_FISICO)
    if tamarchivo <= 0:
        ARCHIVO_LOGICO.seek(0)
        aux = pickle.load(ARCHIVO_LOGICO)
        Tamregistro = ARCHIVO_LOGICO.tell()
        print(Tamregistro)
        print(tamarchivo)
        cantreg = int(tamarchivo // Tamregistro)
        print(cantreg)
        for i in range(0, cantreg - 1):
            for j in range(i + 1, cantreg):
                ARCHIVO_LOGICO.seek(i * Tamregistro, 0)
                auxi = pickle.load(ARCHIVO_LOGICO)
                ARCHIVO_LOGICO.seek(j * Tamregistro, 0)
                auxj = pickle.load(ARCHIVO_LOGICO)
                callback(auxi,auxj,logicafb) 
            def logicafb():
                ARCHIVO_LOGICO.seek(i * Tamregistro, 0)
                pickle.dump(auxj, ARCHIVO_LOGICO)
                ARCHIVO_LOGICO.seek(j * Tamregistro, 0)
                pickle.dump(auxi, ARCHIVO_LOGICO)
                print(auxi.codLocal,auxj.codLocal)
    
#Funcion para ordenar un array 
def falso_burbuja_array(lista,callback):  
    def logica():
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux
        
    length = len(lista)
    
    for i in range(0,length-1):
        for j in range(i+1,length):
            callback(lista[i],lista[j],logica)
    
def busquedadico(data, ARCHIVO_LOGICO, ARCHIVO_FISICO):
    ARCHIVO_LOGICO.seek(0, 0)

    aux = pickle.load(ARCHIVO_LOGICO)

    tamregi = ARCHIVO_LOGICO.tell()

    inicio = 0
                                                    
    cantreg = int(os.path.getsize(ARCHIVO_FISICO) / tamregi)

    fin = cantreg-1
    

    dato = str(data.upper())
    while inicio <= fin:
        medio = (inicio + fin) // 2
        ARCHIVO_LOGICO.seek(medio * tamregi)  #tamregi                                                                                                                                                                              tamaño de cada registro en bytes
        registro = pickle.load(ARCHIVO_LOGICO)
        nombres = str(registro.nombreLocal.upper())
        print(nombres.strip(),"e",dato.strip(),"e")
        if nombres.strip() == dato.strip():
            return medio  # Se encontró el elemento en la posición "medio"
        elif nombres.strip() < dato.strip():
            inicio = medio + 1
        else:
            fin = medio - 1

    return False # Elemento no encontrado


def busquedaSecuencialArray(Lista:list,callback):
    encontrado = False
    hasta = len(Lista)
    index = 0
    while index < hasta and not(encontrado):
        print(Lista[index])
        encontrado = callback(Lista[index])
        index=+1
        
    return encontrado

#Test de funcion para cargar locales 
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
    index = 1
    for i in range(0, 20):
        NuevoLocal = Locales()

        NuevoLocal.codLocal = inputclass(str(index), 8)
        NuevoLocal.nombreLocal = inputclass("test", 50).lower()
        NuevoLocal.UbicacionLocal = inputclass("test", 50)
        NuevoLocal.rubroLocal = inputclass(randomm(), 50)
        NuevoLocal.codUsuario = inputclass(str(random.randint(5, 8)), 40)
        NuevoLocal.estado = inputclass("A", 2)

        print(
            f"\n codLocal:{NuevoLocal.codLocal},\n nombre:{NuevoLocal.nombreLocal},\n ubicacion: {NuevoLocal.UbicacionLocal},\n rubro: {NuevoLocal.rubroLocal}"
        )
        print(NuevoLocal.codUsuario)
        index += 1
        savedata(NuevoLocal, ARCHIVO_LOGICO_LOCALES, ARCHIVO_FISICO_LOCALES, lj_locales)

# Funcion de ingreso que acepta si o no
def yes_no() -> str:
    opcion = input("ingrese una opcion [Y-Si, N-No]: ").upper()
    print("")
    while opcion != "Y" and opcion != "N":
        opcion = input("error, ingrese una opcion valida [Y-Si, N-No]: ").upper()
        print("")
    return opcion

# Funcion para verificar el tipo de un dato y verificar el intervalo
def validar_tipo(opc, tipo, desde: int, hasta: int) -> str | int:
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

#Funcion para validar contraseña 3 intentos
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

#Test de funcion para ver todos los usuarios registrados
def mostrarUsuarios():
    t = os.path.getsize(ARCHIVO_FISICO_USUARIOS)
    ARCHIVO_LOGICO_USUARIOS.seek(0)
    while ARCHIVO_LOGICO_USUARIOS.tell() < t:
        regtemporal:Usuario = pickle.load(ARCHIVO_LOGICO_USUARIOS)
        print(regtemporal.codUsuario,regtemporal.nombreUsuario,regtemporal.claveUsuario,regtemporal.tipoUsuario)
    time.sleep(2)

def inputclass(opc: str, length: int) ->str:
    while not (len(opc) < length):
        opc = input(f"Error, Ingrese nuevamente (hasta {length} caracteres): ")
    return opc.ljust(length)

#Funcion para validar el dominio
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

#Funcion para validar el rubro
def validacion_rubro(rubro: str)-> str:
    rubro = str(rubro)
    while (
        rubro.lower() != "perfumeria"
        and rubro.lower() != "comida"
        and rubro.lower() != "indumentaria"
    ):
        rubro = input("Ingrese un rubro correcto [indumentaria,comida,perfumeria]: ")
    return rubro

#Funcion para buscar el autoincremental de un archivo
def autoincremental(ARCHIVO_LOGICO: io.BufferedRandom, ARCHIVO_FISICO):
    t = os.path.getsize(ARCHIVO_FISICO)
    ARCHIVO_LOGICO.seek(0)
    pickle.load(ARCHIVO_LOGICO)
    tamano = ARCHIVO_LOGICO.tell()
    total = t//tamano 
    return total+1

#No me acuerdo
def extract_characters(listaFilter,callback)-> list:
    enum = []
    for i in range(0,len(listaFilter)):
        character = callback(i,listaFilter)
        enum.append(character)
    return enum   
          
#Test para la funcion promociones
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

#Funcion en proceso
def date():
    flag = True
    while flag:
        try:
            fecha = input("Ingresa una fecha en el formato DD/MM/AAAA: ")
            datetime.datetime.strptime(fecha, "%d/%m/%Y")
            while datetime.datetime.strptime(fecha, "%d/%m/%Y") < datetime.datetime.now() and flag:
                print("Fecha invalida, fuera de tiempo")
                fecha = input("Ingresa una fecha en el formato DD/MM/AAAA: ")
                datetime.datetime.strptime(fecha, "%d/%m/%Y")
            print("Fecha valida")
            flag = False
        except ValueError:
            print("Fecha invalida")
    dia, mes, anio = fecha.split("/")
    return fecha

#Funcion para validar un enum
def validar_enum(opc:str | int,enum:list) -> str:
    index= 0
    flag = True
    while (flag):
        while (index < len(enum)):
            if(opc == enum[index]):
                flag = False
                return opc
            elif (opc=="0" ):
                return opc
            index+=1
        index=0
        opc = input("Error, ingrese nuevamente: ")


def findPromotion(id) -> list:
    promociones:list[Promociones] = []
    locales:list[Locales]

    def searchPromotionbycod(regtemp,pos):
        if str(regtemp.codLocal).strip() == locales[i] :
            promociones.append([str(regtemp.codLocal).strip(),regtemp])
        return False
    
    locales = findBusinessById(id) # Trae registros
    
    for i in range(0,len(locales)):
        locales[i] = [str(locales[i].codLocal).strip()]
    

    for i in range(0,len(locales)):
        busquedasecuencial(ARCHIVO_LOGICO_PROMOCIONES,ARCHIVO_FISICO_PROMOCIONES,searchPromotionbycod)
    
    
    return promociones
    
findPromotion("5")



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
    while opcion  != 0:
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
                reporte_descuentos()
            case 0:
                return
        print(auxp)
        opcion = validar_tipo(input("Ingrese una opcion "), int, 0, 5)

# -------------------Gestion de locales
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
        clear("cls")       
        print(a)

        opcion = validar_tipo(input("Ingrese una opcion  "), str, "a", "e")
    clear("cls")

# ------------------ SubMenus de Gestion de locales
def crear_locales():
    local = "-1"
    encontrado = True
    continuar= "Y"
    NuevoLocal = Locales()
    localesession:list[Locales] = []
    locales = findBusiness()    

    def searchNameVolatil(data):
        print(data)
        print(local)
        if(local == data.nombreLocal):
            return True
        else:
            return False

    def searchUserDueñoLocal(regtemporal, p):
        if (
            str(codduenolocal).strip() == str(regtemporal.codUsuario).strip()
            and str(regtemporal.tipoUsuario).strip() == "DuenoDeLocal"
        ):
            return regtemporal.codUsuario
        else:
            return False
        
    def refresh():
        clear("cls")
        print("Todos los campos son requeridos: \n")
        pantalla_locales([NuevoLocal])
    
    def formatter(locales:list,i:int):
        return [locales[i].nombreLocal,locales[i].UbicacionLocal,locales[i].rubroLocal,locales[i].codUsuario,locales[i].codLocal] 
    
    def comparision(auxi,auxj,logicafb):
        print(auxi.nombreLocal)
        if str(auxi.nombreLocal).strip() > str(auxj.nombreLocal).strip():
            print(auxi.nombreLocal,auxj.nombreLocal)
            logicafb()

    NuevoLocal = Locales()
    
    
    falso_burbuja(ARCHIVO_LOGICO_LOCALES,ARCHIVO_FISICO_LOCALES,comparision)
    #refresh()
    pantalla_locales(locales)

    while continuar == "Y":
        local = input("\nIngrese un nombre de local [0 para salir]: ")
        while local == "0" or busquedadico(local,ARCHIVO_LOGICO_LOCALES,ARCHIVO_FISICO_LOCALES) or busquedaSecuencialArray(localesession,searchNameVolatil):
            if(local =="0"):
                return
            local= input("\nError nombre existente: Ingrese un nombre de local [0 para salir]: ")
            
        NuevoLocal.nombreLocal = local
        refresh()

        ubicacion = input("\nIngrese la ubicacion del local: ")
        NuevoLocal.UbicacionLocal = ubicacion
        refresh()

        rubro = validacion_rubro(input("\nIngrese el rubro del local: "))
        NuevoLocal.rubroLocal = rubro
        refresh()

        codduenolocal = int(input("\nIngrese un código de un dueño de local: "))
        while not(busquedasecuencial(ARCHIVO_LOGICO_USUARIOS,ARCHIVO_FISICO_USUARIOS,searchUserDueñoLocal)):
            codduenolocal = int(input("Ingrese un código de un dueño de local: "))
        NuevoLocal.codUsuario = codduenolocal
        refresh()
        
        NuevoLocal.codLocal = autoincremental(ARCHIVO_LOGICO_LOCALES, ARCHIVO_FISICO_LOCALES)
        refresh()
                

        localesession.append(NuevoLocal)
                    
        print("Desea seguir cargando locales?")
        continuar = yes_no()
        if(continuar == "Y"):
            NuevoLocal = Locales()    
            refresh()
         
    print("Desea guardar estos locales ?: ")        
    pantalla_locales(localesession)

    save = yes_no()
    if save == 'Y':
        for i in range(0, len(localesession)):
            savedata(localesession[i],ARCHIVO_LOGICO_LOCALES,ARCHIVO_FISICO_LOCALES,lj_locales)
        print("Guardado exitoso 📈 ")        


def mod_locales():
    local:Locales
    localPuntero:str
    codLocal = -1

    def searchBusiness(regtemp, pos):
        if str(codLocal) == str(regtemp.codLocal).strip():
            return [regtemp, pos]
        else:
            return False


    while codLocal != 0:
        locales = findBusiness()    
        clear("cls")
        
        pantalla_locales(locales)
        print("\nIngrese el local que desea modificar: \n")

        codLocal = validar_tipo(input("Ingrese un código de local [0 para salir]: "), int, 0, len(locales)-1)
        
        [local,localPuntero] = busquedasecuencial(ARCHIVO_LOGICO_LOCALES, ARCHIVO_FISICO_LOCALES, searchBusiness)
        
        if(local and codLocal != 0):

            save=pantalla_mod_locales(local)    

            if(save):    
                print("\nDesea guardar estos cambios ?\n")
                opc = yes_no()
                if opc == "Y":
                    updatedata(
                        local,
                        ARCHIVO_LOGICO_LOCALES,
                        localPuntero,
                        lj_locales,
                    )
                    []
                    print("Guardado exitoso UwU 😊")
                    clear("pause")

            else:
                print("\nDesea ingresar otro local? \n")


def elim_locales():    
    clear("cls")
    localesActivos = findBusinessA()    

    pantalla_locales(localesActivos)
         
    bool = True

    while bool:
        cod = validar_tipo(input("Ingrese el código de local que desea dar de baja [0 para salir]: "),int,0,len(localesActivos))
        if(cod !=  0): 
            baja_logica(cod)
        else:
            bool= False

def mapa_locales():
    def comparision(auxi,auxj,logica):
        if str(auxi.nombreLocal).strip() > str(auxj.nombreLocal).strip():
            print(auxi.nombreLocal,auxj.nombreLocal )
            logica()
    
    falso_burbuja(ARCHIVO_LOGICO_LOCALES,ARCHIVO_FISICO_LOCALES,comparision)
    mockup:Locales = Locales()

    #Variable con todos los datos de los locales
    locales = findBusiness()

    #Variable con la longitud de los locales
    locales_creados= len(locales)
    
    #Variable ya formateada con sus 50 locales para mostrar en el mapa de locales
    locales_map:list[Locales] = [*locales,*[mockup]*(50-locales_creados)]
    
    techo= "+-+-+-+-+-+"
    aux=techo+"\n"
    
    for i in range(1,len(locales_map)+1):
        local= str(locales_map[i-1].codLocal).strip()
        aux+=f"|{local}"
        if ( i % 5 ==0):
            aux+="|"
            aux += "\n"+techo+"\n"
    print(aux) 

    clear("pause")
    clear("cls")

#mapa_locales()
#---------------------------
def pantalla_mod_locales(local: Locales) -> bool:
    clear("cls")    
    opcScreen = "Y"
    
    print("EDITANDO 🔧 - 🔧 - 🔧 \n")
    pantalla_locales([local])

    opc = input(
        "\n1-Nombre\n2-Ubicacion\n3-Rubro\n4-Estado\n0-Salir\n\nIngrese lo que desea modificar:  "
    )
    
    while opcScreen == "Y":
        match (opc):
            case ("1"):
                nombre = inputclass(input("Ingrese el nuevo nombre del local: "), 50)
                local.nombreLocal = nombre                
                print("Desea modificar otro campo del local?")
                opcScreen = yes_no()
            case ("2"):
                ubicacion = inputclass(
                    input("Ingrese la nueva ubicación del local: "), 50
                )
                local.UbicacionLocal = ubicacion                
                print("Desea modificar otro campo del local?")
                opcScreen = yes_no()
            case ("3"):
                rubro = inputclass(
                    validacion_rubro(input("Ingrese el nuevo rubro: ")), 50
                )
                local.rubroLocal = rubro                
                print("Desea modificar otro campo del local?")
                opcScreen = yes_no()
            case("4"):
                if(str(local.estado).strip() == "A"):
                    print("Su estado ya esta dado de alta si quiere darlo de baja entre a la opcion 3-[Eliminar Locales]")
                    clear("pause")
                    print("Quieres ser redirigido?")
                    opc = yes_no()                    
                    if(opc =="Y"):
                        baja_logica(str(local.codLocal).strip())          
                        local.estado="B"                        
                        clear("pause")
                else:
                    local.estado = "A"
                    print("Estado actualizado")
                    clear("pause")
                    print("Desea modificar otro campo del local?")
                    opcScreen = yes_no()
            case ("0"):
                return False

        clear("cls")
        if opcScreen == "Y":
            print("EDITANDO 🔧 - 🔧 - 🔧 \n")
            print(local.nombreLocal)
            pantalla_locales([local])
            opc = input(
                "\n1-Nombre\n2-Ubicacion\n3-Rubro\n4-Estado\n0-Salir\nIngrese lo que desea modificar: "
            )
            
    clear("cls")
    print("Su local actualizado")
    print("EDITANDO 🔧 - 🔧 - 🔧 \n")
    pantalla_locales([local])
    return True

                       
def baja_logica(cod:str) :
    def Searchlocal(regtemp,pos):
        if str(regtemp.codLocal).strip() == str(cod) and str(regtemp.estado).strip()  == 'A':
            return [regtemp,pos]
        else:
            return False
        

    Local:Locales
    pos:int
    [Local,pos] = busquedasecuencial(ARCHIVO_LOGICO_LOCALES, ARCHIVO_FISICO_LOCALES, Searchlocal)
    
    if Local:
        pantalla_locales([Local])

        print("¿Está seguro que desea dar de baja este local?")
    
        opc = yes_no()

        if opc == 'Y':
            Local.estado="B"
            
            updatedata(Local,ARCHIVO_LOGICO_LOCALES,pos,lj_locales)

            print("Baja existosa")
                
#---------------------------
def reporte_descuentos():
    print("Fecha Mínima: ")
    fechadesde = date()
    print("Fecha Máxima: ")
    fechahasta = date()
   
#---------------------------
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
        emailUsuario = str(inputclass(input("ingrese el nombre de usuario: "), 100))

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


def mostrar_descuentos_pendientes(registro:list[Promociones]):
    clear("cls")
    colsPromocion = ["Nombre","CodLocal","CodPromocion","Estado"]
    data = []
    for i in range(0,len(registro)):
        data.append([str(registro[i].codLocal).strip(),str(registro[i].codPromo).strip(),str(registro[i].estado).strip(),"null"])
    
    testSchema(colsPromocion,data) 

    """ longitud = len(registro)
    if longitud > 0:
        for i in range(0, longitud):
            print("Código de local: ",registro[i].codLocal)
            print("Código de promoción del local: ",registro[i].codPromo)
            print("Estado del local: ",registro[i].estado)
            print("\n")
    else:
        print("No hay archivos") """


def promotionsPending() -> list[Promociones]  :
    regPendientes: list[Promociones] = []

    def SearchState(regtemp, p):
        if str(regtemp.estado).strip() == "pendiente":
            regPendientes.append(regtemp)
        return False    
        
    busquedasecuencial(
        ARCHIVO_LOGICO_PROMOCIONES, ARCHIVO_FISICO_PROMOCIONES, SearchState
    )
    
    return regPendientes

    
def logica_descuento(cod:int):
    regtemp:Promociones
    pos:int

    def Searchcodstate(regtemp,pos):
            if str(cod) == str(regtemp.codPromo).strip():
                return [regtemp,pos]
            else:
                return False       

    [regtemp,pos]=busquedasecuencial(ARCHIVO_LOGICO_PROMOCIONES,ARCHIVO_FISICO_PROMOCIONES,Searchcodstate) 

    if regtemp:
        opc = input("Desea rechazar o aprobar la promoción del local?: ").lower()
        print(opc)
        
        while opc != "aprobar" and opc != "rechazar" and opc != "salir":
            opc = input("Escriba correctamente si desea rechazar o aprobar la promoción del local: ").lower()

        match (opc):
            case ("aprobar"):
                print("Estás seguro que desea aprobar esta promoción?")
                yn = yes_no()
                if yn == 'Y':
                    regtemp.estado = "aprobado"
                    updatedata(regtemp, ARCHIVO_LOGICO_PROMOCIONES,pos,lj_promociones)
                    print("Guardado exitoso! 🕵️‍♂️ ")
            case ("rechazar"):
                print("Estás seguro que desea rechazar esta promoción?")
                yn = yes_no()
                if yn  == 'Y':
                    regtemp.estado = "rechazado"
                    updatedata(regtemp, ARCHIVO_LOGICO_PROMOCIONES,pos,lj_promociones)
                    print("Guardado existoso! 🕵️‍♂️ ")
            case("salir"):
                return
            
                
def aprobar_denegar_descuento():            
    cod:str
    enum:list
    
    regPendientes  = promotionsPending()

    def filter(i:int,promociones:list[Promociones]):
        return str(promociones[i].codLocal).strip()

    enum = extract_characters(regPendientes,filter)

    mostrar_descuentos_pendientes(regPendientes)

    cod = validar_enum(input("Ingrese el cod de promoción que quiere aprobar/rechazar [0-Salir]: "),enum)

    while (cod != "0"):
        logica_descuento(cod)
        print("Desea seguir en aprobar/denegar descuentos?: ")
        continuar=yes_no()
        if(continuar == "Y"): 
            cod =validar_enum(input("Ingrese el cod de promoción que quiere aprobar/rechazar [0-Salir]: "),enum)
        elif(continuar == "N"):
            return
              

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

def owner_menu():
    #os.system("cls")
    a = "Menú principal:\n1. Crear descuento\n2. Reporte uso de descuentos\n3. Ver novedades\n0. Salir"
    print(a)
    opc = validar_tipo(input("Ingrese una opción: "), int, 0, 3)
    match (opc):
        case (1):
            crear_descuento()
        case (2):
            reporte_uso_desc()
        case (3):
            print("Está en chapin")
        case (0):
            print("Ha salido")

def crear_descuento():
    
    def filter(i:int,locales:list[locales]):
        return str(locales[i].codLocal).strip()
    
    promotion = findPromotion()  
    codlocales = extract_characters(locales,filter)
    cod = validar_enum(input("Ingrese el codigo de su local para aplicar un descuento [0-Salir]: "),codlocales)
    while cod != 0 or not(busquedasecuencial(ARCHIVO_LOGICO_LOCALES, ARCHIVO_FISICO_LOCALES, Findcod)):
        descripcion = input("Ingrese los detalles de su descuento: ")
        print("Ingrese desde que fecha quiere que se habilite su descuento ")
        desdefecha = date()
        print("Ingrese hasta que fecha quiere que su descuento esté disponible")
        hastafecha = date()
        
    cod = validar_enum(input("Ingrese el codigo de su local para aplicar un descuento [0-Salir]: "),codlocales)

def reporte_uso_desc():
    print("CHAU!")

# --------------------------------------- Funciones del Cliente ---------------------------------------------------------------------------------------------------------------------

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
"""    cliente_menu()"""


def usuario_registrado():
    usuario:Usuario
    clear("cls")

    email = inputclass(input("Ingrese email: "), 100)
    password = inputclass(getpass.getpass("Ingrese su contraseña: "), 8)

    def login(regtemporal, p):
        if (
            str(regtemporal.nombreUsuario).strip() == email.strip()
            and str(regtemporal.claveUsuario).strip() == password.strip()
        ):
            return regtemporal
        else:
            return False

    usuario = busquedasecuencial(ARCHIVO_LOGICO_USUARIOS, ARCHIVO_FISICO_USUARIOS, login)

    saveSession(usuario) if (usuario) else None
    
    charge(4)
    match (NowSession.tipoUsuario):
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



menuprincipal()

