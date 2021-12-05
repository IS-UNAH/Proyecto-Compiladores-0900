# -*- coding:utf-8 -*-
"""
----------------------------------------------------------------------------------------------------
    
    @author Grupo #4
    @date 02/12/2021
    @decription Traductor basico - Analisis Lexico, Sintactico y Semantico
    @name_file main.py
    @version 1.0

----------------------------------------------------------------------------------------------------
    
    ! Archivo Ejecutador
    ! Al momento de ejecutarlo se deben de enviar 4 parametros
        * python3 <nombreArchivo> <nombreArchivo> <comando>
    ? Impresión del control de errores con color rojo (ANSI)
    ? Comandos aceptados 
        * Imprimir tabla de símbolos 
            ? --symbols-table
        * Traduccion por gramatica libre de contexto 
            ? --grammar-translation
        * Imprimir arbol sintactico
            ? --syntactic-tree
        * Graficar arbol sintactico
            ? --graph-tree
----------------------------------------------------------------------------------------------------
"""
from Core.Analyzers.LexicalAnalyzer import Lexical
from Core.Analyzers.SyntacticAnalyzer import Syntactic
from Core.Analyzers.SemanticAnalyzer import Semantic
from Core.Graph.GraphTree import Graph
from Core.Reader.Reader import Reader
from tabulate import tabulate

reader = Reader().read()

if reader.command == "--symbols-table":
    print("\033[32m"+"%s " % "\n =========================== Tabla de Simbolos =========================== \n")
    tokens = Lexical(reader).processText().identifyToken().patterns
    headers = ['Linea','Token','Descripcion']
    if len(tokens) > 0:
        print(tabulate(tokens, headers, tablefmt="fancy_grid"))
    else:
        print("\033[31m"+"La tabla se encuentra vacia")

elif reader.command == '--grammar-translation':
    print("\033[34m"+"%s " % "\n =========================== Traduccion =========================== \n")
    text = Lexical(reader).processText().identifyToken().text
    Syntactic(text).run()


elif reader.command == "--syntactic-tree":
    print("\033[33m"+"%s " % "\n =========================== Arbol Sintactico =========================== \n")
    text = Lexical(reader).processText().identifyToken().text
    Syntactic(text).tree()

elif reader.command == "--graph-tree":
    print("\033[30m"+"\033[107m"+"%s " % "\n =========================== Grafico Arbol Sintactico =========================== \n")

    text = Lexical(reader).processText().identifyToken().text
    text_tree = Syntactic(text).text_tree()
    lexems = ['add', 'sub', 'mul', 'div', 'concatenate', 'repeat', 'getvar']
    text_tree= text_tree.replace("\t", "\n")
    info = text_tree.split("\n")
    
    for index, line in enumerate(info):
        lineStr = str(line).strip()
        if index != 0 and line.count("  ") == 0:
            blns = info[index - 1].count("  ") + 1
            tabs = "  "* blns
            info[index] = tabs  + lineStr

        if lineStr.count("'") > 0 or lineStr.count('"') > 0:
            blns = line.count("  ") + 1
            tabs = "  "* blns
            info[index] = tabs + lineStr
            
        if lineStr in lexems: 
            info[index - 1] = ('%s / %s') %( info[index - 1], lineStr)
            info.remove(line)
            
    prin = Graph()
    prin.graphTree(info)
    print("\033[30m"+"\033[107m"+"%s " % "                           Abriendo Grafico del arbol...                            \n")
else:
    quit("\033[31m"+"Faltan parametros, abocarse al README.md")
