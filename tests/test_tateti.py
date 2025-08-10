import unittest
from tateti import Tateti
from tablero import PosOcupadaException

class TestTateti(unittest.TestCase):
    def setUp(self):
        self.juego = Tateti("Jugador1", "Jugador2", 0)

    def test_poner_ficha_en_casilla_libre(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.tablero.contenedor[0][0], "X")

    def test_no_permitir_poner_ficha_en_casilla_ocupada(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        with self.assertRaises(Exception):
            self.juego.ocupar_una_de_las_casillas(0, 0)

    def test_ganador_fila(self):
        self.juego.ocupar_una_de_las_casillas(0, 0) 
        self.juego.cambiar_turno()
        self.juego.ocupar_una_de_las_casillas(1, 0)  
        self.juego.cambiar_turno()
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.juego.cambiar_turno()
        self.juego.ocupar_una_de_las_casillas(1, 1)  
        self.juego.cambiar_turno()
        self.juego.ocupar_una_de_las_casillas(0, 2)  
        self.assertTrue(self.juego.hay_ganador())

    def test_ganador_columna(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  
        self.juego.cambiar_turno()
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.juego.cambiar_turno()
        self.juego.ocupar_una_de_las_casillas(1, 0)  
        self.juego.cambiar_turno()
        self.juego.ocupar_una_de_las_casillas(1, 1)  
        self.juego.cambiar_turno()
        self.juego.ocupar_una_de_las_casillas(2, 0)  
        self.assertTrue(self.juego.hay_ganador())

    def test_ganador_diagonal(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  
        self.juego.cambiar_turno()
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.juego.cambiar_turno()
        self.juego.ocupar_una_de_las_casillas(1, 1)  
        self.juego.cambiar_turno()
        self.juego.ocupar_una_de_las_casillas(0, 2)  
        self.juego.cambiar_turno()
        self.juego.ocupar_una_de_las_casillas(2, 2)  
        self.assertTrue(self.juego.hay_ganador())

    def test_empate(self):
        jugadas = [
            (0, 0), (0, 1), (0, 2),
            (1, 1), (1, 0), (1, 2),
            (2, 1), (2, 0), (2, 2)
        ]
        for idx, (f, c) in enumerate(jugadas):
            self.juego.ocupar_una_de_las_casillas(f, c)
            if idx < len(jugadas) - 1:
                self.juego.cambiar_turno()
        self.assertTrue(self.juego.esta_lleno())
        self.assertFalse(self.juego.hay_ganador())

if __name__ == "__main__":
    unittest.main()