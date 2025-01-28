automata = {
    'q0': {'0': 'q1', '1': 'q3'},
    'q1': {'0': 'q1', '1': 'q2'},
    'q2': {'0': 'q1', '1': 'q2'},
    'q3': {'0': 'q4', '1': 'q3'},
    'q4': {'0': 'q4', '1': 'q3'},
}

estados_finales = {'q2', 'q4'}

def simular_automata(cadena, estado_inicial='q0'):
    estado_actual = estado_inicial

    for simbolo in cadena:
        if simbolo in automata[estado_actual]:
            estado_actual = automata[estado_actual][simbolo]
        else:
            return False

    return estado_actual in estados_finales


def main():
    print("Simulador de autómata")
    print("Ingresa las cadenas que deseas probar (escribe 'salir' para terminar).")

    while True:
        cadena = input("\nIngresa una cadena de 0s y 1s: ").strip()

        if cadena.lower() == 'salir':
            print("¡Gracias por usar el simulador de autómata!")
            break

        if not all(caracter in {'0', '1'} for caracter in cadena):
            print("Error: La cadena debe contener solo 0s y 1s.")
            continue

        if simular_automata(cadena):
            print(f"La cadena '{cadena}' es ACEPTADA por el autómata.")
        else:
            print(f"La cadena '{cadena}' es RECHAZADA por el autómata.")


if __name__ == "__main__":
    main()