from gestion_archivos import *
from validaciones import *
from os import system

principal = ['1.- Cambiar el directorio local', '2.- Copiar un archivo',
             '3.- Mover un archivo','4.- Historial de movimientos.', '5.- Salir']

movimientos = list()
dir_mov = list()
tipo = list()

Entrada.separador()
print("Sistema de administración de archivos.")
Entrada.separador()
directorio = input("Para comenzar, introduce un directorio: ")
directorio = Archivo.comprobar_dir(directorio)
dir_actual = os.chdir(directorio)
Entrada.saltar()
Entrada.separador()

try:
    while True:
        Entrada.saltar()
        print("Sistema de administración de archivos.")
        Entrada.separador()
        rango = (1, 2, 3, 4, 5)
        #Entrada.limpiar_pantalla()
        for i in principal:
            print(i)
        opcion = Entrada.validacion_entero("Elige la opcion deseada: ")
        contador = 4
        while opcion not in rango:
            opcion = Entrada.validacion_entero("La opcion elegida no existe, intentalo de nuevo: ")
            contador -= 1
            print(f"Intentos restantes: {contador}")
            Entrada.separador()
            if contador == 0:
                contador +=4
                Entrada.bloqueo(10)
        Entrada.saltar()

        if opcion == 1:
            Entrada.limpiar_pantalla()
            Archivo.ver_directorio()
            Entrada.saltar()
            Entrada.separador()
            salida = Entrada.validacion_entero("Presione 1 para salir o 2 para cambiar de directorio : ")
            while salida not in (1, 2):
                salida = Entrada.validacion_entero("Presione 1 para salir o 2 para cambiar de directorio : ")
                
            if salida == 1:
                Entrada.limpiar_pantalla()
                Entrada.separador()
                pass
                
            if salida == 2:
                Entrada.limpiar_pantalla()
                directorio = input("Introduce el nuevo directorio: ")
                directorio = Archivo.comprobar_dir(directorio)
                dir_actual = os.chdir(directorio)
                Archivo.ver_directorio()
                Entrada.saltar()
                Entrada.separador()

        if opcion == 2:
            Entrada.limpiar_pantalla()
            nombre = input("Nombre del archivo con su extension: ")
            Archivo.comprobar_file(nombre)
            movimientos.append(nombre)
            
            Entrada.saltar()
            Entrada.separador()

            dir_actual = os.getcwd()
            destino = input("Directorio destino del archivo: ")
            Archivo.comprobar_dir(destino)
            dir_mov.append(destino)
            
            Entrada.saltar()
            Entrada.separador()
            
            tipo.append(0)
            archivo = Archivo(nombre, destino)
            archivo.copiar()
            
            Entrada.saltar()
            Entrada.separador()
            
        if opcion == 3:
            Entrada.limpiar_pantalla()
            nombre = input("Nombre del archivo con su extension: ")
            Archivo.comprobar_file(nombre)
            movimientos.append(nombre)
            
            Entrada.saltar()
            Entrada.separador()
            
            dir_actual = os.getcwd()
            destino = input("Directorio destino del archivo: ")
            Archivo.comprobar_dir(destino)
            dir_mov.append(destino)
            
            Entrada.saltar()
            Entrada.separador()
            
            archivo = Archivo(nombre, destino)
            archivo.mover()
            tipo.append(1)
            
            Entrada.saltar()
            Entrada.separador()

                


    
            


    



