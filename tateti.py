from tablero import Tablero, PosOcupadaException
from jugador import Jugador

class Tateti:
    def __init__(self, nombre1, nombre2, turno_inicial):
        self.tablero = Tablero()
        self.jugadores = [
            Jugador(nombre1, "X"),
            Jugador(nombre2, "O")
        ]
        self.turno = turno_inicial  # 0 o 1
        self.jugador_actual = self.jugadores[self.turno]

    def ocupar_una_de_las_casillas(self, fil, col):
        try:
            self.tablero.poner_la_ficha(fil, col, self.jugador_actual.ficha)
        except PosOcupadaException as e:
            raise Exception("¡Esa casilla ya está ocupada!")

    def cambiar_turno(self):
        self.turno = 1 - self.turno
        self.jugador_actual = self.jugadores[self.turno]

    def hay_ganador(self):
        t = self.tablero.contenedor
        f = self.jugador_actual.ficha
        # Filas y columnas
        for i in range(3):
            if all(t[i][j] == f for j in range(3)):
                return True
            if all(t[j][i] == f for j in range(3)):
                return True
        # Diagonales
        if all(t[i][i] == f for i in range(3)):
            return True
        if all(t[i][2-i] == f for i in range(3)):
            return True
        return False

    def esta_lleno(self):
        return all(self.tablero.contenedor[i][j] != "" for i in range(3) for j in range(3))

