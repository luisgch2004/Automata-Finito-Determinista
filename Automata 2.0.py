def reconocimiento(cadena):
    if not cadena:
        return False
    if not all(char in '01' for char in cadena):
        return False

    estado = "inicio"
    for char in cadena:
        match estado:
            case "inicio":
                if char == "0":
                    estado = "inicio_0"
                elif char == "1":
                    estado = "inicio_1"
                else:
                    return False
            case "inicio_0":
                if char not in "01":
                    return False
            case "inicio_1":
                if char not in "01":
                    return False

    match estado:
        case "inicio_0":
            return cadena[-1] == '1'
        case "inicio_1":
            return cadena[-1] == '0'

if __name__ == "__main__":
    print("Automata")
    cadena = input("Ingrese la cadena binaria: ")
    if reconocimiento(cadena):
        print(f"La cadena {cadena} fue reconocida CORRECTA")
    else:
        print(f"La cadena {cadena} fue reconocida INCORRECTA")