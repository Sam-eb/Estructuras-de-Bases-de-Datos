from Arbol_KD import Arbol_KD
import random
numeros = []
for i in range(1000):
    numeros.append(random.randint(-100,100))
datos = []
for i in range(1000):
    cors = [random.choice(numeros),random.choice(numeros)]
    datos.append(cors)

arbol = Arbol_KD(datos)
