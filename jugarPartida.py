#Importamos librerias, funciones y variables externas necesarias
import random
import os
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import *
from funciones import limpiarVentana, crearVentana, jugadores, salirDelJuego
from funciones import jugadores, crearVentana, salirDelJuego, limpiarVentana
from tiradas import lanzarDado, categoriaTocado

def jugar(ventana):#funcion para comenzar a jugar tras añadir jugadores y nombres
    limpiarVentana(ventana)
    turno=0#Inicializamos en el turno 0
    
    def turnoJugador():#Funcion que iterara en el turno de un jugador, tirando dado, verificando pregunta y respuestas etc...
        limpiarVentana(ventana)
        jugador = jugadores[turno] #Variable que almacenará los datos del jugador de este turno.
        dado = lanzarDado() #Lanzamos dado
        mensaje = f"{jugador['nombre']} ha sacado un {dado}"#Imprimimos el numero de dado sacado y por quien
        etiquetaMensaje = tk.Label(ventana, text=mensaje)
        etiquetaMensaje.pack()
        pregunta , categoria = categoriaTocado(dado) #Asignamos a pregunta y categoria las variables almacenadas en la categoria tocada del dado
        preguntaHecha = random.choice(pregunta) #Escogemos del diccionario guardado en pregunta, una al azar.
        respuesta = preguntaHecha["respuesta"].upper() #Variable en que guardamos la respuesta de la pregunta escogida del random y la parseamos a upper
        etiquetaPregunta = tk.Label(ventana, text=f"\nPregunta de {categoria}: {preguntaHecha['pregunta']}")#De la pregunta escogida, la imprimimos y mostramos sus opciones
        etiquetaPregunta.pack()
        etiquetaOpciones = tk.Label(ventana, text="Opciones: ")
        etiquetaOpciones.pack()
        botonesOpciones = {} #Inicializamos un boton para almacenar las opciones de respuesta
        boton = tk.Button(ventana, text="Salir del juego", command=lambda: salirDelJuego(ventana))#opcion salir del juego
        boton.pack(side= BOTTOM)
        for letra, opcion in preguntaHecha['opciones'].items(): #Bucle que recorrera cada opcion dentro de la pregunta
            botonesOpciones[letra] = tk.Button(ventana, text=f"{letra}: {opcion}", command=lambda letra=letra: verificarRespuesta(letra, respuesta, jugador, categoria))#boton con la letra de la opcion imprime su informacion y lee la eleccion
            botonesOpciones[letra].pack(side=tk.LEFT)
        def verificarRespuesta(letra, respuesta, jugador, categoria):#Funcion anidada para verificar la respuesta escogida
            nonlocal turno
            if letra == respuesta:#Condicional si la respuesta es correcta
                if not jugador['categoriasGanadas'][categoria]:#Condicional si no se habia acertado esta categoria, la pasamos a True el acierto y lo indicamos por mensaje
                    jugador['categoriasGanadas'][categoria] = True
                    mensajeRespuesta = f"Respuesta correcta, ahora ya tienes acertada la categoria de {categoria}. Vuelve a tirar el dado."
                else:#Si ya estab acertada la categoria, se avisa y se vuelve a tirar
                    mensajeRespuesta = "Respuesta correcta, vuelve a tirar el dado."
                etiquetaRespuesta = tk.Label(ventana, text=mensajeRespuesta)
                etiquetaRespuesta.pack()
                if all(jugador['categoriasGanadas'].values()):#Verificamos si ya estan todas las categorias en True y de ser avisamos del ganador y salimos del programa
                    etiquetaGanador = tk.Label(ventana, text=f"¡{jugador['nombre']} ha ganado la partida!")
                    etiquetaGanador.pack()
                    return
                ventana.after(2000, turnoJugador)#Damos un timelapse para el cambio de turno
            else:#En caso de fallar respuesta, no se suma  naada y se pasa el turno
                etiquetaRespuesta = tk.Label(ventana, text="Incorrecto. Es el turno del siguiente jugador.")
                etiquetaRespuesta.pack()
                turno = (turno + 1) % len(jugadores)
                ventana.after(2000, turnoJugador)
    turnoJugador()#Pasamos turno