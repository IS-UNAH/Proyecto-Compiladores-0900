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

import re

class Lexical:
    def __init__(self, reader):
        self.reader = reader
        self.fileName = self.reader.fileName
        self.text = self.reader.text
        self.patterns = []
        self.tokensDict = {}

    def processText(self):
        text = re.split(r"\n", self.text)

        cont = 0
        for line in text:
            cont += 1
            self.tokensDict[cont] = re.split(r"\s", line)
        return self

    def identifyToken(self):
        patterns = []

        for key in self.tokensDict:
            for arrToken in self.tokensDict[key]:
                if(arrToken != ''):
                        if re.match(r"\'[^\']*\'",arrToken):
                            patterns.append([key, arrToken, "Identificador de cadena"])

                        # Identificar de usuario
                        elif re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", arrToken):
                            patterns.append([key, arrToken, "Identificador de usuario"])

                        # Operador de asignacion
                        elif re.match(r"^=$", arrToken):
                            patterns.append([key, arrToken, "Operador de asignacion"])

                        # Operador de fin de Instruccion
                        elif re.match(r"^\$$", arrToken):
                            patterns.append([key, arrToken, "Identificador de fin de instruccion"])

                        # Numero
                        elif re.match(r"^\d+(\.\d+)?$", arrToken):
                            patterns.append([key, arrToken, "Identificador de Numero"])

                        # Operador Aritmetico
                        elif re.match(r"^[\+|\-\*\/]$", arrToken):
                            patterns.append([key, arrToken, "Operador Aritmetico"])

                        # Operador de repeticion
                        elif re.match(r"^\#$", arrToken):
                            patterns.append([key, arrToken, "Operador de repeticion"])
                        
                        # Operador de concatenacion
                        elif re.match(r"^\:$", arrToken):
                            patterns.append([key, arrToken, "Operador de concatenacion"])

                        else:
                            quit(
                                "Error: \n\tSe ha encontrado un token desconocido en la linea %s: %s \n\n" % (
                                    self.searchTokenLineError(arrToken),
                                    arrToken
                                )
                            )

        self.patterns = patterns
        return self

    def searchTokenLineError(self, token):
        errorLine = 0

        f = open(self.fileName, 'r')
        for line in f:
            errorLine += 1
            if re.match(r'^.*%s.*$' % self.prevent(token), line):

                break
        f.close()
        return errorLine

    def prevent(self, token):

        if re.match(r'[\+\*\.\(\)\{\}\[\]\\\<\>]', token):
            return '\\%s' % token
