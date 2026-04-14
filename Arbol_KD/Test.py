import random
import matplotlib.pyplot as plt
from Arbol_KD import Arbol_KD, Nodo 
"""
A continuación se desarrollan las funciones necesarias para graficar el resultado obtenido por el arbol
"""
def graficar_vecino(datos,punto_busqueda, punto_resultado, min, max):
    """
    datos= Los datos utilizados en la prueba, debe de ser un iterable.
    punto_busqueda = El punto objetivo de la busqueda, con este podemos verificar si el punto más cercano efectivamente 
    es el más cercano. Este se colorea distinto.
    punto_resultado: El punto retornado por el arbol.Este se marca de color distinto.
    min = El valor minimo que pueden tomar los datos. Usado para establecer los límites del gráfico.
    max = El valor máximo que pueden tomar los datos. Usado para establecer los límites del gráfico.
    ----
    Este metodo se encarga de graficar los puntos relacionados a los datos generados, cambia el color de un punto en especifico (o mejor dicho, crea 
    un nuevo punto de un color distinto sobre el viejo ), dicho punto es el retornado por el arbol KD al llamar el metodo "buscar_vecino"
    """
    plt.xlim(min, max)
    plt.ylim(min, max)
    xs, ys = zip(*datos)
    plt.scatter(xs, ys, c='steelblue', alpha=0.5, s=20)
    plt.scatter(*punto_busqueda, c='red', s=20, zorder=5)
    plt.scatter(*punto_resultado, c='green', s=20, zorder=5)
    plt.show()

def graficar_radio(datos, punto_centro, radio, puntos_encontrados, min, max):
    """
    datos= Los datos utilizados en la prueba, debe de ser un iterable.
    punto_centro = El centro del radio de busqueda, lo marcamos de otro color para denotarlo con calridad.
    radio: El radio de busqueda.
    puntos_encontrados = Los puntos retornados por el árbol, se les da un color distinto para identificarlos claramente.
    min = El valor minimo que pueden tomar los datos. Usado para establecer los límites del gráfico.
    max = El valor máximo que pueden tomar los datos. Usado para establecer los límites del gráfico.
    -------
    Este metodo se encarga de graficar los datos, un circulo con radio y centro dados y cambiar el color de los puntos retornados por 
    el arbol KD al llamar el metodo "encontrar_radio()".
    """
    plt.xlim(min, max)
    plt.ylim(min, max)
    xs, ys = zip(*datos)
    plt.scatter(xs, ys, c='steelblue', alpha=0.5, s=20)
    
    circulo = plt.Circle(punto_centro, radio, fill=False, color='orange', linewidth=1)
    plt.gca().add_patch(circulo)
    plt.gca().set_aspect('equal')
    
    if puntos_encontrados:
        ex, ey = zip(*puntos_encontrados)
        plt.scatter(ex, ey, c='green', s=20, zorder=5)
    
    plt.scatter(*punto_centro, c='red', s=20, zorder=5)
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
        if (mejor_distancia > ( (dato[0]-objetivo[0])**2 + (dato[0]-objetivo[0])**2 ) **(1/2)):
            vecino_m_cercano = dato
            mejor_distancia = ((dato[0]-objetivo[0])**2+(dato[0]-objetivo[0])**2)**(1/2)

    return vecino_m_cercano

def fuerza_bruta_radio(radio, centro,datos):
    encontrados = []
    for dato in datos:
        if (((dato[0]-centro[0])**2+(dato[0]-centro[0])**2)**(1/2) < radio):
            encontrados.append(dato)
    return encontrados

"""#En este apartado se deja una pequeña prueba realizada.
min = -100
max = 100
cantidad = 100
datos = generar_datos(min,max,cantidad)

arbol = Arbol_KD(datos)

objetivo = random.choice(datos)
objetivo[1] = objetivo[1] + 40
objetivo[0] = objetivo[0] + 40
#Se selecciona un dato cualquiera y se le realiza un pequeño cambio.

graficar_vecino( datos, objetivo,arbol.buscar_vecino(objetivo),min, max)
centro = datos[0]
radio = (100)
graficar_radio(datos,centro,radio,arbol.encontrar_radio(centro,radio), min, max)

#En esta pruebas los datos son arbitrarios y sin intención especifica.

"""
