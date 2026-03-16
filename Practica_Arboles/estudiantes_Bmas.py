"Codigo Co-Creado con Herramientas de Inteligencia Artificial."
import json


# ── Nodo del árbol B+ ─────────────────────────────────────
class NodoHoja:
    __slots__ = ["claves", "datos", "siguiente", "anterior"]
    def __init__(self):
        self.claves    = []       # IDs
        self.datos     = []       # estudiantes (SOLO en hojas)
        self.siguiente = None     # puntero a la hoja derecha
        self.anterior  = None     # puntero a la hoja izquierda

class NodoInterno:
    __slots__ = ["claves", "hijos"]
    def __init__(self):
        self.claves = []          # solo referencias/guías para bajar
        self.hijos  = []          # punteros a hijos (internos u hojas)

class ArbolBMas:
    def __init__(self, orden=50):
        self.raiz       = NodoHoja()   # árbol vacío empieza con una hoja
        self.orden      = orden
        self.max_claves = orden - 1
        self.mid        = orden // 2

    # ── Insertar ─────────────────────────────────────────
    def insertar(self, estudiante):
        id = estudiante["id"]
        resultado = self._insertar(self.raiz, id, estudiante)

        # Si la raíz se dividió, crear nueva raíz interna
        if resultado:
            clave_subir, nodo_derecho = resultado
            nueva_raiz         = NodoInterno()
            nueva_raiz.claves  = [clave_subir]
            nueva_raiz.hijos   = [self.raiz, nodo_derecho]
            self.raiz          = nueva_raiz

    def _insertar(self, nodo, id, estudiante):
        # ── Caso hoja: insertar aquí ──────────────────────
        if isinstance(nodo, NodoHoja):
            lo, hi = 0, len(nodo.claves)
            while lo < hi:
                mid = (lo + hi) // 2
                if nodo.claves[mid] < id: 
                    lo = mid + 1
                else: hi = mid

            if lo < len(nodo.claves) and nodo.claves[lo] == id:
                return None  # duplicado

            nodo.claves.insert(lo, id)
            nodo.datos.insert(lo, estudiante)

            # Dividir si está llena
            if len(nodo.claves) > self.max_claves:
                return self._dividir_hoja(nodo)
            return None

        # ── Caso nodo interno: bajar al hijo correcto ─────
        lo, hi = 0, len(nodo.claves)
        while lo < hi:
            mid = (lo + hi) // 2
            if nodo.claves[mid] <= id: lo = mid + 1
            else: hi = mid
        i = lo

        resultado = self._insertar(nodo.hijos[i], id, estudiante)

        # Si el hijo se dividió, insertar la clave que sube
        if resultado:
            clave_subir, nodo_derecho = resultado
            nodo.claves.insert(i, clave_subir)
            nodo.hijos.insert(i + 1, nodo_derecho)

            # Dividir si está lleno
            if len(nodo.claves) > self.max_claves:
                return self._dividir_interno(nodo)
        return None

    def _dividir_hoja(self, hoja):
        mid        = self.mid
        nueva_hoja = NodoHoja()

        # La nueva hoja toma la mitad derecha
        nueva_hoja.claves = hoja.claves[mid:]
        nueva_hoja.datos  = hoja.datos[mid:]
        hoja.claves       = hoja.claves[:mid]
        hoja.datos        = hoja.datos[:mid]

        # ── Actualizar punteros entre hojas ──────────────
        nueva_hoja.siguiente = hoja.siguiente
        nueva_hoja.anterior  = hoja
        if hoja.siguiente:
            hoja.siguiente.anterior = nueva_hoja
        hoja.siguiente = nueva_hoja

        # La clave que sube al padre es la primera de la nueva hoja
        return (nueva_hoja.claves[0], nueva_hoja)

    def _dividir_interno(self, nodo):
        mid      = self.mid
        nuevo    = NodoInterno()
        clave_subir = nodo.claves[mid]   # esta clave SUBE, no se copia

        # El nodo nuevo toma la mitad derecha (sin la clave del medio)
        nuevo.claves = nodo.claves[mid + 1:]
        nuevo.hijos  = nodo.hijos[mid + 1:]
        nodo.claves  = nodo.claves[:mid]
        nodo.hijos   = nodo.hijos[:mid + 1]

        return (clave_subir, nuevo)

    # ── Buscar ───────────────────────────────────────────
    def buscar(self, id, silencioso=False):
        # Bajar por nodos internos hasta llegar a una hoja
        nodo = self.raiz
        while isinstance(nodo, NodoInterno):
            lo, hi = 0, len(nodo.claves)
            while lo < hi:
                mid = (lo + hi) // 2
                if nodo.claves[mid] <= id: lo = mid + 1
                else: hi = mid
            nodo = nodo.hijos[lo]

        # Buscar en la hoja
        lo, hi = 0, len(nodo.claves)
        while lo < hi:
            mid = (lo + hi) // 2
            if nodo.claves[mid] < id: lo = mid + 1
            else: hi = mid

        if lo < len(nodo.claves) and nodo.claves[lo] == id:
            if silencioso:
                print(f"🔍 Estudiante encontrado: {nodo.datos[lo]}")
            return nodo.datos[lo]

        if silencioso:
            print(f"❌ No se encontró un estudiante con el ID {id}")
        return None

    # ── Eliminar ─────────────────────────────────────────
    def eliminar(self, id):
        nodo = self.raiz
        while isinstance(nodo, NodoInterno):
            lo, hi = 0, len(nodo.claves)
            while lo < hi:
                mid = (lo + hi) // 2
                if nodo.claves[mid] <= id: lo = mid + 1
                else: hi = mid
            nodo = nodo.hijos[lo]

        lo, hi = 0, len(nodo.claves)
        while lo < hi:
            mid = (lo + hi) // 2
            if nodo.claves[mid] < id: lo = mid + 1
            else: hi = mid

        if lo < len(nodo.claves) and nodo.claves[lo] == id:
            nodo.claves.pop(lo)
            nodo.datos.pop(lo)
            print(f"✅ Estudiante con ID {id} eliminado")
        else:
            print(f"❌ No se encontró un estudiante con el ID {id}")

    # ── Listar (recorre punteros entre hojas) ─────────────
    def buscar_rango(self, min, max):
        resultado = []
        # Bajar hasta la primera hoja por la izquierda
        nodo = self.raiz
        while isinstance(nodo, NodoInterno):
            nodo = nodo.hijos[0]
        resultado = self._buscar_rango(min, max, resultado, nodo)
        return resultado

    def _buscar_rango(self, min,max, resultado, nodo):
        while nodo:
            if min > nodo.claves[len(nodo.claves)-1]:
                return self._buscar_rango(min, max, resultado, nodo.siguiente)
            if max < nodo.claves[0]:
                return resultado
            for d in nodo.datos:
                if min <= d["id"] <= max:
                    resultado.append(d)
            nodo = nodo.siguiente


    # ── Agregar ──────────────────────────────────────────
    def agregar(self, id, nombre, promedio):
        self.insertar({"id": id, "nombre": nombre, "promedio": promedio})
        print(f"✅ Estudiante agregado: ID={id}, Nombre={nombre}, Promedio={promedio}")


    def leer(self, archivo="estudiantes_bmas.txt"):
        with open(archivo, "r", encoding="utf-8") as f:
            estudiantes = json.load(f)
        for e in estudiantes:
            self.insertar(e)
        print(f"✅ {len(estudiantes)} estudiantes cargados en el árbol B+")



