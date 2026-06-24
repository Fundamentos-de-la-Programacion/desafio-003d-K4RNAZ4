import random

banco_preguntas = [
    {" pregunta ": " Cual es la capital de Chile ?", " respuesta ": " Santiago "},
    {" pregunta ": " Cuanto es 7 por 8?", " respuesta ": "56"},
    {
        " pregunta ": " Que palabra clave define una funcion en Python ?",
        " respuesta ": " def ",
    },
    {
        " pregunta ": " Cual es el simbolo del resto ( modulo ) en Python ?",
        "respuesta ": " %",
    },
    {" pregunta ": " Que tipo de dato es 3.14? ", " respuesta ": " float "},
    {" pregunta ": " Cuantos colores tiene el arcoiris ?", " respuesta ": "7"},
    {
        " pregunta ": " Que funcion muestra texto en pantalla en Python ?",
        "respuesta ": " print ",
    },
    {
        " pregunta ": " Cual es el oceano que limita con Chile ?",
        " respuesta ": " Pacifico ",
    },
]

def mostrar_pregunta(pregunta):
    """Recibe un diccionario de pregunta y muestra en pantalla su texto de la clave "pregunta"."""
    print(pregunta[" pregunta "])


def normalizar(texto)
    """Convierte a minúsculas y quita espacios al inicio y final."""
    return texto.lower().strip()


def es_correcta(respuesta_usuario, respuesta_correcta)
    """Retorna True si las respuestas coinciden luego de normalizarlas."""
    return normalizar(respuesta_usuario) == normalizar(respuesta_correcta)


def jugar_ronda(jugador, banco, n)
    """Elige n preguntas al azar del banco, las juega y retorna el puntaje obtenido."""
    preguntas_jugadas = random.sample(banco, n)
    puntaje = 0

    for pregunta in preguntas_jugadas:
        mostrar_pregunta(pregunta)
        respuesta_usuario = input("Tu respuesta: ")

        if es_correcta(respuesta_usuario, pregunta[" respuesta "]):
            puntaje += 1

    return puntaje

def mostrar_ranking(jugadores)
    """Ordena de mayor a menor puntaje y muestra el ranking con porcentaje de aciertos."""
    jugadores_ordenados = sorted(jugadores, key=lambda j: j["puntaje"], reverse=True)

    print("=== RANKING FINAL ===")

    for i, jugador in enumerate(jugadores_ordenados, start=1):
        preguntas = jugador["preguntas"]
        if preguntas == 0:
            porcentaje = 0.0
        else:
            porcentaje = (jugador["puntaje"] / preguntas) * 100

        print(
            f"{i}. {jugador['nombre']} - {jugador['puntaje']} pts - {porcentaje:.2f} % de aciertos"
        )


def main()
    print("Bienvenido al Juego de Trivia")

    try:
        cantidad = int(input("¿Cuántos jugadores van a jugar? "))
    except ValueError:
        cantidad = 0

    jugadores = []
    n_preguntas = 5

    for _ in range(cantidad):
        nombre = input("Nombre del jugador: ")
        puntaje = jugar_ronda(nombre, banco_preguntas, n_preguntas)

        jugadores.append(
            {
                "nombre": nombre,
                "puntaje": puntaje,
                "preguntas": n_preguntas,
            }
        )

    mostrar_ranking(jugadores)
    print("Gracias por jugar!")


if __name__ == "__main__":
    main()

