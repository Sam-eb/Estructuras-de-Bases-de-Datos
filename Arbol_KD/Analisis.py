import time
import random
from Arbol_KD import Arbol_KD
from Test import fuerza_bruta_radio, fuerza_bruta_vecino, generar_datos

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
        arbol = Arbol_KD(datos[i])
        objetivos = random.sample(datos[i], 3)
        

        for j in range(len(objetivos)):

            inicio = time.time()
            arbol.buscar_vecino(objetivos[j])
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
        arbol = Arbol_KD(datos[i])
        centros = random.sample(datos[i], 3)

        for j in range(len(centros)):

            inicio = time.time()
            arbol.encontrar_radio(centros[j],radios[i])
            fin = time.time()
            promedios_arbol[i] += fin-inicio

            inicio = time.time()
            fuerza_bruta_radio(radios[i],centros[j],datos[i])
            fin = time.time()
            promedios_fuerza_b[i] += fin-inicio

        promedios_arbol[i] = promedios_arbol[i]/len(centros)
        promedios_fuerza_b[i] = promedios_fuerza_b[i]/len(centros)
    
    return promedios_arbol, promedios_fuerza_b


print("Se inicia la prueba para vecinos cercanos, en la cual se realizan 5 pruebas con 3 objetivos distintos y con distintos datos entre pruebas, cada conjunto")
print("con un tamaño distinto.")
tamannos = [100,500,1000,5000,10000]
tiempos_arbol, tiempos_fuerza_bruta = comparacion_vecino()
for i in range(5):
    print(f"Prueba {i}: Con tamaño de {tamannos[i]} datos:")
    print(f"Tiempo Arbol: {tiempos_arbol[i]:<15.6f}")
    print(f"Tiempo Fuerza Bruta: {tiempos_fuerza_bruta[i]:<15.6f}")
    print("")


print("Se inicia la prueba para busqueda por radio, en la cual se realizan 5 pruebas con 3 centros distintos y con distintos datos entre pruebas, cada conjunto")
print("con un radio distinto.")
radios = [500,1000,2000,5000,7000]
tiempos_arbol, tiempos_fuerza_bruta = comparacion_radio()
for i in range(5):
    print(f"Prueba {i}: Con radio de tamaño: {radios[i]}")
    print(f"Tiempo Arbol: {tiempos_arbol[i]:<15.6f}")
    print(f"Tiempo Fuerza Bruta: {tiempos_fuerza_bruta[i]:<15.6f}")
    print("")
