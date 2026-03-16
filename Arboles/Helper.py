import random
import json

class generar_estudiantes:
    def generar_estudiantes():
        nombres = [
            "Ana", "Carlos", "María", "José", "Laura", "Pedro", "Sofía", "Diego",
            "Valentina", "Andrés", "Camila", "Juan", "Isabella", "Miguel", "Lucía",
            "Santiago", "Gabriela", "Daniel", "Mariana", "Sebastián", "Michel", "Charlie kirk", "Alvaro Uribe velez",
            "Petro", "Lady Gaga", "Cerati","Edison","Samuel"
        ]
        ids = random.sample(range(1000, 99999), 10000)
        return [
            {"id": ids[i], "nombre": random.choice(nombres), "promedio": round(random.uniform(0, 10), 1)}
            for i in range(10000)
        ]

    # ── Archivo ──────────────────────────────────────────
    def escribir(estudiantes, archivo="estudiantes.txt"):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(estudiantes, f, ensure_ascii=False, separators=(",", ":"))
        print(f"✅ {len(estudiantes)} estudiantes guardados en '{archivo}'")
