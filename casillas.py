from abc import ABC, abstractmethod 

# Clase base para todas las casillas
class Casilla(ABC):
    def __init__(self):
        self.revelada = False     # Indica si la casilla ya fue descubierta
        self.marcada = None       # Puede ser '!' o '?', si el jugador la marcó

    @abstractmethod
    def revelar(self):
        pass

    def marcar(self):
        # Permite al jugador marcar una casilla que aún no ha sido revelada
        if self.revelada:
            print("No se puede marcar una casilla revelada.")
            return
        # Ciclo de marcas: nada → '!' → '?' → nada
        if self.marcada is None:
            self.marcada = '!'
        elif self.marcada == '!':
            self.marcada = '?'
        else:
            self.marcada = None

    def mostrar(self, revelar_todo=False):
        # Devuelve lo que se va a mostrar en el tablero
        if revelar_todo or self.revelada:
            return self._mostrar_revelada()
        # Si está marcada, muestra la marca
        elif self.marcada:
            return self.marcada
        # Si está oculta y sin marcar, se muestra como cuadrado lleno
        else:
            return "■"

    @abstractmethod
    def _mostrar_revelada(self):
        pass

# Clase para una casilla que tiene una mina
class CasillaConMina(Casilla):
    def revelar(self):
        # Al revelar esta casilla se activa la mina
        self.revelada = True

    def _mostrar_revelada(self):
        # Representamos la mina con un asterisco (*)
        return "*"

# Clase para una casilla normal (sin mina)
class CasillaSinMina(Casilla):
    def __init__(self):
        super().__init__()          # Llama al constructor de Casilla
        self.minas_cercanas = 0     # Guarda cuántas minas hay alrededor

    def revelar(self):
        # Marca la casilla como revelada
        self.revelada = True

    def _mostrar_revelada(self):
        # Muestra el número de minas cercanas si hay alguna,
        return str(self.minas_cercanas) if self.minas_cercanas > 0 else " "
