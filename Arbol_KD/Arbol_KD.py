class Nodo:
    """
    Nodo: La estructura base para el Arbol_KD, con este se puede guardar la información de un punto y guardar 2 punteros (hijos) que serán utilizados
    en el árbol.
    """
    def __init__(self, bordes):
        self.bordes = bordes
        self.hijo_izq = None
        self.hijo_der = None


class Arbol_KD:
    """
    Arbol_KD = Clase utilizada para construir un arbol de K dimensiones (No en su totalidad, aun tiene partes que se dejan en 2D),
    ____

    Atributos:
    raiz: El nodo raiz apartir el cual se crea el árbol.
    """

    def __init__(self, datos):
        """
        datos= Un iterable (lista) con las cordenadas para construir el árbol.
        -----
        El constructor del arbol, con este se genera toda la estructura.
        """

        profundidad = 0

        parametro = profundidad%len(datos[0])#Esto para el caso de K Dimensiones

        datos = sorted(datos, key= lambda d : d[parametro])
        self.raiz = Nodo(datos[len(datos)//2])#Esta media se calcula asmumiendo una distribución homogenea.
                                              #Adicional que los datos se ordenan por dimensión.
        self.raiz.hijo_izq = self.construir_arbol(datos[:len(datos)//2], profundidad + 1) #Se construye el arbol por la izquierda.
        self.raiz.hijo_der = self.construir_arbol(datos[len(datos)//2 + 1:], profundidad + 1) #Se construye el arbol por la derecha.

    def construir_arbol(self, datos, profundidad):
        """
        datos= Un iterable (lista) con las cordenadas para construir el árbol.
        """
        if not datos:
            return None

        puntos = datos.copy()
        parametro = profundidad%len(datos[0])

        puntos = sorted(puntos, key=  lambda d : d[parametro] )
        nodo = Nodo(puntos[len(puntos)//2])
        nodo.hijo_izq = self.construir_arbol(puntos[:len(puntos)//2], profundidad +1) #Se sigue construyendo de forma recursiva.
        nodo.hijo_der = self.construir_arbol(puntos[len(puntos)//2 + 1:], profundidad +1) #Se sigue construyendo de forma recursiva.
        return nodo

    def buscar_vecino(self, objetivo):
        """
        objetivo =  una cordenada para realizar la busqueda.
        ____

        Este metodo hace uso de la estrategia de esclavo maestro, esto con el fin de evitar complicaciones innecesarias en la recursividad.
        """
        resultado = self.buscar_vecino_(objetivo, m_candidato=self.raiz, profundidad=0) 
        return resultado.bordes if resultado else None



    def buscar_vecino_(self, objetivo, m_candidato, profundidad = 0):
        """
        objetivo =  una cordenada para realizar la busqueda.
        m_candidato = Un nodo del árbol candidato a ser el vecino más cercano al objetivo.
        profundidad = La profundidad de la busqueda (se utiliza para realizar las comparaciones por dimensión)
        ____
        Este seria el metodo esclavo para buscar el nodo más cercano, se encarga de bajar por los punteros ( hijos) del árbol y 
        """

        if m_candidato is None:
            return None

        parametro_busqueda = profundidad%len(objetivo)

        if m_candidato.bordes[parametro_busqueda] <= objetivo[parametro_busqueda]:
            candidato = self.buscar_vecino_(objetivo, m_candidato=m_candidato.hijo_der, profundidad= profundidad + 1)
        else:
            candidato = self.buscar_vecino_(objetivo, m_candidato=m_candidato.hijo_izq, profundidad= profundidad + 1)

        if candidato is not None:
            distancia_m_candidato = ((objetivo[0]-m_candidato.bordes[0])**2+(objetivo[1]-m_candidato.bordes[1])**2)
            distancia_candidato = ((objetivo[0]-candidato.bordes[0])**2+(objetivo[1]-candidato.bordes[1])**2)
            if distancia_candidato < distancia_m_candidato:
                mejor = candidato
            else:
                mejor = m_candidato
        else:
            mejor = m_candidato
        """En algunos casos especificos este metodo se puede equivocar, ya que si el objetivo tiene un padre/camino que se descarta por la distancia 
        se llegará a uno cercano pero no el "más" cercano."""
        return mejor 


    def encontrar_radio(self,centro, radio):
        
        resultados = self.encontrar_radio_(self.raiz, centro, radio)
        return resultados

    
    def encontrar_radio_(self,raiz, centro, radio, profundidad = 0, encontrados = None):
        if encontrados is None:
            encontrados = []

        if raiz is None:
            return encontrados

        parametro = profundidad % len(raiz.bordes)
        distancia = ((raiz.bordes[0] - centro[0])**2 + (raiz.bordes[1] - centro[1])**2)**(1/2)

        if distancia <= (radio):
            encontrados.append(raiz.bordes)

        diferencia = centro[parametro] - raiz.bordes[parametro]
        if diferencia < 0:
            rama_cercana = raiz.hijo_izq
            rama_lejana = raiz.hijo_der
        else:
            rama_cercana = raiz.hijo_der
            rama_lejana = raiz.hijo_izq

        self.encontrar_radio_(rama_cercana, centro, radio, profundidad+1, encontrados)

        if abs(diferencia) <= radio:
            self.encontrar_radio_(rama_lejana, centro, radio, profundidad+1, encontrados)
        
        return encontrados
