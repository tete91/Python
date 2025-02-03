import random #Importamos el random
import tkinter as tk#Importamos librerias tkinter
from tkinter import simpledialog, messagebox
from tkinter import *
from funciones import limpiarVentana, jugadores, salirDelJuego#Importamos variables y funciones almacenadas externas
from jugarPartida import jugar

def comenzarPartida(ventana):#Funcion para comenzar una partida
    limpiarVentana(ventana)
    cantidadJugadores = 0#Inicializamos la cantidad de jugadores en 0
    etiquetaCantidadJugadores = tk.Label(ventana, text="Cuantos jugadores van a participar? ")
    etiquetaCantidadJugadores.pack()
    boton = tk.Button(ventana, text="2 jugadores", command=lambda: jugaran2(ventana))
    boton.pack(side= TOP)
    boton = tk.Button(ventana, text="3 jugadores", command=lambda: jugaran3(ventana))
    boton.pack(side= TOP)
    boton = tk.Button(ventana, text="4 jugadores", command=lambda: jugaran4(ventana))
    boton.pack(side= TOP)
    boton = tk.Button(ventana, text="5 jugadores", command=lambda: jugaran5(ventana))
    boton.pack(side= TOP)
    boton = tk.Button(ventana, text="6 jugadores", command=lambda: jugaran6(ventana))
    boton.pack(side= TOP)
    boton = tk.Button(ventana, text="Salir del juego", command=lambda: salirDelJuego(ventana))
    boton.pack(side= BOTTOM)

def solicitarNombre(ventana, cantidadJugadores=0):#Funcion para introducir los nombres de los jugadores
    limpiarVentana(ventana)
    contador = 0#Inicializamos el contador en 0
    etiqueta = tk.Label(ventana, text=f"Introduzca el nombre del jugador {contador+1}: ")#Pedimos el nombre del jugador en contador+1
    etiqueta.pack()
    entradaNombre = tk.Entry(ventana)#creamos un recuadro para la introduccion de texto y lo imprimimos
    entradaNombre.pack()
    boton = tk.Button(ventana, text="Salir del juego", command=lambda: salirDelJuego(ventana))#Damos la opcion en cualquier momento de abandonar el programa abajo en la app
    boton.pack(side= BOTTOM)
    def confirmarNombre():#Funcion anidada para rellenar los nombres
        nonlocal contador
        nombre = entradaNombre.get()
        if nombre:  #Almacenamos el nombre introducido e inicializamos todas las categorias en False
            jugadores.append({
                "nombre": nombre,
                "categoriasGanadas": {
                    "Pokemon": False,
                    "Dragon Ball": False,
                    "One Piece": False,
                    "Naruto": False,
                    "Hunter x Hunter": False,
                    "Yu-Gi-Oh!": False
                }    
            })
            contador+=1#contador +1 para iterar por los nombres
            if contador < cantidadJugadores:#Condicional si aun quedan nombres por introducir
                etiqueta.config(text=f"Introduzca el nombre del jugador {contador+1}: ")
                entradaNombre.delete(0, tk.END)
            else:#Ya estan completos pasamos a jugar
                if jugadores:
                    limpiarVentana(ventana)
                    jugar(ventana)
        else:#condicional en caso de no introducir nada
            etiqueta.config(text="Por favor, ingresa un nombre.")

    botonConfirmar = tk.Button(ventana, text="Confirmar", command=confirmarNombre)#Confirmamos y almacenamos el nombre
    botonConfirmar.pack()
#Funciones para cada cantidad posible de jugadores
def jugaran2(ventana):
    cantidadJugadores=2
    solicitarNombre(ventana, cantidadJugadores=cantidadJugadores)
    boton = tk.Button(ventana, text="Salir del juego", command=lambda: salirDelJuego(ventana))
    boton.pack(side= BOTTOM)
def jugaran3(ventana):
    cantidadJugadores=3
    solicitarNombre(ventana, cantidadJugadores=cantidadJugadores)
    boton = tk.Button(ventana, text="Salir del juego", command=lambda: salirDelJuego(ventana))
    boton.pack(side= BOTTOM)
def jugaran4(ventana):
    cantidadJugadores=4
    solicitarNombre(ventana, cantidadJugadores=cantidadJugadores)
    boton = tk.Button(ventana, text="Salir del juego", command=lambda: salirDelJuego(ventana))
    boton.pack(side= BOTTOM)
def jugaran5(ventana):
    cantidadJugadores=5
    solicitarNombre(ventana, cantidadJugadores=cantidadJugadores)
    boton = tk.Button(ventana, text="Salir del juego", command=lambda: salirDelJuego(ventana))
    boton.pack(side= BOTTOM)
def jugaran6(ventana):
    cantidadJugadores=6
    solicitarNombre(ventana, cantidadJugadores=cantidadJugadores)
    boton = tk.Button(ventana, text="Salir del juego", command=lambda: salirDelJuego(ventana))
    boton.pack(side= BOTTOM)
