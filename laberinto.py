TAMAÑO = 5
mapa = [["·" for _ in range(TAMAÑO)] for _ in range(TAMAÑO)]
obstaculos = [(0,1),(0,2),(0,3),(0,4),(1,1),(2,1),(2,3),(3,3),(4,0),(4,1),(4,2),(4,3)]
for f, c in obstaculos:
    mapa[f][c] = "X"
inicio = [0, 0]
meta = [4, 4]
pos_actual = list(inicio)

def dibujar_escenario():
    print("\n--- LABERINTO INTERACTIVO ---")
    for f in range(TAMAÑO):
        fila_visual = ""
        for c in range(TAMAÑO):
            if [f, c] == pos_actual:
                fila_visual += " P " # P de Personaje
            elif [f, c] == meta:
                fila_visual += " S " # S de Salida
            else:
                fila_visual += f" {mapa[f][c]} "
        print(fila_visual)
    print("-----------------------------\n")

while pos_actual != meta:
    dibujar_escenario()
    mov = input("Mueve con W (arriba), S (abajo), A (izquierda), D (derecha): ").upper()

    nueva_f, nueva_c = pos_actual[0], pos_actual[1]

    if mov == "W": nueva_f -= 1
    elif mov == "S": nueva_f += 1
    elif mov == "A": nueva_c -= 1
    elif mov == "D": nueva_c += 1
    else:
        print("¡Tecla no válida!")
        continue

    if 0 <= nueva_f < TAMAÑO and 0 <= nueva_c < TAMAÑO and mapa[nueva_f][nueva_c] != "X":
        pos_actual = [nueva_f, nueva_c]
    else:
        print("¡No puedes ir por ahí! Hay un muro o es el límite.")

print("\n¡Felicidades! Has llegado a la salida.")