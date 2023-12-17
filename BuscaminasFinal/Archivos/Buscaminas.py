import tkinter as tk
from tkinter import messagebox
from .. import Final



def contar_minas_alrededor(tablero, fila, columna):
    filas, columnas = len(tablero), len(tablero[0])
    minas_alrededor = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            nueva_fila, nueva_columna = fila + i, columna + j
            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and tablero[nueva_fila][nueva_columna] == 'M':
                minas_alrededor += 1

    return minas_alrededor

#Funciones click derecho e izquierdo (revelar casillas y agregar banderines)
def clic_boton(fila, columna, event):
    global contador_bandera
    if event == '<Button-1>':  # Clic izquierdo
        if tablero[fila][columna] == 'M':
            messagebox.showinfo("Fin del juego", "¡Has perdido!")
            desactivar_botones()
        else:
            revelar_casilla(fila, columna)
            if verificar_victoria():
                messagebox.showinfo("Fin del juego", "¡Has ganado!")
                desactivar_botones()
    elif event == '<Button-3>':  # Clic derecho
        if botones[fila][columna]['text'] == ' ' and contador_bandera < minas:
            agregar_banderin(fila, columna)
            contador_bandera += 1
            actualizar_contador()
        elif botones[fila][columna]['text'] == '🚩':
            eliminar_banderin(fila, columna)
            contador_bandera -= 1
            actualizar_contador()

def agregar_banderin(fila, columna):
    botones[fila][columna].config(text='🚩', fg='red')

def eliminar_banderin(fila, columna):
    botones[fila][columna].config(text=' ', state=tk.NORMAL)

def revelar_casilla(fila, columna):
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
                    revelar_casilla(nueva_fila, nueva_columna)

def verificar_victoria():
    for fila in range(filas):
        for columna in range(columnas):
            if (
                tablero[fila][columna] != 'M'
                and botones[fila][columna]['state'] == tk.NORMAL
            ):
                return False
    return True

def desactivar_botones():
    global contador_bandera
    for fila in range(filas):
        for columna in range(columnas):
            if tablero[fila][columna] == 'M' and botones[fila][columna]['text'] != '🚩':
                botones[fila][columna].config(state=tk.DISABLED, text='💣', bg='#C91E00')
            else:
                botones[fila][columna].config(state=tk.DISABLED)
            botones[fila][columna].unbind('<Button-3>')

def actualizar_contador():
    contador.config(text=f"Contador: {contador_bandera}/{minas}")


def Tablero(Ventana2):
    global root, tablero, botones, contador,inicio_tiempo
    Ventana2.destroy()
    root = tk.Tk()
    root.resizable(0,0)
    root.title("Buscaminas")

    # Frames que separan la ventana
    frame1 = tk.Frame(root, bg="blue")
    frame1.pack(side="top", fill="both")
    frame2 = tk.Frame(root, bg="Yellow")
    frame2.pack(expand=True, fill="both")

    # Frame1
    contador = tk.Label(frame1, text=f"Contador: {0}/{minas}", font=("Helvetica", 12))
    contador.pack(side="left")

    volver_boton = tk.Button(frame1, text="😊", command=lambda: PantallaConfig(root), font=("Helvetica", 12), width=1, height=1, bg="yellow")
    volver_boton.pack(side="left", anchor="n", fill="y")


    tiempo_transcurrido = tk.StringVar()
    tiempo_transcurrido.set("Tiempo: 0")
    Temporizador = tk.Label(frame1, textvariable=tiempo_transcurrido, font=("Helvetica", 12))
    Temporizador.pack(side="right")

    # Frame2 (del tablero de juego)
    tablero = inicializar_tablero(filas, columnas, minas)
    botones = [[None for _ in range(columnas)] for _ in range(filas)]
    for fila in range(filas):
        for columna in range(columnas):
            boton = tk.Button(frame2, text=' ', width=2, height=1, command=lambda f=fila, c=columna: clic_boton(f, c, '<Button-1>'))
            boton.grid(row=fila, column=columna)
            botones[fila][columna] = boton
            boton.bind('<Button-3>', lambda event, f=fila, c=columna: clic_boton(f, c, '<Button-3>'))  # Asociar clic derecho

    def actualizar_temporizador():
        tiempo_actual = int(time.time() - inicio_tiempo)
        tiempo_transcurrido.set(f"Tiempo: {tiempo_actual}")
        root.after(1000, actualizar_temporizador)  # Llamar a la función cada 1000 ms (1 segundo)

    inicio_tiempo = time.time()  # Guardar el tiempo de inicio
    actualizar_temporizador()  # Iniciar el temporizador


    root.mainloop()
