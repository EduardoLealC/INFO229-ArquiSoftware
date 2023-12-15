import tkinter as tk
from Archivos.ConfigVentana import Configuracion_Inicial_Ventana

def PantallaInicial(Ventana):

    #Titulo
    titulo_label = tk.Label(Ventana, text="Bienvenido a Buscaminas", font=("Helvetica", 14))
    titulo_label.place(relx=0.1, y=20)

    #Botones
    boton = tk.Button(text="Iniciar Partida", command=lambda: PantallaConfig(Ventana))
    boton2 = tk.Button(text="Salir", command=Ventana.destroy)

    boton.place(relx=0.3, y=70, width=100, height=30)
    boton2.place(relx=0.3, y=140, width=100, height=30)

def Tablero(Ventana2):
    Ventana2.destroy()
    Tablero = tk.Tk()
    Configuracion_Inicial_Ventana(Tablero,"Buscaminas","300x300")

    #Frames que separan la ventana
    frame1 = tk.Frame(Tablero,bg="blue")
    frame1.pack(side="top",fill="both")
    frame2 = tk.Frame(Tablero,bg="Yellow")
    frame2.pack(expand=True,fill="both")

    #Frame1
    contador = tk.Label(frame1, text="Contador: 0", font=("Helvetica", 12))
    contador.pack(side="left")

    Temporizador = tk.Label(frame1, text="Contador: 0", font=("Helvetica", 12))
    Temporizador.pack(side="right")

    Tablero.mainloop() 



def PantallaConfig(Ventana):
    Ventana.destroy() 
    ventana_nueva1 = tk.Tk()
    Configuracion_Inicial_Ventana(ventana_nueva1,"Configuracion","300x300")
 

    #Titulo
    Titulo = tk.Label(ventana_nueva1, text="Configure la Partida a jugar", font=("Helvetica", 14))
    Titulo.place(relx=0.1, y=20)

    #Dificultad
    Subtitulo1 = tk.Label(ventana_nueva1, text="Dificultad", font=("Helvetica", 9))
    Dificultad_boton1 = tk.Button(text="Facil")
    Dificultad_boton2 = tk.Button(text="Medio")
    Dificultad_boton3 = tk.Button(text="Dificil")

    Subtitulo1.place(relx=0.05, y=90)
    Dificultad_boton1.place(relx=0.1, y=140, width=60, height=30)
    Dificultad_boton2.place(relx=0.4, y=140, width=60, height=30)
    Dificultad_boton3.place(relx=0.7, y=140, width=60, height=30)

    #Inicio
    Comenzar_boton = tk.Button(text="Comenzar",command=lambda: Tablero(ventana_nueva1))
    Comenzar_boton.place(relx=0.25, rely=0.8, width=150, height=30)

    ventana_nueva1.mainloop() 

Ventana = tk.Tk() # Crear ventana principal
Configuracion_Inicial_Ventana(Ventana,"Buscaminas","280x200") #Configurar Ventana
PantallaInicial(Ventana) #Pantalla Inicial
Ventana.mainloop() # Mostrar Ventana