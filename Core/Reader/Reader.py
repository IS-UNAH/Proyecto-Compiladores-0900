# -*- coding:utf-8 -*-
"""
----------------------------------------------------------------------------------------------------
    
    @author Grupo #4
    @date 27/11/2021
    @decription Leer archivo de texto plano .lng
    @name_file Reader.py
    @version 1.0

----------------------------------------------------------------------------------------------------
    
    !! Lector de parametros por consola y de archivos de texto plano
    * Lectura de los parametros envíados por consola.
    * Lectura del contenido del archivo enviado como parametro.
    ? Impresión del control de errores con color rojo (ANSI)

----------------------------------------------------------------------------------------------------
"""
import sys

class Reader():
    def __init__(self): 
        self.command = None
        self.fileName = None
        self.text = None

    def read(self):
        """ Leer el contenido del archivo de texto plano enviado como parametro"""
        self.params = sys.argv[1:]

        try:
            if len(self.params) == 2:
                self.command = self.params[1]
                self.fileName = self.params[0]
                f = open(self.fileName,'r')
                self.text = f.read()
                f.close()
            else:
                print("\033[31m"+"Error cantidad de parametros invalidos")

        except FileNotFoundError as e:
            print("\033[31m"+"Archivo no encontrado --> %s"%e)
        return self 