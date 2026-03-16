"Codigo Co-Creado con Herramientas de Inteligencia Artificial."

import json

class Lista:
        
    def leer_estudiantes(archivo="estudiantes.txt"):
        with open(archivo, "r", encoding="utf-8") as f:
            estudiantes = json.load(f)
        print(f" {len(estudiantes)} estudiantes leídos desde '{archivo}'")
        return estudiantes


    def agregar_estudiante(estudiantes, id, nombre, promedio):
        if any(e["id"] == id for e in estudiantes):
            print(f" Ya existe un estudiante con el ID {id}")
            return estudiantes

        nuevo = {"id": id, "nombre": nombre, "promedio": promedio}
        estudiantes.append(nuevo)
        print(f" Estudiante agregado: {nuevo}")
        return estudiantes

    def eliminar_estudiante(estudiantes, id):
        for i, estudiante in enumerate(estudiantes):
            if estudiante["id"] == id:
                estudiantes.pop(i)
                print(f" Estudiante con ID {id} eliminado")
                return estudiantes

        print(f" No se encontró un estudiante con el ID {id}")
        return estudiantes

    def consultar_estudiante(estudiantes, id):
        resultado = next((e for e in estudiantes if e["id"] == id), None)
        if resultado:
            print(f" Estudiante encontrado: {resultado}")
        else:
            print(f" No se encontró un estudiante con el ID {id}")
        return resultado

    def listar_estudiantes(estudiantes):
        ordenados = sorted(estudiantes, key=lambda e: e["id"])
        return ordenados


    def buscar_en_lista(estudiantes, id):
            for estudiante in estudiantes:
                if estudiante["id"] == id:
                    return estudiante
            return None
    
    def buscar_rango(rango, estudiantes):
        resultado = []
        for estudiante in estudiantes:
            if rango[0]  <= estudiante["id"] <= rango[1]:
                resultado.append(estudiante)

        return resultado
                

