#Importamos librerias, funciones y variables externas
import random #Importamos el random
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import *
from descripcionTrivianime import obtenerDescripcionTrivianime

jugadores = []#Inicializamos la lista con los nombres y datos de los jugadores

def crearVentana():#Funcion que creará la ventana principal con sus caracteristicas
    ventana = tk.Tk()
    ventana.title("TRIVIANIME")
    ventana.geometry("1024x768")
    return ventana

def limpiarVentana(ventana):#Funcion para limpiar la pantalla y no se apelotone codigo
    for widget in ventana.winfo_children():
        widget.destroy()

def salirDelJuego(ventana):#Funcion para salir del juego en cualquier momento
    ventana.destroy()
