Aquí la explicación de cada archivo:

-estudiantes_ABB_.py: En este archivo se encuentran las clases Nodo y ABB, la clase Nodo se encarga de generar la estructara de un árbol
ABB, teniendo un hijo izquierdo, un hijo derecho y un dato (en este caso un estudiante). La clase ABB se encarga de operar sobre ese nodo, es decir, tiene los metodos con los cuales se inserta, elimina, busca, etc.

-estudiantes_Bmas.py: Este archivo tiene como proposito generar un árbol B+, en este caso tiene 2 clases de Nodo,
un Nodo Interno (solo tiene referencias e hijos) y un Nodo Hoja (que tiene referencias, datos y punteros a otros Nodos Hojas). Esta
clase hace uso de las otras 2, con las cuales guarda la información, pero es la clase ArbolBmas la encargada de administrar sus hijos, claves y datos.

-estudiantes_lista.py: Es una clase cuyos metodos permiten operar sobre listas (en este caso de estudiantes).

-Helper.py: Una clase que se utiliza para generar los estudiantes y guardarlos en disco.

-Medición: Este archivo se encarga de medir tiempos, sacar promedios y comparativas.
