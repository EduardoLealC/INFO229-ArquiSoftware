import tkinter as tk

def Configuracion_Inicial_Ventana(Ventana, Titulo, Tamaño):
    Ventana.title(Titulo)  # Titulo
    Ventana.geometry(Tamaño)  # Tamaño
    Ventana.resizable(0, 0)  # No se permite editar el tamaño de la ventana
