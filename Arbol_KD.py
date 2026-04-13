class Nodo:
    def __init__(self, bordes):
        self.bordes = bordes
        self.hijo_izq = None
        self.hijo_der = None


class Arbol_KD:
    def order(self, dato):
        return dato[self.profundidad%len(dato)]

    def __init__(self, datos):
        """
        datos= Un iterable (lista) de tuplas ordenadas."""
        self.profundidad = 0
        datos = sorted(datos, key= self.order)
        self.raiz = Nodo(datos[len(datos)//2])
        
        self.raiz.hijo_izq = self.construir_arbol(datos[:len(datos)//2], self.profundidad + 1)
        self.raiz.hijo_der = self.construir_arbol(datos[len(datos)//2 + 1:], self.profundidad + 1)               

    def construir_arbol(self, datos, profundidad):
        if not datos:
            return None
        puntos = datos.copy()
        self.profundidad = max(self.profundidad, profundidad)
        puntos = sorted(puntos, key= self.order)
        nodo = Nodo(puntos[len(puntos)//2])
        nodo.hijo_izq = self.construir_arbol(puntos[:len(puntos)//2], profundidad +1)
        nodo.hijo_der = self.construir_arbol(puntos[len(puntos)//2 + 1:], profundidad +1)
        return nodo
        
