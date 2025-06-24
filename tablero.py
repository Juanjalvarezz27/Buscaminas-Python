import os 
import random 
from casillas import CasillaConMina, CasillaSinMina 

# Esta clase representa el tablero del juego
class Tablero:
    def __init__(self, filas, columnas, minas):
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        # Creamos la matriz vacía del tablero
        self.grid = [[None for _ in range(columnas)] for _ in range(filas)]
        self.juego_terminado = False  # Se vuelve True si se gana o se pisa una mina
        self.perdio = False  # Se vuelve True solo si se pisa una mina

    def generar_tablero(self):
        posiciones = [(x, y) for x in range(self.filas) for y in range(self.columnas)]
        # Elegimos aleatoriamente las posiciones donde irán las minas
        minas_colocadas = random.sample(posiciones, self.minas)

        # Recorremos todas las casillas del tablero
        for x in range(self.filas):
            for y in range(self.columnas):
                # Si la posición está en la lista de minas, colocamos una mina
                if (x, y) in minas_colocadas:
                    self.grid[x][y] = CasillaConMina()
                else:
                    self.grid[x][y] = CasillaSinMina()

        # Calculamos cuántas minas hay alrededor de cada casilla sin mina
        for x in range(self.filas):
            for y in range(self.columnas):
                if isinstance(self.grid[x][y], CasillaSinMina):
                    self.grid[x][y].minas_cercanas = self.contar_minas_alrededor(x, y)

    def contar_minas_alrededor(self, x, y):
        # Cuenta las minas alrededor de una casilla
        contador = 0
        for dx in range(-1, 2):  # -1, 0, 1
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy  
                if 0 <= nx < self.filas and 0 <= ny < self.columnas:
                    if isinstance(self.grid[nx][ny], CasillaConMina):
                        contador += 1
        return contador

    def revelar(self, x, y):
        # Revela una casilla del tablero
        if not (0 <= x < self.filas and 0 <= y < self.columnas):
            print("Coordenadas fuera de rango.")
            return

        casilla = self.grid[x][y]

        if casilla.revelada:
            print("Casilla ya revelada.")
            return

        casilla.revelar()

        # Si era una mina, el jugador pierde
        if isinstance(casilla, CasillaConMina):
            self.perdio = True
            self.juego_terminado = True

        # Si no tiene minas alrededor, revelamos automáticamente sus vecinas
        elif isinstance(casilla, CasillaSinMina) and casilla.minas_cercanas == 0:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.filas and 0 <= ny < self.columnas:
                        vecino = self.grid[nx][ny]
                        if not vecino.revelada:
                            self.revelar(nx, ny)

    def marcar(self, x, y):
        # Marca o desmarca una casilla como posible mina
        if not (0 <= x < self.filas and 0 <= y < self.columnas):
            print("Coordenadas fuera de rango.")
            return
        self.grid[x][y].marcar()

    def mostrar(self, revelar_todo=False):
        # Limpia la consola para que se vea solo el tablero actualizado
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Imprimimos los números de columna como encabezado
        encabezado = "    " + "".join([f"{i:^3}" for i in range(self.columnas)])
        print(encabezado)

        # Mostramos cada fila del tablero
        for i, fila in enumerate(self.grid):
            fila_str = f"{i:2}  " + "".join([f"{casilla.mostrar(revelar_todo):^3}" for casilla in fila])
            print(fila_str)

    def verificar_victoria(self):
        # Verifica si el jugador ya ganó (todas las casillas sin mina están reveladas)
        for fila in self.grid:
            for casilla in fila:
                if not isinstance(casilla, CasillaConMina) and not casilla.revelada:
                    return False
        self.juego_terminado = True
        return True
