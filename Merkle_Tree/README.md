En esta carpeta se encuentra el codigo para generar un Arbol de Merklee con el cual se arma "de abajo hacia arriba" utilizando los 
hashes de los archivos que se encuentran en sus hojas, el proceso concatena los hashes de hojas "hermanas" y luego realiza la misma 
operación hash (en este caso SHA 256) e itera hasta llegar a la raiz.
