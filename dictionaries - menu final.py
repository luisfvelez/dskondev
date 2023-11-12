# DSKON 1.1 (C) 1988 - 2023

def mostrar_menu(opciones):
    print ("DSKON DB Engine (C) 1988-2023 by LFVelezE")
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo...')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Ingresar data      1', accion1),
        '2': ('Imprimir data      2', accion2),
        '3': ('Buscar  data       3', accion3),
        '4': ('Guardar data       4', accion4),
        '5': ('Opción             5', accion5),
        '6': ('Salir              6', salir)
    }
    generar_menu(opciones, '6')

def accion1():
    print('Has elegido la opción 1')
    ap="1"
    pe=[]
    x= input("Ingresa el identificador: ")
    while ap!="" :
            ap=input ("ingrese los datos de ese identificador y presione enter para terminar  ")
            pe.append(ap)
    mi_diccionario[x]= pe


def accion2():
    print('Has elegido la opción 2')
    print ("Identificador--> Datos")
    for keys in mi_diccionario:
         print (keys, "----- >", mi_diccionario[keys])
    e=input("Fin .... Presione <enter>")

def accion3():
    print('Has elegido la opción 3')
    x= input("Ingresa el identificador: ")
    for keys in mi_diccionario:
        if x==keys:
            print (keys, "--- >", mi_diccionario[keys])
    print ("Fin de la busqueda ...")

def accion4():
    print('Has elegido la opción 4')
    with open("myDictionary.pkl", "wb") as tf:
        pickle.dump(mi_diccionario, tf)
    print ("Guardado ... ")

def accion5():
    print('Has elegido la opción 5')
    

def salir():
    print('Saliendo... ')
   


mi_diccionario={}
import pickle
with open("myDictionary.pkl", "rb") as tf:
        mi_diccionario = pickle.load(tf)
if __name__ == '__main__':
    menu_principal()
# (C) LFVELEZE Software