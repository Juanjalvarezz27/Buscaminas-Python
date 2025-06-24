import time  
from tablero import Tablero  
from jugador import Jugador  
from config_loader import ConfigLoader  

# Esta clase se encarga de controlar todo el flujo del juego
class Juego:
    def __init__(self):
        self.config = ConfigLoader("records.json")
        # Crea un nuevo jugador
        self.jugador = Jugador()
        # Inicializa el tablero 
        self.tablero = None
        # Aquí guardaremos el tiempo cuando empiece la partida
        self.start_time = None

    def mostrar_menu(self):
        # Menú principal del juego
        while True:
            print("\n==== MENÚ PRINCIPAL ====")
            print("1. Jugar")
            print("2. Ver récords")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            # Según la opción, llama a la función correspondiente
            if opcion == "1":
                self.iniciar()
            elif opcion == "2":
                self.config.mostrar_records()
            elif opcion == "3":
                print("¡Gracias por jugar!")
                break
            else:
                print("Opción no válida.")

    def seleccionar_dificultad(self):
        # Muestra un submenú para que el usuario seleccione la dificultad
        while True:
            print("\nSelecciona dificultad:")
            print("1. Fácil (10%)")
            print("2. Media (30%)")
            print("3. Difícil (60%)")
            print("4. Imposible (80%)")
            opcion = input("Ingrese una opción (1-4): ")

            if opcion in ["1", "2", "3", "4"]:
                return opcion
            else:
                print("Opción no válida. Intenta de nuevo.")

    def iniciar(self):
        dificultad = self.seleccionar_dificultad()
        filas, columnas = 9, 9  

        # Porcentajes de minas según dificultad
        proporciones = {
            "1": 0.1,  # Fácil
            "2": 0.3,  # Media
            "3": 0.6,  # Difícil
            "4": 0.8   # Imposible
        }

        minas = int(filas * columnas * proporciones[dificultad])

        # Creamos el tablero con las configuraciones
        self.tablero = Tablero(filas, columnas, minas)
        self.tablero.generar_tablero()

        # Guardamos el tiempo en que inicia la partida
        self.start_time = time.time()

        mensaje = ""  # Aquí se guarda cualquier mensaje de error o aviso

        # Mientras el juego no haya terminado
        while not self.tablero.juego_terminado:
            self.tablero.mostrar()  # Mostramos el tablero
            if mensaje:
                print(f"\n{mensaje}")  # Si hay mensaje, lo mostramos
                mensaje = ""  

            # Pedimos al jugador una acción
            accion, x, y = self.jugador.pedir_accion()

            # Validamos que las coordenadas estén dentro del tablero
            if not (0 <= x < filas and 0 <= y < columnas):
                mensaje = "❌ Coordenadas fuera del tablero. Intenta de nuevo."
                continue  # Volvemos a mostrar el tablero

            # Si la acción es revelar
            if accion == "R":
                self.tablero.revelar(x, y)
            # Si es marcar
            elif accion == "M":
                self.tablero.marcar(x, y)

            # Verificamos si el jugador ya ganó
            if self.tablero.verificar_victoria():
                self.tablero.mostrar(revelar_todo=True)
                print("🎉 ¡Felicidades! Has ganado.")
                duracion = time.time() - self.start_time
                # Registramos el récord
                self.config.registrar_record(self.jugador.nombre, duracion, filas, columnas)
                break  

        # Si perdió, mostramos el tablero completo con minas reveladas
        if self.tablero.perdio:
            self.tablero.mostrar(revelar_todo=True)
            print("💥 ¡BOOM! Has pisado una mina. Fin del juego.")
