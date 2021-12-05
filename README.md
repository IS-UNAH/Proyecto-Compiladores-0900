<div align="center">
    <img src="https://blog.mastercoria.com/wp-content/uploads/2018/02/compiladores-online.png" width="300px"> </img> 


# 0900 - IS-913_Diseño de Compiladores
Impartida por el *Ing. Alex Hernán Moncada Gómez*

# Proyecto lenguaje de programación
Ante las tres propuestas de proyecto ofrecidas, como equipo tomamos en consideracion los aspectos necesarios para la eleccion del ejercicio idoneo el cual serviria de proyecto final de esta clase, en nuetro caso despues de llevarlo a discucion se tomo la alternativa “Proyecto Lenguaje de Programación” (Opcion 3).  

El cual ante nuestra perspectiva, cumple a plenitud nuestras espectativas acerca de lo que un proyecto final podria llegara a ser. Nuestro proyecto se busca al menos el uso de 4 operaciones (Ya especificadas en la propuesta). Cabe recalcar que para la realizacion de este proyecto se busco por los medios existentes conocer mas acerca de los temas recabados en el periodo, de esta manera realizar un proyecto de altura para la clase en cuestion. 

En el presente informe se detalla todos los aspectos trabajados en el respectivo proyecto, ahondando en su funcionamiento, sus componentes, y aspectos generales de interes para el entendimiento completo del mismo.



## **Grupo #4**
| Nombre | Numero De Cuenta |
|:-------------:| :-----:|
| Gina Nicol Discua Quiroz | `20181005768` |
| Gerson David Chávez Figueroa | `20171000892` |
| Kevin Daniel Varela Vásquez | `20171004483` |
| Edgar Josué Benedetto Godoy | `20171033802` |
| Lisandro Alfredo Suárez Salinas | `20161002968` |
| Rafael Alberto Bautista Santos | `20151001991` |
| Cristian Alexander Martínez Ochoa | `20131015700` |

</div>

# Funcionamiento
La funcionalidad de nuestro código radica en la ejecución de tres distintas funciones con las cuales queremos resaltar las distintas etapas que se pueden ejecutar dentro de un compilador al momento de utilizar un lenguaje de programación. Estas funciones estan definidas como: un traductor, un analizador léxico y un árbol sintáctico, el cual se imprimira para poder mostrar las rutas que toma nuestro lenguaje de programación al momento de compilarlo. 

Para poder ejecutar nuestras distintas funciones, tenemos como dato de entrada el archivo “index.lng”, el cual contiene las siguientes instrucciones: 

# Traductor 
Como tal su funcionamiento se basa en recibir una entrada en este caso un archivo de texto, el cual producira una salida en este caso la conversion de este codigo, esta traduccion se hace basandose directamente en la gramatica que hemos definido en el proyecto. 

Al utilizar el comando “python3 main.py index.lng”  


# Analizador Léxico 
El Analizador Léxico mostrará de manera detallada los tokens y sus respectivos atributos obtenidos del archivo “index.lng” 
Al utilizar el comando “python3 main.py index.lng --analisis-lexico"


# Árbol Sintáctico 
Basicamente su funcionamiento es en poder tener una visualizacion mucho mas calara del arbol generado para poder traducir el codigo brindado. 
Al correr el comando “python3 main.py index.lng --arbol-sintactico" 
