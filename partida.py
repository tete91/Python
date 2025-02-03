import random #Importamos el random
from diccionarioNaruto import obtenerPreguntasNaruto #Importamos los diccionarios con las palabras del juego
from diccionarioOnePiece import obtenerPreguntasOnePiece
from diccionarioDragonBall import obtenerPreguntasDragonBall
from diccionarioHXH import obtenerPreguntasHXH
from diccionarioPokemon import obtenerPreguntasPokemon
from diccionarioYugioh import obtenerPreguntasYugioh

jugadores = [] #Inicializamos la lista que contendrá los jugadores a participar.

def comenzarPartida(): #Creamos una función para comenzar la partida.
    cantidadJugadores = int(input("¿Cuántos jugadores van a jugar? Elige un mínimo de 2 y un máximo de 6.")) #Inicializamos una variable que contendrá la cantidad de jugadores y pedimos la cantidad por terminal
    while cantidadJugadores<2 or cantidadJugadores>6: #Bucle mientras no se introduzca una cantidad correcta de jugadores
        cantidadJugadores = int(input("¿Cuántos jugadores van a jugar? Elige un mínimo de 2 y un máximo de 6.")) #Repetimos pregunta de la variable al no introducir un valor correcto
    for contador in range(cantidadJugadores): #Bucle con un contador que recorrerá la cantidad del rango de cantidadJugadores
        nombre = input(f"Ingrese el nombre del jugador {contador+1}: \n") #Variable con el nombre de los jugadores, solicitamos el input indicando su posición de la lista + 1 para el usuario
        jugadores.append({ #Rellenamos cada jugador con sus datos de nombre y las categorias ganadas inicializadas en false.
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

def jugar(): #Creamos una función para comenzar a jugar.
    seguirJugando=True #Inicializamos el seguir jugando a True para iterar almenos una vez antes de cada partida.
    turno=0 #Inicializamos una variable que contendrá el jugador al que le toca tirar
    while seguirJugando: #Bucle que iterará mientras nadie gane la partida.
        jugador = jugadores[turno] #Variable que almacenará los datos del jugador de ese turno.
        dado = lanzarDado() #Lanzamos dado
        print(f"El jugador {jugador['nombre']} ha sacado un {dado}") #Indicamos el valor del dado lanzado
        pregunta , categoria = categoriaTocado(dado) #Asignamos a pregunta y categoria las variables almacenadas en la categoria tocada del dado
        preguntaHecha = random.choice(pregunta) #Escogemos del diccionario guardado en pregunta, una al azar.
        respuesta=preguntaHecha["respuesta"].upper #Variable en que guardamos la respuesta de la pregunta escogida del random y la parseamos a upper
        print(f"\nPregunta: {preguntaHecha['pregunta']}") #Imprimimos la pregunta
        print(f"\nOpciones: ") #Imprimimos las posibles respuestas
        for letra, opcion in preguntaHecha['opciones'].items(): #Bucle que recorrera cada opcion dentro de la pregunta
            print(f"{letra}: {opcion}") #Imprimimos cada posible opción.
        respuestaIntroducida = input("\nEscoge la respuesta entre A, B o C: ").upper() #Pedimos y leemos por terminal la respuesta elegida
        if jugador['categoriasGanadas'][categoria] is True: #Condicional en caso de que ya se tuviese esa categoria acertada
            if respuestaIntroducida == preguntaHecha['respuesta'].upper(): #Si la respuesta es correcta lo indicamos y volvemos a tirar
                print("Respuesta correcta, vuelve a tirar el dado.")
                input("Presiona enter para continuar.")
            else: #Si la respuesta es incorrecta lo indicamos y pasamos turno sumando 1 al contador
                print("Respuesta incorrecta. Pasa al turno al siguiente compañero.")
                input("Presiona enter para continuar.")
                turno+=1
        else: #Si la categoria no estaba acertada con anterioridad
            if respuestaIntroducida == preguntaHecha['respuesta'].upper():#Si la respuesta es correcta lo indicamos y volvemos a tirar
                print(f"Respuesta correcta, ahora ya tienes acertada la categoria de {categoria}. Vuelve a tirar el dado.")
                jugador['categoriasGanadas'][categoria] = True
                input("Presiona enter para continuar.")
            else:#Si la respuesta es incorrecta lo indicamos y pasamos turno sumando 1 al contador
                print("Respuesta incorrecta. Pasa al turno al siguiente compañero.")
                input("Presiona enter para continuar.")
                turno+=1
        if all(jugador['categoriasGanadas'][categoria] == True for categoria in jugador['categoriasGanadas']): #Condicional en caso de haber acertado todas las categorias, Indicamos el ganador y salimos del bucle cambiando seguirJugando a False
            print(f"\n Enhorabuena {jugador['nombre']} has ganado la partida.")
            seguirJugando = False
        if turno > len(jugadores) - 1: #Condicional en caso de haber tirado ya todos los jugadores reinicializamos los turnos.
            turno = 0
