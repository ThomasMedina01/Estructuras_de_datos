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
    

    
            


    



