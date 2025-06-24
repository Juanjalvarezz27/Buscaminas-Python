class Jugador:
    
    def __init__(self):
        # Al crear un jugador, le pedimos su nombre por consola
        self.nombre = input("Ingrese su nombre: ")

    def pedir_accion(self):
        # Esta función le pide al jugador qué acción desea hacer y en qué casilla
        while True:
            entrada = input("Acción (R para revelar, M para marcar) seguido de coordenadas x y separadas por espacios: ").upper()
            partes = entrada.strip().split()

            # Validamos que haya exactamente 3 partes: acción, x, y
            if len(partes) != 3:
                print("Entrada inválida. Intente de nuevo.")
                continue

            accion, x, y = partes

            # Validamos que la acción sea R o M
            if accion not in ["R", "M"]:
                print("Acción inválida.")
                continue

            try:
                # Convertimos las coordenadas a números
                x = int(x)
                y = int(y)
                return accion, x, y
            except ValueError:
                # Si no se puede convertir a número, mostramos error
                print("Coordenadas inválidas.")
