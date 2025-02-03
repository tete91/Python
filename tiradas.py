#Importamos librerias, funciones y variables almacenadas externamente
import random #Importamos el random
from diccionarios.diccionarioNaruto import obtenerPreguntasNaruto #Importamos los diccionarios con las palabras del juego
from diccionarios.diccionarioOnePiece import obtenerPreguntasOnePiece
from diccionarios.diccionarioDragonBall import obtenerPreguntasDragonBall
from diccionarios.diccionarioHXH import obtenerPreguntasHXH
from diccionarios.diccionarioPokemon import obtenerPreguntasPokemon
from diccionarios.diccionarioYugioh import obtenerPreguntasYugioh
from descripcionTrivianime import obtenerDescripcionTrivianime
def lanzarDado(): #Creamos una función para lanzar el dado con un numero random del 1 al 6
    return random.randint(1, 6)

def categoriaTocado(dado): #Creamos una función que en función al numero sacado escoja una categoria u otra y la asignamos a su respectivo diccionario.
    if dado == 1:
        return obtenerPreguntasDragonBall(), "Dragon Ball"
    elif dado == 2:
        return obtenerPreguntasHXH(), "Hunter x Hunter"
    elif dado == 3:
        return obtenerPreguntasNaruto(), "Naruto"
    elif dado == 4:
        return obtenerPreguntasOnePiece(), "One Piece"
    elif dado == 5:
        return obtenerPreguntasPokemon(), "Pokemon"
    elif dado == 6:
        return obtenerPreguntasYugioh(), "Yu-Gi-Oh!"
