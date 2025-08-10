from tateti import Tateti
import random

def pedir_nombre(jugador_num):
    return input(f"Ingrese el nombre del jugador {jugador_num}: ")

def tirada_moneda(jugador1, jugador2):
    eleccion = input(f"{jugador1}, elige cara o cruz: ").strip().lower()
    while eleccion not in ["cara", "cruz"]:
        eleccion = input("Por favor, elige 'cara' o 'cruz': ").strip().lower()
    resultado = random.choice(["cara", "cruz"])
    print(f"Salió {resultado}!")
    if eleccion == resultado:
        print(f"{jugador1} comienza.")
        return 0  # jugador1 empieza
    else:
        print(f"{jugador2} comienza.")
        return 1  # jugador2 empieza

def mostrar_tablero(tablero):
    print("  1 2 3")
    for i, fila in enumerate(tablero):
        print(f"{i+1} " + " ".join([casilla if casilla != "" else "." for casilla in fila]))

def pedir_posicion():
    while True:
        try:
            col = int(input("Ingrese columna (1-3): "))
            fil = int(input("Ingrese fila (1-3): "))
            if col not in [1,2,3] or fil not in [1,2,3]:
                print("Debe ingresar números entre 1 y 3.")
                continue
            return fil-1, col-1
        except ValueError:
            print("Debe ingresar un número entero entre 1 y 3.")

def main():
    print("Bienvenidos al Tateti")
    nombre1 = pedir_nombre(1)
    nombre2 = pedir_nombre(2)
    turno_inicial = tirada_moneda(nombre1, nombre2)
    juego = Tateti(nombre1, nombre2, turno_inicial)
    while True:
        mostrar_tablero(juego.tablero.contenedor)
        print(f"Turno de: {juego.jugador_actual.nombre} ({juego.jugador_actual.ficha})")
        fil, col = pedir_posicion()
        try:
            juego.ocupar_una_de_las_casillas(fil, col)
        except Exception as e:
            print(e)
            continue  # No cambia el turno si la casilla está ocupada
        if juego.hay_ganador():
            mostrar_tablero(juego.tablero.contenedor)
            print(f"¡Ganó {juego.jugador_actual.nombre}!")
            break
        if juego.esta_lleno():
            mostrar_tablero(juego.tablero.contenedor)
            print("¡Empate!")
            break
        juego.cambiar_turno()
        print("-" * 20)  # Línea divisora estética

if __name__ == '__main__':
    main()
