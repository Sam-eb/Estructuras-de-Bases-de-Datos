import random
from Quadtree import Quadtree
from matplotlib import patches
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
"""
A continuación se desarrollan las funciones necesarias para graficar el resultado obtenido por el arbol
"""
def graficar_puntos(datos, arbol):
    x = [p[0] for p in datos]
    y = [p[1] for p in datos]

    fig, ax = plt.subplots(figsize=(8, 8))
    dibujar_cuadrantes(arbol, ax)  # <-- agregar esto
    ax.scatter(x, y, s=1, alpha=0.4, color='purple', label='Puntos')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Todos los puntos')
    ax.legend()
    ax.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

COLORES = ['#ffd6d6', '#d6e8ff', '#d6ffd6', '#fff4d6',
           '#f0d6ff', '#d6fff4', '#ffe8d6', '#d6d6ff']

def dibujar_cuadrantes(nodo, ax, nivel=0, max_nivel=8):
    rects = []
    colores = []
    _recolectar_rects(nodo, rects, colores, nivel, max_nivel)
    col = PatchCollection(rects, facecolor=colores, edgecolor='gray', alpha=0.3, linewidth=0.5)
    ax.add_collection(col)

def _recolectar_rects(nodo, rects, colores, nivel, max_nivel):
    if nivel > max_nivel:
        return
    color = COLORES[nivel % len(COLORES)]
    ancho = nodo.maximos[0] - nodo.minimos[0]
    alto  = nodo.maximos[1] - nodo.minimos[1]
    rects.append(patches.Rectangle((nodo.minimos[0], nodo.minimos[1]), ancho, alto))
    colores.append(color)
    if not nodo.soy_hoja():
        for hijo in nodo.hijos:
            _recolectar_rects(hijo, rects, colores, nivel + 1, max_nivel)

def graficar_mas_cercano(datos, objetivo, resultado, arbol):
    x = [p[0] for p in datos]
    y = [p[1] for p in datos]

    fig, ax = plt.subplots(figsize=(8, 8))
    dibujar_cuadrantes(arbol, ax) 

    ax.scatter(x, y, s=1, alpha=0.3, color='purple', label='Puntos')
    ax.scatter(objetivo[0], objetivo[1], s=10, color='red', zorder=5, label=f'Objetivo: {objetivo}')
    ax.scatter(resultado[0], resultado[1], s=10, color='orange', zorder=5, label=f'Más cercano: {resultado}')
    ax.plot([objetivo[0], resultado[0]],
            [objetivo[1], resultado[1]],
            color='orange', linewidth=1, linestyle='--')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Punto más cercano')
    ax.legend(loc='upper right')
    plt.tight_layout()
    plt.show()


def graficar_radio(datos, centro, radio, encontrados, arbol):
    x = [p[0] for p in datos]
    y = [p[1] for p in datos]

    fig, ax = plt.subplots(figsize=(8, 8))
    dibujar_cuadrantes(arbol, ax)  # <-- agregar esto

    ax.scatter(x, y, s=1, alpha=0.3, color='purple', label='Puntos')

    xf = [n[0] for n in encontrados]
    yf = [n[1] for n in encontrados]
    ax.scatter(xf, yf, s=1, color='darkorange', zorder=5, label=f'Encontrados ({len(encontrados)})')
    ax.scatter(centro[0], centro[1], s=80, color='red', zorder=6, label=f'Centro: {centro}')

    circulo = patches.Circle(centro, radio,
                              linewidth=0.5, edgecolor='red',
                              facecolor='none')
    ax.add_patch(circulo)
    ax.set_aspect('equal')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Búsqueda por radio ({radio})')
    ax.legend(loc='upper right')
    plt.tight_layout()
    plt.show()
def generar_datos(min, max, cantidad):
    """
    min = El valor minimo que pueden tomar los datos.
    max = El valor máximo que pueden tomar los datos.
    cantidad = El número de datos a generar.
    ----
    Este metodo usa la librería random para generar los datos usados en las pruebas. Se utiliza el random.uniform para evitar que los datos tengan una forma determinada que pueda
    afectar el desempeño.

    """
    datos = []
    for i in range(cantidad):
        dato = [random.uniform(min, max),random.uniform(min, max)]
        datos.append(dato)
    return datos

def fuerza_bruta_vecino(datos, objetivo):
    vecino_m_cercano = None
    mejor_distancia = 99999999
    for dato in datos:
        if (mejor_distancia > ( (dato[0]-objetivo[0])**2 + (dato[1]-objetivo[1])**2 )):
            vecino_m_cercano = dato
            mejor_distancia = ((dato[0]-objetivo[0])**2+(dato[1]-objetivo[1])**2)

    return vecino_m_cercano

def fuerza_bruta_radio(radio, centro,datos):
    encontrados = []
    for dato in datos:
        if (((dato[0]-centro[0])**2+(dato[1]-centro[1])**2)**(1/2) < radio):
            encontrados.append(dato)
    return encontrados

"""
datos = generar_datos(-1000,1000,600)
Qt = Quadtree(datos)
objetivo = random.choice(datos)
objetivo = [objetivo[0]+20,objetivo[1]+20]

#Esta es una prueba para verificar que si se encuentre el más cercano

#______________________________________________



mejor = fuerza_bruta_vecino(datos, objetivo)
print(Qt.distancia_puntos(objetivo, mejor))
mejor_dist = Qt.distancia_puntos(objetivo, mejor)**(1/2)

print(objetivo)
print("fb",mejor, mejor_dist)
print("qt",Qt.buscar_cercano(objetivo))
mejor, _ = Qt.buscar_cercano(objetivo)
graficar_mas_cercano(datos, objetivo, mejor,Qt.raiz)


radio = 100
encontrados = Qt.buscar_radio(radio, objetivo)
print(fuerza_bruta_radio(radio, objetivo, datos))
print()
print(Qt.buscar_radio(radio, objetivo))

graficar_radio(datos, objetivo, radio, encontrados, Qt.raiz)
"""