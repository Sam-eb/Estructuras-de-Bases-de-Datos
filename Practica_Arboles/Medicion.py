import Helper
import random
import time
from estudiantes_ABB_ import ABB
from estudiantes_Bmas import ArbolBMas
from estudiantes_lista import Lista

num_pruebas = 100
estudiantes = Helper.generar_estudiantes.generar_estudiantes()
Helper.generar_estudiantes.escribir(estudiantes)
arbol_Bmas = ArbolBMas(50)
arbol_Bmas.leer("estudiantes.txt")
raiz = ABB.leer_ABB("estudiantes.txt")

print("▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣ Estudiantes generados ▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣\n")
print(f"Iniciando prueba #1: \nEn esta se generan {num_pruebas} ids de forma aleatoria y se realiza la " \
"busqueda en las 3 estructuras distintas " )

ids = random.sample(range(1000,100000),num_pruebas)
input("")
print("Usando Listas: ")
inicio = time.time()
list = []
for id in ids:
    list.append(Lista.buscar_en_lista(estudiantes, id))
fin = time.time()
print(f"Los 10 primeros son: {list[:10]}")
print(f"Tiempo de busqueda para {num_pruebas} ids: {fin-inicio:.6f}")
input("")

list =[]
print("Usando Arboles ABB: ")
inicio = time.time()

for id in ids:
    list.append(ABB.buscar(raiz,id))

fin = time.time()
print(f"Los 10 primeros son: {list[:10]}")
print(f"Tiempo de busqueda para {num_pruebas} ids: {fin-inicio:.6f}")
input("")

list =[]
print("Usando Arboles B+: ")
inicio = time.time()

for id in ids:
    list.append(arbol_Bmas.buscar(id))

fin = time.time()
print(f"Los 10 primeros son: {list[:10]}")
print(f"Tiempo de busqueda para {num_pruebas} ids: {fin-inicio:.6f}")
input("")

list = []

print("Iniciando prueba #2: \n" \
f"En esta prueba se realizaran consultas por rango, las cuales deben de llegar en orden y cumplir con el rango: ")
rango = (10000, 20000)
print(f"El rango se escoge de manera arbitraria desde {rango[0]} hasta {rango[1]}.")
input("")

print("Usando Listas: ")
inicio = time.time()
list = Lista.buscar_rango(rango, estudiantes)
fin = time. time()
print(f"La longitud de la lista es de: {len(list)}\n")
print(f"Los 10 primeros son: {list[:10]}")
print(f"Tiempo de busqueda para {num_pruebas} ids: {fin-inicio:.6f}")
input("")

list = []
print("Usando Arboles ABB: ")
inicio = time.time()
list = ABB.buscar_orden(raiz, rango)
fin = time.time()
print(f"La longitud de la lista es de: {len(list)}\n")
print(f"Los 10 primeros son: {list[:10]}")
print(f"Tiempo de busqueda para {num_pruebas} ids: {fin-inicio:.6f}")
input("")

list = []
print("Usando Arboles B+: ")
inicio = time.time()
list = arbol_Bmas.buscar_rango(rango[0], rango[1])
fin = time.time()
print(f"La longitud de la lista es de: {len(list)}\n")
print(f"Los 10 primeros son: {list[:10]}")

print(f"Tiempo de busqueda para {num_pruebas} ids: {fin-inicio:.6f}")
input("")






