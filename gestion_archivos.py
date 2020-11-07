import shutil
import os
import sys

class Archivo:
    def __init__ (self, nombre, directorio):
        self.__nombre = nombre
        self.__directorio = directorio
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def directorio(self):
        return self.__directorio
    
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor
        
    @directorio.setter
    def directorio(self,valor):
        self.__directorio = valor
        
    def copiar(self):
        shutil.copy(self.__nombre, self.__directorio)
    
    def mover(self):
        try:
            shutil.move(self.__nombre, self.__directorio)
        except:
            print(f"No puede mover el archivo a la misma direccion: \n {sys.exc_info()[0]}")
    
    @staticmethod
    def comprobar_file(nombre):
        while True:
            while os.path.exists(nombre)==False:
                nombre = input(f"El archivo {nombre} no existe\n intentalo nuevamente: ")
            if os.path.exists(nombre)==True:
                print(f"El archivo {nombre} si existe en el disco duro.")
                return nombre
                break
            
    @staticmethod
    def comprobar_dir(directorio):
        while True:
            while os.path.exists(directorio)==False:
                directorio = input(f"El directorio {directorio} no existe, intentalo nuevamente: ")

            if os.path.exists(directorio)==True:
                print(f"El directorio {directorio} si existe en el disco duro.")
                return directorio
                break
            
    @staticmethod
    def ver_directorio():
        print("Escoge un archivo del directorio actual.")
        print()
        for raiz, dirs, archivos in os.walk(".", topdown=False):    #Demostración de unpacking
            for nombre in archivos:
                print(os.path.join(raiz, nombre))
            for nombre in dirs:
                print(os.path.join(raiz, nombre))

    

#a = Archivo("bank.csv", r'C:\Users\Windows 10\Videos\python')
#a.copiar()        




    
    
    
    
    
    
    