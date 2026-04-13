class Nodo:
    def __init__(self, b_x,_b_y):
        self.b_x = b_x
        self.b_y = b_y
        self.valor = []
        self.hij_izq = None
        self.hij_der = None
    
    def agregar_valores(self, valores):
        self.valor.append(valores)
class Arbol_KD:

    def __init__(self, datos):
        import statistics
        """
        datos= Un iterable (lista) de tuplas ordenadas."""
        
        datos = sorted(datos, key= order_x)
        self.raiz = Nodo(datos[len(datos)//2 -1][0],datos[len(datos)//2 -1][0])
        self.agregar_valores(self.raiz, datos)
        
        self.contruir_arbol(datos)               

    def construir_arbol(self, datos):
        """
        datos= Un iterable (lista) de tuplas ordenadas.
        """
        eje = self.raiz
        nivel = 0
        datos = sorted(datos, key = order_y)
        cen_izq, cen_der = datos[:len(datos)//2][len(datos)//4-1],datos[len(datos)//2:][len(datos)//4-1]
        eje.hijo_izq = Nodo(cen_izq[0],cen_izq[1])
        eje.hijo_izq = Nodo(cen_der[0],cen_der[1])
        self.construir_arbol_(eje.hij_izq, datos[:len(datos)], nivel + 1)
        self.construir_arbol_(eje.hij_der, datos[len(datos)], nivel + 1)
        
    def construir_arbol_(datos, eje, nivel):
        match nivel:
            case 0:
                cen_izq, cen_der = datos[:len(datos)//2][len(datos)//4-1],datos[len(datos)//2:][len(datos)//4-1]
                self.construir_arbol_(,,nivel+1)
            case 1:
                cen_izq, cen_der = datos[:len(datos)//2][len(datos)//4-1],datos[len(datos)//2:][len(datos)//4-1]
                self.construir_arbol_(,,nivel-1)
        
    def order_x(dato):
            return dato[0]
    
    def order_y(dato):
            return dato[1]
     
    def agregar_valores(self, punto, datos):
        median = len(datos//2)
        dato_l = datos[len(datos//2)]
        dato_h = datos[len(datos//2)+1]
        cont= 0
        while punto.b_x == dato_l[0] or punto.b_y == dato_h[0]:
            if punto == dato_l[0]:
                punto.agregar_valores(dato_l)
                    datos.remove(dato_l)
                    dato_l = datos(median-cont)                
            if punto.b_x == dato_h[0]:
                    punto.agregar_valores(dato_h)
                    datos.remove(dato_h)
                    dato_h = datos(median+cont)    
            cont += 1
