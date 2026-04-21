class Nodo:
    def __init__(self,minimos, maximos, hijos = [], dato = None):
        self.minimos = minimos 
        self.maximos = maximos
        self.hijos = hijos
        self.dato = dato

    def soy_hoja(self):
        if len(self.hijos) == 0:
            return True
        return False  
      
    def contiene(self, punto):
        for i in range(len(self.minimos)):
            if punto[i] < self.minimos[i]:
                return False
            if punto[i] >= self.maximos[i]:
                return False
        return True

    def intersecta(self, quad):
        for i in range(len(self.minimos)):
            if quad.minimos[i] < self.maximos[i]:
                return True
            if quad.maximos[i] >= self.maximos[i]:
                return True
        return False

    def insertar(self, punto):
        if not self.contiene(punto):
            return False
        
        if self.soy_hoja() and self.dato == None:
            self.dato = punto
            return True

        if self.soy_hoja():
            self.subdividir()
            for hijo in self.hijos:
                if hijo.insertar(self.dato):
                    break
            self.dato = None

        for hijo in self.hijos:
            if hijo.insertar(punto):
                return True
            
        return False
        
    def subdividir(self):
        mids = [(self.maximos[i]+self.minimos[i])/2 for i in range(len(self.minimos))]
        self.hijos = [
            Nodo(self.minimos, mids),
            Nodo(mids, self.maximos),
            Nodo([mids[0],self.minimos[1]],[self.maximos[0], mids[1]]),
            Nodo([self.minimos[0],mids[1]],[mids[0],self.maximos[1]])
        ]



class Quadtree:

    def __init__(self, datos):
        maximos = [0 for i in range(len(datos[0]))]
        minimos = [9999999 for i in range(len(datos[0]))]
        for i in range(len(datos)):
            for j in range(len(datos[0])):
                if datos[i][j] < minimos[j]:
                    minimos [j] = datos[i][j]
                if datos[i][j] > maximos[j]:
                    maximos [j] = datos[i][j]
        for i in range(len(minimos)):
            minimos[i] = minimos[i] - 1
            maximos[i] = maximos[i ] +1 
        
        self.raiz = Nodo(minimos, maximos)
        self.construir_arbol(datos)


    def construir_arbol(self,datos):
        for dato in datos:
            self.raiz.insertar(dato)

    def buscar_cercano(self, punto):
        resultado,distancia = self._buscar_cercano(punto, self.raiz)
        return resultado, (distancia)**(1/2)
    
    def _buscar_cercano(self, objetivo,raiz = Nodo, mejor = None, mejor_dist = float("inf")):

        if raiz.soy_hoja():
            if raiz.dato is not None:
                return raiz.dato, self.distancia_puntos(raiz.dato, objetivo)
            return None, float("inf")
        
        no_contiene = []
        for hijo in raiz.hijos:
            if hijo.contiene(objetivo):
                candidato, distancia = self._buscar_cercano(objetivo, hijo, mejor, mejor_dist)
                if distancia < mejor_dist:
                    #En el caso de que un cuadrante tenga la misma distancia que la mejor, puede existir un error
                    #pero se prefiere sacrificar esos pocos casos.
                    mejor, mejor_dist = candidato, distancia
            else:
                no_contiene.append(hijo)
        
        for nodo in no_contiene:
            if self.distancia_limites(nodo, objetivo) < mejor_dist:
                candidato, distancia = self._buscar_cercano(objetivo, nodo, mejor, mejor_dist)
                if distancia < mejor_dist:
                            mejor, mejor_dist = candidato, distancia
        
        
        return mejor, mejor_dist

    def buscar_radio(self,radio, centro):
        resultados = self._buscar_radio(self.raiz, radio, centro)
        return resultados     
    
    def _buscar_radio(self, raiz, radio, centro):
        encontrados = []
        for hijo in raiz.hijos:
            if self.distancia_limites(hijo, centro) < radio**2:
                if hijo.soy_hoja():
                    if hijo.dato is not None:
                        distancia = self.distancia_puntos(centro, hijo.dato)
                        if distancia < radio**2:
                            encontrados.append(hijo.dato)
                else:
                        encontrados += self._buscar_radio(hijo, radio, centro)
        return encontrados
                
    def distancia_puntos(self, puntoa, puntob):
        distancia = 0
        for i in range (len(puntoa)):
            distancia += (puntoa[i] - puntob[i])**2
        return distancia
    
    def distancia_limites(self, limites, punto):
        mas_izquierda = min(punto[0], limites.maximos[0])
        mas_abajo = min(punto[1], limites.maximos[1])
        mas_cerca_x = max(limites.minimos[0], mas_izquierda)
        mas_cerca_y = max(limites.minimos[1], mas_abajo)
        return self.distancia_puntos(punto, [mas_cerca_x, mas_cerca_y])

    
        


