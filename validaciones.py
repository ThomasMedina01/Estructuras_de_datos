import time
from os import system,name

class Entrada:
    
    @staticmethod
    def limpiar_pantalla():
        if name == "nt":
            system("cls")
        else:
            system("clear")
    
    @staticmethod
    def bloqueo(segundos): 
        while segundos: 
            mins, secs = divmod(segundos, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("Tiempo de bloqueo: ",timer, end="\r") 
            time.sleep(1) 
            segundos -= 1

        print('Tiempo de bloqueo terminado, intentalo nuevamente.') 

    @staticmethod
    def validacion_entero(cadena):
        contador = 4
        while True:
            valor = input(cadena)
            try:
                valor = int(valor)
                return valor
            except ValueError:
                contador -= 1
                print()
                print(f"ATENCIÓN: Debe ingresar un número entero, tienes {contador} intentos más.")
                if contador == 0:
                    contador +=4
                    Entrada.bloqueo(10)
                
    @staticmethod           
    def validacion_flotante(cadena):
        contador = 4  
        while True:
            valor = input(cadena)
            try:
                valor = float(valor)
                return valor
            except ValueError:
                contador -= 1
                print()
                print(f"ATENCIÓN: Debe ingresar un número entero, tienes {contador} intentos más.")
                if contador == 0:
                    contador +=4
                    Entrada.bloqueo(10)
    @staticmethod
    def saltar():
        print()
    @staticmethod
    def separador():
        print("♦" * 100)
