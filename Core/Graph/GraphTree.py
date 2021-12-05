#-*- coding: utf-8 -*-
from os import scandir
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image
from networkx.drawing.nx_pydot import graphviz_layout

class Graph:
    def __init__(self):
        self.grafo=None
        self.anex = None
        self.arrayRutes = []
        self.arrayWeight = []

    #Función que crea el grafo tipo TDA con los datos del TextEdit
    def graphTree(self, value):
        # print(value)
        lenTree= len(value)-1
        currentEdge1 = None
        currentEdge2 = None
        currentEdge3 = None
        currentEdge4 = None
        currentVertex = None
        G = nx.DiGraph()

        #variable que contendra la imagen
        image = plt.figure(1, figsize=(55,20), dpi=60)

        for i in range(lenTree):

            #Dependiendo el tabulado se sabrá si es vertice, arista o caracteristica
            if(value[i].count("  ") == 0):
                
                currentVertex = value[i]
                #Se agraga al grafo tipo TDA como vertice por poseer 0 Tab en su cadena
                G.add_node("%s" % currentVertex)

            else:
                if (value[i].count("  ") == 1):
                    #Se elimina el tabulado de la cadena quedando el nombre real de la arista
                    currentEdge1 = value[i].lstrip("  ")
                    #Se agraga al grafo tipo TDA como arista por poseer 0 Tab en su cadena
                    G.add_node("%s" % currentEdge1)
                    if currentVertex:
                        G.add_edge("%s" % currentVertex, "%s" % currentEdge1, weight=1)

                if(value[i].count("  ") == 2):
                    currentEdge2 = value[i].lstrip("  ")
                    #Se agraga al grafo tipo TDA como arista por poseer 0 Tab en su cadena
                    G.add_node("%s" % currentEdge2)
                    if currentEdge1:
                        G.add_edge("%s" % currentEdge1, "%s" % currentEdge2, weight=1)
                
                if(value[i].count("  ") == 3):
                    currentEdge3 = value[i].lstrip("  ")
                    #Se agraga al grafo tipo TDA como arista por poseer 0 Tab en su cadena
                    G.add_node("%s" % currentEdge3)
                    if currentEdge2:
                        G.add_edge("%s" % currentEdge2, "%s" % currentEdge3, weight=1)

                if(value[i].count("  ") == 3):
                    currentEdge3 = value[i].lstrip("  ")
                    #Se agraga al grafo tipo TDA como arista por poseer 0 Tab en su cadena
                    G.add_node("%s" % currentEdge3)
                    if currentEdge2:
                        G.add_edge("%s" % currentEdge2, "%s" % currentEdge3, weight=1)

                if(value[i].count("  ") == 4):
                    currentEdge4 = value[i].lstrip("  ")
                    #Se agraga al grafo tipo TDA como arista por poseer 0 Tab en su cadena
                    G.add_node("%s" % currentEdge4)
                    if currentEdge3:
                        G.add_edge("%s" % currentEdge3, "%s" % currentEdge4, weight=1)

                if(value[i].count("  ") == 5):
                    currentEdge4 = value[i].lstrip("  ")
                    #Se agraga al grafo tipo TDA como arista por poseer 0 Tab en su cadena
                    G.add_node("%s" % currentEdge4)
                    if currentEdge3:
                        G.add_edge("%s" % currentEdge3, "%s" % currentEdge4, weight=1)

        #pos = nx.circular_layout(G)
        """
        T = nx.balanced_tree(n,G)

        pos = graphviz_layout(T, prog="dot")
        nx.draw(G,pos, with_labels=True, arrows=True, node_size=5000,node_color='#a8dee3',node_shape='8')
        """

        pos = graphviz_layout(G, prog='dot')

        #lista de nodos del grafo
        nlist = [node for node in G.nodes()]

        #lista de aristas del grafo
        elist = [edge for edge in G.edges()]
        nx.draw_networkx_nodes(G, pos,  nodelist = nlist, node_size= 5000, node_shape="o", node_color="#B9BCD6")
        nx.draw_networkx_labels(G,pos,font_size=20, font_color="k", font_family="sans-serif", font_weight="normal", horizontalalignment="center", verticalalignment="center", clip_on=True)
        #nx.draw_networkx_edge_labels(G,pos)
        nx.draw_networkx_edges(G, pos,edgelist=elist,width=3, arrowstyle='-|>',arrowsize=10, node_size= 5000 )
        #Guardado de la imagen/Mapa de los nodos y aristas edge_labels={('A','B'):'8',('B','C'):'12',('C','D'):'7',('E','D'):'15',('B','D'):'9'}
        image.savefig('/home/benedetto/Documentos/IS913 - 0900 - Diseño de Compiladores/Proyecto Repositorio/proyecto-compiladores-0900/Img/GraphTree.png')
        img = Image.open('/home/benedetto/Documentos/IS913 - 0900 - Diseño de Compiladores/Proyecto Repositorio/proyecto-compiladores-0900/Img/GraphTree.png')
        img.show()


        

        