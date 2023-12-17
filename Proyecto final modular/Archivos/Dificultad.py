import tkinter as tk

def setDificultadFacil():
    global tamTablero
    global minas
    global filas
    global columnas
    global dificultad
    tamTablero = "270x270"
    minas = 10
    filas = 9
    columnas = 9
    dificultad = 'Facil'

def setDificultadMedio():
    global tamTablero
    global minas
    global filas
    global columnas
    global dificultad
    tamTablero = "320x320"
    minas = 40
    filas = 16
    columnas = 16
    dificultad = 'Media'

def setDificultadDificil():
    global tamTablero
    global minas
    global filas
    global columnas
    global dificultad
    tamTablero = "320x600"
    minas = 99
    filas = 30
    columnas = 16
    dificultad = 'Dificil'