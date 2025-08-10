import unittest
from tateti import Tateti
from jugador import Jugador

class TestTatetiIntegridad(unittest.TestCase):
    def test_inicializacion_jugadores(self):
        juego = Tateti("Ana", "Luis", 0)
        self.assertEqual(juego.jugadores[0].nombre, "Ana")
        self.assertEqual(juego.jugadores[1].nombre, "Luis")
        self.assertEqual(juego.jugadores[0].ficha, "X")
        self.assertEqual(juego.jugadores[1].ficha, "O")

    def test_turno_inicial(self):
        juego = Tateti("Ana", "Luis", 1)
        self.assertEqual(juego.jugador_actual.nombre, "Luis")
        juego = Tateti("Ana", "Luis", 0)
        self.assertEqual(juego.jugador_actual.nombre, "Ana")

    def test_cambiar_turno(self):
        juego = Tateti("Ana", "Luis", 0)
        self.assertEqual(juego.jugador_actual.nombre, "Ana")
        juego.cambiar_turno()
        self.assertEqual(juego.jugador_actual.nombre, "Luis")
        juego.cambiar_turno()
        self.assertEqual(juego.jugador_actual.nombre, "Ana")

    def test_tablero_vacio_al_iniciar(self):
        juego = Tateti("Ana", "Luis", 0)
        for fila in juego.tablero.contenedor:
            for casilla in fila:
                self.assertEqual(casilla, "")

    def test_no_hay_ganador_al_iniciar(self):
        juego = Tateti("Ana", "Luis", 0)
        self.assertFalse(juego.hay_ganador())

if __name__ == "__main__":
    unittest.main()