import random

def inicializar_tablero(filas, columnas, num_minas):
    tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

    # Colocar minas aleatorias
    for _ in range(num_minas):
        fila, columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)
        while tablero[fila][columna] == 'M':
            fila, columna = random.randint(0, filas - 1), random.randint(0, columnas - 1)
        tablero[fila][columna] = 'M'

    # Calcular números alrededor de las minas
    for fila in range(filas):
        for columna in range(columnas):
            if tablero[fila][columna] != 'M':
                minas_alrededor = contar_minas_alrededor(tablero, fila, columna)
                tablero[fila][columna] = str(minas_alrededor) if minas_alrededor > 0 else ' '

    return tablero

def contar_minas_alrededor(tablero, fila, columna):
    filas, columnas = len(tablero), len(tablero[0])
    minas_alrededor = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            nueva_fila, nueva_columna = fila + i, columna + j
            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and tablero[nueva_fila][nueva_columna] == 'M':
                minas_alrededor += 1

    return minas_alrededor