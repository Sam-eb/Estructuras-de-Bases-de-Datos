"Codigo Co-Creado con Herramientas de Inteligencia Artificial."

import json

# ── Nodo AVL ──────────────────────────────────────────────
class Nodo:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.izquierda = None
        self.derecha = None
        self.altura = 1
class ABB:
    # ── Utilidades AVL ────────────────────────────────────────
    def _altura(nodo):
        return nodo.altura if nodo else 0

    def _balance(nodo):
        return ABB._altura(nodo.izquierda) - ABB._altura(nodo.derecha) if nodo else 0

    def _actualizar_altura(nodo):
        nodo.altura = 1 + max(ABB._altura(nodo.izquierda), ABB._altura(nodo.derecha))

    # ── Rotaciones ────────────────────────────────────────────
    def _rotar_derecha(y):
        x = y.izquierda
        y.izquierda = x.derecha
        x.derecha = y
        ABB._actualizar_altura(y)
        ABB._actualizar_altura(x)
        return x

    def _rotar_izquierda(x):
        y = x.derecha
        x.derecha = y.izquierda
        y.izquierda = x
        ABB._actualizar_altura(x)
        ABB._actualizar_altura(y)
        return y

    def _rebalancear(nodo):
        ABB._actualizar_altura(nodo)
        b = ABB._balance(nodo)

        # Caso izquierda-izquierda
        if b > 1 and ABB._balance(nodo.izquierda) >= 0:
            return ABB._rotar_derecha(nodo)
        # Caso izquierda-derecha
        if b > 1 and ABB._balance(nodo.izquierda) < 0:
            nodo.izquierda = ABB._rotar_izquierda(nodo.izquierda)
            return ABB._rotar_derecha(nodo)
        # Caso derecha-derecha
        if b < -1 and ABB._balance(nodo.derecha) <= 0:
            return ABB._rotar_izquierda(nodo)
        # Caso derecha-izquierda
        if b < -1 and ABB._balance(nodo.derecha) > 0:
            nodo.derecha = ABB._rotar_derecha(nodo.derecha)
            return ABB._rotar_izquierda(nodo)

        return nodo

    # ── Operaciones AVL ───────────────────────────────────────
    def insertar(nodo, estudiante):
        if nodo is None:
            return Nodo(estudiante)
        if estudiante["id"] < nodo.estudiante["id"]:
            nodo.izquierda = ABB.insertar(nodo.izquierda, estudiante)
        elif estudiante["id"] > nodo.estudiante["id"]:
            nodo.derecha = ABB.insertar(nodo.derecha, estudiante)
        else:
            print(f"❌ Ya existe un estudiante con el ID {estudiante['id']}")
            return nodo
        return ABB._rebalancear(nodo)


    def buscar(nodo, id):
        if nodo is None:
            return None
        if id == nodo.estudiante["id"]:
            return nodo.estudiante
        if id < nodo.estudiante["id"]:
            return ABB.buscar(nodo.izquierda, id)
        return ABB.buscar(nodo.derecha, id)
    
    def buscar_orden(nodo, rango):
        resultado = []
        ABB._buscar_orden(nodo, rango, resultado)
        return resultado
    
    def _buscar_orden(nodo, rango, resultado):
        if nodo is None:
            return 
        if rango[0] < nodo.estudiante["id"]:
            ABB._buscar_orden(nodo.izquierda, rango, resultado)
        if rango[0] <= nodo.estudiante["id"] <= rango[1]:
            resultado.append(nodo.estudiante)
        if nodo.estudiante["id"] < rango[1]:
            ABB._buscar_orden(nodo.derecha, rango,resultado)

    def _minimo(nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def eliminar(nodo, id):
        if nodo is None:
            print(f"❌ No se encontró un estudiante con el ID {id}")
            return None
        if id < nodo.estudiante["id"]:
            nodo.izquierda = ABB.eliminar(nodo.izquierda, id)
        elif id > nodo.estudiante["id"]:
            nodo.derecha = ABB.eliminar(nodo.derecha, id)
        else:
            if nodo.izquierda is None:
                print(f"✅ Estudiante con ID {id} eliminado")
                return nodo.derecha
            if nodo.derecha is None:
                print(f"✅ Estudiante con ID {id} eliminado")
                return nodo.izquierda
            sucesor = ABB._minimo(nodo.derecha)
            nodo.estudiante = sucesor.estudiante
            nodo.derecha = ABB.eliminar(nodo.derecha, sucesor.estudiante["id"])
            return ABB._rebalancear(nodo)
        return ABB._rebalancear(nodo)


    def listar(nodo, resultado=None):
        if resultado is None:
            resultado = []
        if nodo is None:
            return resultado
        ABB.listar(nodo.izquierda, resultado)
        resultado.append(nodo.estudiante)
        ABB.listar(nodo.derecha, resultado)
        return resultado



    def leer_ABB(archivo="estudiantes_avl.txt"):
        with open(archivo, "r", encoding="utf-8") as f:
            estudiantes = json.load(f)
        raiz = None
        for e in estudiantes:
            raiz = ABB.insertar(raiz, e)
        print(f"✅ {len(estudiantes)} estudiantes cargados en el árbol de Busqueda Binario.")
        return raiz





# ── Uso ───────────────────────────────────────────────────




# ── Buscar sin imprimir ───────────────────────────────────
def buscar_silencioso(nodo, id):
    if nodo is None:
        return None
    if id == nodo.estudiante["id"]:
        return nodo.estudiante
    if id < nodo.estudiante["id"]:
        return buscar_silencioso(nodo.izquierda, id)
    return buscar_silencioso(nodo.derecha, id)



