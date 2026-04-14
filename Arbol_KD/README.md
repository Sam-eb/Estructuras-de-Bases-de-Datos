Se encuentran los archivos respectivos para Generar un arbol KD y una prueba para verificar el arbol, esto con el objetivo de solucionar el laboratorio 2.

# Laboratorio 2: Arboles KD
Durante el laboratorio se desarrollo la actividad comparativa del arbol KD y la fuerza bruta para realizar diversas busquedas.

# Definición de pruebas:
Estas busquedas se basaron en 2 tipos, vecino más cercanos y busqueda por radio.
Para ambas busquedas se realizaron 5 escenarios, estos variando el tamaño de los datos y en el caso del segundo tipo de busqueda variando tambien el radio,
en cada escenario se realizan 3 pruebas, en la busqueda del vecino se cambia el vecino y en el caso del radio se cambia el centro.
Luego estos 3 tiempos se promedian dando el resultado de cada algoritmo en los distintos escenarios.

# Analisis

Con estas busquedas se denoto lo siguiente:
En todos los escenarios de la busqueda de vecinos cercanos se identificó un tiempo sobresaliente en el arbol KD, teniendo tiempos como:

Prueba 1: Con tamaño de 100 datos:
Tiempo Arbol: 0.000008       
Tiempo Fuerza Bruta: 0.000022       
El arbol es 2.8181818181818183 veces más rapido

Prueba 2: Con tamaño de 500 datos:
Tiempo Arbol: 0.000005       
Tiempo Fuerza Bruta: 0.000106       
El arbol es 19.391304347826086 veces más rapido

Prueba 3: Con tamaño de 1000 datos:
Tiempo Arbol: 0.000006       
Tiempo Fuerza Bruta: 0.000214       
El arbol es 34.97402597402597 veces más rapido

Prueba 4: Con tamaño de 5000 datos:
Tiempo Arbol: 0.000019       
Tiempo Fuerza Bruta: 0.001235       
El arbol es 63.97530864197531 veces más rapido

Prueba 5: Con tamaño de 10000 datos:
Tiempo Arbol: 0.000009       
Tiempo Fuerza Bruta: 0.002076       
El arbol es 235.2972972972973 veces más rapido

(Tiempos conseguidos en una de las comparaciones)
Como se puede observar el tiempo del arbol KD es muy superior en todos los tamaños.
Claro adicional a este ejemplo se realizaron distintas pruebas y en todos los casos el arbol KD tenia un mejor rendimiento.

En este otro ejemplo se muestra un ejemplo de tiempos en la busqueda por radio:

Prueba 1: Con radio de tamaño: 500
Tiempo Arbol: 0.000011       
Tiempo Fuerza Bruta: 0.000025       
El arbol es 2.2554744525547448 veces más rapido

Prueba 2: Con radio de tamaño: 1000
Tiempo Arbol: 0.000010       
Tiempo Fuerza Bruta: 0.000115       
El arbol es 11.5 veces más rapido

Prueba 3: Con radio de tamaño: 2000
Tiempo Arbol: 0.000023       
Tiempo Fuerza Bruta: 0.000235       
El arbol es 10.385964912280702 veces más rapido

Prueba 4: Con radio de tamaño: 5000
Tiempo Arbol: 0.000149       
Tiempo Fuerza Bruta: 0.001167       
El arbol es 7.830490405117271 veces más rapido

Prueba 5: Con radio de tamaño: 7000
Tiempo Arbol: 0.000813       
Tiempo Fuerza Bruta: 0.002558       
El arbol es 3.1460267813507965 veces más rapido

Así sea de menor magnitud se evidencia que el arbol KD es mejor, llegando a ser 11 veces más rapido que la fuerza bruta.
