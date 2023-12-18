import tkinter as tk
from tkinter import messagebox
from Archivos import Dificultad
import time

def PantallaInicial(Ventana):
    # Titulo
    from Archivos.ConfigVentana import Configuracion_Inicial_Ventana
    Configuracion_Inicial_Ventana(Ventana,"Buscaminas","280x200")
    titulo_label = tk.Label(Ventana, text="Bienvenido a Buscaminas", font=("Helvetica", 14))
    titulo_label.place(relx=0.1, y=20)

    # Botones
    boton = tk.Button(text="Iniciar Partida", command=lambda: PantallaConfig(Ventana))
    boton2 = tk.Button(text="Salir", command=Ventana.destroy)
    boton.place(relx=0.3, y=70, width=100, height=30)
    boton2.place(relx=0.3, y=140, width=100, height=30)

def PantallaConfig(Ventana):
    from Archivos.ConfigVentana import Configuracion_Inicial_Ventana
    from Archivos.Dificultad import SetDificultad

    Ventana.destroy()
    ventana_nueva1 = tk.Tk()
    Configuracion_Inicial_Ventana(ventana_nueva1,"Configuracion","300x300")

    def cambiarColor(Boton,SobranteA,SobranteB): # Funcion para cambiar color del boton
        SobranteA.configure(bg="#f0f0f0")
        SobranteB.configure(bg="#f0f0f0")
        Boton.configure(bg="#73a0c1")
    
    # Titulo
    Titulo = tk.Label(ventana_nueva1, text="Configure la Partida a Jugar", font=("Helvetica", 14))
    Titulo.place(relx=0.1, y=20)

    # Dificultad por botones
    Subtitulo1 = tk.Label(ventana_nueva1, text="Dificultad", font=("Helvetica", 9))

    Dificultad_boton1 = tk.Button(text="Facil", command=lambda:  [SetDificultad("270x270",10,9,9,'Facil'),cambiarColor(Dificultad_boton1,Dificultad_boton2,Dificultad_boton3)])
    Dificultad_boton2 = tk.Button(text="Medio", command=lambda:  [SetDificultad("320x320",40,16,16,'Media'),cambiarColor(Dificultad_boton2,Dificultad_boton3,Dificultad_boton1)])
    Dificultad_boton3 = tk.Button(text="Dificil", command=lambda: [SetDificultad("320x600",99,30,16,'Dificil'),cambiarColor(Dificultad_boton3,Dificultad_boton1,Dificultad_boton2)])

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
    from Archivos.Jugabilidad import clic_boton
    from Archivos.ConfigTablero import inicializar_tablero
    minas = Dificultad.minas
    filas = Dificultad.filas
    columnas = Dificultad.columnas

    global root, tablero, botones, contador,inicio_tiempo
    Ventana2.destroy()
    root = tk.Tk()
    root.resizable(0,0)
    root.title("Buscaminas")

    # Frames que separan la ventana
    frame1 = tk.Frame(root, bg="#73a0c1")
    frame1.pack(side="top", fill="both")
    frame2 = tk.Frame(root, bg="Yellow")
    frame2.pack(expand=True, fill="both")

    # Frame1
    contador = tk.Label(frame1, text=f"Contador: {0}/{minas}", font=("Helvetica", 12), bg="#73a0c1")
    contador.pack(side="left")

    volver_boton = tk.Button(frame1, text="😊", command=lambda: PantallaConfig(root), font=("Helvetica", 12), width=1, height=1, bg="yellow")
    volver_boton.pack(side="left", anchor="n", fill="y")

    #Timer
    tiempo_transcurrido = tk.StringVar()
    tiempo_transcurrido.set("Tiempo: 0")
    Temporizador = tk.Label(frame1, textvariable=tiempo_transcurrido, font=("Helvetica", 12), bg="#73a0c1")
    Temporizador.pack(side="right")

    # Frame2 (del tablero de juego)
    tablero = inicializar_tablero(filas, columnas, minas)
    botones = [[None for _ in range(columnas)] for _ in range(filas)]
    for fila in range(filas):
        for columna in range(columnas):
            boton = tk.Button(frame2, text=' ', width=2, height=1, command=lambda f=fila, c=columna: clic_boton(f, c, '<Button-1>',tablero, botones, contador))
            boton.grid(row=fila, column=columna)
            botones[fila][columna] = boton
            boton.bind('<Button-3>', lambda event, f=fila, c=columna: clic_boton(f, c, '<Button-3>', tablero, botones, contador))  # Asociar clic derecho
    
    def actualizar_temporizador():
        tiempo_actual = int(time.time() - inicio_tiempo)
        tiempo_transcurrido.set(f"Tiempo: {tiempo_actual}")
        root.after(1000, actualizar_temporizador)  # Llamar a la función cada 1000 ms (1 segundo)

    inicio_tiempo = time.time()  # Guardar el tiempo de inicio
    actualizar_temporizador()  # Iniciar el temporizador

    root.mainloop()
