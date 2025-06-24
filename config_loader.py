import json 

# Esta clase se encarga de leer y guardar los mejores tiempos (récords)
class ConfigLoader:
    def __init__(self, archivo="records.json"):
        # Guardamos el nombre del archivo donde están los récords
        self.archivo = archivo

    def mostrar_records(self):
        # Muestra por consola la lista de los 3 mejores tiempos guardados
        print("\n=== Mejores Tiempos ===")
        try:
            with open(self.archivo, "r") as f:
                records = json.load(f) 
                for record in records:
                    # Mostramos nombre, apellido y tiempo
                    print(f"{record['first_name']} {record['last_name']} - {record['time']}s")
        except FileNotFoundError:
            # Si no existe el archivo, informamos que no hay récords
            print("No hay récords aún.")

    def registrar_record(self, nombre, tiempo, filas, columnas):
        # Esta función guarda un nuevo récord si el jugador gana
        try:
            with open(self.archivo, "r") as f:
                records = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            records = []

        # Dividimos el nombre completo en nombre y apellido
        first, *last_parts = nombre.split()
        last = " ".join(last_parts) if last_parts else "(Sin apellido)"

        # Creamos el nuevo récord como un diccionario
        nuevo_record = {
            "first_name": first,
            "last_name": last,
            "time": round(tiempo, 2)  
        }

        # Agregamos el nuevo récord a la lista
        records.append(nuevo_record)

        # Ordenamos la lista por el tiempo (de menor a mayor)
        records.sort(key=lambda x: x["time"])

        # Nos quedamos solo con los 3 mejores
        records = records[:3]

        # Guardamos nuevamente en el archivo los mejores récords
        with open(self.archivo, "w") as f:
            json.dump(records, f, indent=2) 
