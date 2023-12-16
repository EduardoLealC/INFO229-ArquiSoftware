import tkinter as tk
from tkinter import messagebox
import random

# Define el tamaño del tablero segun la dificultad
def setDificultadFacil():
    global tamTablero
    global minas
    global filas
    global columnas
    tamTablero = "270x270"
    minas = 10
    filas = 9
    columnas = 9

def setDificultadMedio():
    global tamTablero
    global minas
    global filas
    global columnas
    tamTablero = "320x320"
    minas = 40
    filas = 16
    columnas = 16

def setDificultadDificil():
    global tamTablero
    global minas
    global filas
    global columnas
    tamTablero = "320x600"
    minas = 99
    filas = 30
    columnas = 16
#---------------------------- Fin de Seleccionar dificultad -------------------- 

# DEL TABLERO Y LA JUGABILIDAD:

#Inicializa el tablero (Coloca las minas y numeros aleatoriamente)
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

#Cuenta las minas alrededor del numero
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
        if botones[fila][columna]['text'] == ' ':
            agregar_banderin(fila, columna)
        elif botones[fila][columna]['text'] == 'B':
            eliminar_banderin(fila, columna)



def agregar_banderin(fila, columna):
    botones[fila][columna].config(text='B', fg='red', state=tk.DISABLED)

def eliminar_banderin(fila, columna):
    botones[fila][columna].config(text=' ', state=tk.NORMAL)


def revelar_casilla(fila, columna):
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
    for fila in range(filas):
        for columna in range(columnas):
            botones[fila][columna].config(state=tk.DISABLED)

def PantallaInicial(Ventana):
    # Titulo
    Ventana.geometry("300x300")
    Ventana.title("Buscaminas")
    titulo_label = tk.Label(Ventana, text="Bienvenido a Buscaminas", font=("Helvetica", 14))
    titulo_label.place(relx=0.1, y=20)

    # Botones
    boton = tk.Button(text="Iniciar Partida", command=lambda: PantallaConfig(Ventana))
    boton2 = tk.Button(text="Salir", command=Ventana.destroy)
    boton.place(relx=0.3, y=70, width=100, height=30)
    boton2.place(relx=0.3, y=140, width=100, height=30)

def PantallaConfig(Ventana):
    Ventana.destroy()
    ventana_nueva1 = tk.Tk()
    ventana_nueva1.geometry("300x300")  # Ajustar el tamaño de la ventana según tus necesidades
    ventana_nueva1.title("Buscaminas")
    # Titulo
    Titulo = tk.Label(ventana_nueva1, text="Configure la Partida a Jugar", font=("Helvetica", 14))
    Titulo.place(relx=0.1, y=20)

    # Dificultad por botones
    global tamTablero
    tamTablero = None
    Subtitulo1 = tk.Label(ventana_nueva1, text="Dificultad", font=("Helvetica", 9))
    Dificultad_boton1 = tk.Button(text="Facil", command=setDificultadFacil)
    Dificultad_boton2 = tk.Button(text="Medio", command=setDificultadMedio)
    Dificultad_boton3 = tk.Button(text="Dificil", command=setDificultadDificil)
    # Ubicacion de los botones
    Subtitulo1.place(relx=0.05, y=90)
    Dificultad_boton1.place(relx=0.1, y=140, width=60, height=30)
    Dificultad_boton2.place(relx=0.4, y=140, width=60, height=30)
    Dificultad_boton3.place(relx=0.7, y=140, width=60, height=30)

    # Inicio (boton comenzar)
    Comenzar_boton = tk.Button(text="Comenzar", command=lambda: Tablero(ventana_nueva1))
    Comenzar_boton.place(relx=0.25, rely=0.8, width=150, height=30)

    ventana_nueva1.mainloop()

def Tablero(Ventana2):
    global root, tablero, botones
    Ventana2.destroy()
    root = tk.Tk()
    root.title("Buscaminas")

    # Frames que separan la ventana
    frame1 = tk.Frame(root, bg="blue")
    frame1.pack(side="top", fill="both")
    frame2 = tk.Frame(root, bg="Yellow")
    frame2.pack(expand=True, fill="both")

    # Frame1
    contador = tk.Label(frame1, text="Contador: 0", font=("Helvetica", 12))
    contador.pack(side="left")

    Temporizador = tk.Label(frame1, text="Contador: 0", font=("Helvetica", 12))
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

    root.mainloop()

Ventana = tk.Tk() # Crear ventana principal
PantallaInicial(Ventana) # Pantalla Inicial
Ventana.mainloop() # Mostrar Ventana
