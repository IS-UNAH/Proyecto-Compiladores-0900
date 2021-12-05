# -*- coding: utf-8 -*-
"""
----------------------------------------------------------------------------------------------------
    
    @author Grupo #4
    @date 01/11/2021
    @decription Analisis sintactico con Lark
    @name_file SyntacticAnalyzer.py
    @version 1.0

----------------------------------------------------------------------------------------------------

    ! Análisis Semántico con Lark
    * Uso del árbol el parseo LALR --> Look-Ahead LR
    * Uso de la funcion 'pretty' para mostrar y graficar el arbol sintactico producid por Lark

----------------------------------------------------------------------------------------------------
"""
from Core.Analyzers.Grammar import *
from Core.Analyzers.SemanticAnalyzer import Semantic
from lark import Lark, Transformer


class Syntactic:
    def __init__(self, text):
        self.text = text

    def run(self):
        parser = Lark(grammar, parser="lalr", transformer=Semantic())
        language = parser.parse
        sample = self.text

        try:
            language(sample)
        except Exception as e:
            print("Error: %s" % e)

    def tree(self):
        parser = Lark(grammar, parser="lalr")
        language = parser.parse
        sample = self.text

        try:
            print(language(sample).pretty())
        except Exception as e:
            print("Error: %s" % e)
    
    def text_tree(self):
        parser = Lark(grammar, parser="lalr")
        language = parser.parse
        sample = self.text

        try:
            return language(sample).pretty()

        except Exception as e:
            print("Error: %s" % e)