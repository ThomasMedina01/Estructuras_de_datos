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
        
    @nombre.setter
    def directorio(self,valor):
        self.__directorio = valor
    

#a = Archivo("bank.csv", r'C:\Users\Windows 10\Videos\python')
#a.copiar()        




    
    
    
    
    
    
    