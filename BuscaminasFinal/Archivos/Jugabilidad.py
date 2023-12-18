import tkinter as tk
from tkinter import messagebox

from Archivos.Dificultad import filas, columnas, minas

contador_bandera = 0

def clic_boton(fila, columna, event, tablero, botones, contador):
    global contador_bandera
    if event == '<Button-1>':  # Clic izquierdo
        if tablero[fila][columna] == 'M':
            messagebox.showinfo("Fin del juego", "¡Has perdido!")
            desactivar_botones(tablero, botones)
        else:
            revelar_casilla(fila, columna, botones, tablero)
            if verificar_victoria(tablero, botones):
                messagebox.showinfo("Fin del juego", "¡Has ganado!")
                desactivar_botones(tablero, botones)
    elif event == '<Button-3>':  # Clic derecho
        if botones[fila][columna]['text'] == ' ' and contador_bandera < minas:
            botones[fila][columna].config(text='🚩', fg='red') #Agregar Banderin
            contador_bandera += 1
        elif botones[fila][columna]['text'] == '🚩':
            botones[fila][columna].config(text=' ', state=tk.NORMAL) #Eliminar Banderin
            contador_bandera -= 1
        contador.config(text=f"Contador: {contador_bandera}/{minas}")

def revelar_casilla(fila, columna, botones, tablero):
    if botones[fila][columna]['text'] == '🚩':
        # Si hay una bandera en la casilla, no hagas nada
        return

    if tablero[fila][columna] != ' ':
        botones[fila][columna].config(text=tablero[fila][columna], state=tk.DISABLED)
    else:
        botones[fila][columna].config(state=tk.DISABLED, bg='#D3D3D3')
        for i in range(-1, 2):
            for j in range(-1, 2):
                nueva_fila, nueva_columna = fila + i, columna + j
                if (
                    0 <= nueva_fila < filas
                    and 0 <= nueva_columna < columnas
                    and botones[nueva_fila][nueva_columna]['state'] == tk.NORMAL
                    and botones[nueva_fila][nueva_columna]['text'] != '🚩'
                ):
                    revelar_casilla(nueva_fila, nueva_columna,botones,tablero)

def verificar_victoria(tablero, botones):
    for fila in range(filas):
        for columna in range(columnas):
            if (
                tablero[fila][columna] != 'M'
                and botones[fila][columna]['state'] == tk.NORMAL
            ):
                return False
    return True

def desactivar_botones(tablero, botones):
    global contador_bandera
    for fila in range(filas):
        for columna in range(columnas):
            if tablero[fila][columna] == 'M' and botones[fila][columna]['text'] != '🚩':
                botones[fila][columna].config(state=tk.DISABLED, text='💣', bg='#C91E00')
            else:
                botones[fila][columna].config(state=tk.DISABLED)
            botones[fila][columna].unbind('<Button-3>')


