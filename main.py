import random #Importamos el random
import tkinter as tk#Importamos todas las librerias de tkinter
from tkinter import simpledialog, messagebox
from tkinter import *
from funciones import limpiarVentana, crearVentana, jugadores, salirDelJuego#Importamos las funciones y variables almacenadas en otros archivos
from comenzarPartida import comenzarPartida
from tiradas import lanzarDado, categoriaTocado
from jugarPartida import jugar
from descripcionTrivianime import obtenerDescripcionTrivianime

ventana = crearVentana()#Inicializamos una ventana llamanda la funcion.
ventana.config(bg="#2A5736")#Cambiado el background a un color verde tapete de poker
descripcionText = tk.Text(ventana, wrap="word", height=15)#Creamos una seccion con texto en nuestra ventana y le damos valores
descripcionText.insert("1.0", obtenerDescripcionTrivianime)#Indicamos la posicion del texto y lo imprimimos por ventana
descripcionText.config(state="disabled")#Desactivamos que puedan modificarlo
descripcionText.pack(expand=False, fill="both", pady=10)#Se coloca el texto en ventana y se le dan valores
limpiarVentana(ventana)

def comenzarPartidaNueva():#Funcion para comenzar una partida llamando a su correspondiente funcion almacenada en otro archivo
    comenzarPartida(ventana)

etiqueta = tk.Label(ventana, text=obtenerDescripcionTrivianime(), wraplength=500, justify="left", font=("Arial", 12))#Creamos texto con indicaciones del programa
etiqueta.pack(padx=10, pady=10)#Imprimimos el texto
etiqueta = tk.Label(ventana, text="A continuación diga que desea hacer: ")#Creamos texto con indicaciones del programa
etiqueta.pack()#Imprimimos el texto
boton = tk.Button(ventana, text="Comenzar nueva partida", command=comenzarPartidaNueva)#Creamos un boton de comenzar nueva partida y lo imprimimos
boton.pack()
boton = tk.Button(ventana, text="Salir del juego", command=lambda: salirDelJuego(ventana))#Creamos un boton de salir del juego y lo imprimimos
boton.pack()

ventana.mainloop()#Inicializamos el programa en entorno GUI