import time
import random
from Quadtree import Quadtree
from Test import fuerza_bruta_radio, fuerza_bruta_vecino, generar_datos
import matplotlib.pyplot as plt
import numpy as np
 
def graficar_comparacion_vecino(datos_alg1, datos_alg2, tamannos,
                         nombre_alg1='Quadtree', nombre_alg2='Fuerza Bruta',
                         metrica='Tiempo (ms)'):
    x = np.arange(5)
    ancho = 0.35
    etiquetas = [f'n={t}' for t in tamannos]
 
    fig, ax = plt.subplots(figsize=(10, 6))
 
    ax.bar(x - ancho/2, datos_alg1, ancho, label=nombre_alg1, color='steelblue')
    ax.bar(x + ancho/2, datos_alg2, ancho, label=nombre_alg2, color='coral')
 
    ax.set_xlabel('Prueba (tamaño de datos)')
    ax.set_ylabel(metrica)
    ax.set_title(f'Comparación: {nombre_alg1} vs {nombre_alg2}')
    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas)
    ax.legend()
 
    plt.tight_layout()
    plt.show()
 
def graficar_comparacion_radio(datos_alg1, datos_alg2, tamannos,radios,
                         nombre_alg1='Quadtree', nombre_alg2='Fuerza Bruta',
                         metrica='Tiempo (ms)'):
    x = np.arange(5)
    ancho = 0.35
    etiquetas = [f'n={t}\nr={r}' for t, r in zip(tamannos, radios)]
 
    fig, ax = plt.subplots(figsize=(10, 6))
 
    ax.bar(x - ancho/2, datos_alg1, ancho, label=nombre_alg1, color='steelblue')
    ax.bar(x + ancho/2, datos_alg2, ancho, label=nombre_alg2, color='coral')
 
    ax.set_xlabel('Prueba (tamaño de datos)')
    ax.set_ylabel(metrica)
    ax.set_title(f'Comparación: {nombre_alg1} vs {nombre_alg2}')
    ax.set_xticks(x)
    ax.set_xticklabels(etiquetas)
    ax.legend()
 
    plt.tight_layout()
    plt.show()
 


def comparacion_vecino():
    min = -5000
    max = 5000
    tamannos = [100,500,1000,5000,10000]
    datos  = []

    for tamanno in tamannos:
        dato = generar_datos(min, max, tamanno)
        datos.append(dato)
    
    promedios_arbol = [0 for _ in range(len(datos))]
    promedios_fuerza_b = [0 for _ in range(len(datos))]

    for i in range (len(tamannos)):
        arbol = Quadtree(datos[i])
        objetivos = random.sample(datos[i], 3)
        

        for j in range(len(objetivos)):

            inicio = time.time()
            arbol.buscar_cercano(objetivos[j])
            fin = time.time()
            promedios_arbol[i] += fin-inicio

            inicio = time.time()
            fuerza_bruta_vecino(datos[i],objetivos[j])
            fin = time.time()
            promedios_fuerza_b[i] += fin-inicio

        promedios_arbol[i] = promedios_arbol[i]/len(objetivos)
        promedios_fuerza_b[i] = promedios_fuerza_b[i]/len(objetivos)
    
    return promedios_arbol, promedios_fuerza_b


def comparacion_radio():
    min = -5000
    max = 5000
    tamannos = [100,500,1000,5000,10000]
    radios = [50,250,500,1000,2000]
    datos  = []
    for tamanno in tamannos:
        dato = generar_datos(min, max, tamanno)
        datos.append(dato)

    promedios_arbol = [0 for _ in range(len(datos))]
    promedios_fuerza_b = [0 for _ in range(len(datos))]

    for i in range (len(radios)):
        arbol = Quadtree(datos[i])
        centros = random.sample(datos[i], 3)

        for j in range(len(centros)):

            inicio = time.time()
            arbol.buscar_radio(radios[i],centros[j])
            fin = time.time()
            promedios_arbol[i] += fin-inicio

            inicio = time.time()
            fuerza_bruta_radio(radios[i],centros[j],datos[i])
            fin = time.time()
            promedios_fuerza_b[i] += fin-inicio

        promedios_arbol[i] = promedios_arbol[i]/len(centros)
        promedios_fuerza_b[i] = promedios_fuerza_b[i]/len(centros)
    
    return promedios_arbol, promedios_fuerza_b

tamannos = [100,500,1000,5000,10000]
tiempos_arbol, tiempos_fuerza_bruta = comparacion_vecino()
graficar_comparacion_vecino(tiempos_arbol, tiempos_fuerza_bruta, tamannos=tamannos)

radios = [500,1000,2000,5000,7000]
tiempos_arbol, tiempos_fuerza_bruta = comparacion_radio()
graficar_comparacion_radio(tiempos_arbol, tiempos_fuerza_bruta,tamannos, radios)
