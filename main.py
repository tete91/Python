import partida #Importamos partida

def mostrarMenu(): #Funcion para mostrar el menú
    print("1. Comenzar una nueva partida")
    print("2. Salir del juego")
    
opcion = 0 #Variable para la opcion del menu, inicializada a 0 para iterar almenos una vez.
while opcion < 1 or opcion > 2: #Bucle que se repetirá mientras el valor introducido no sea un valor valido del menú.
    mostrarMenu() #Mostramos menú
    opcion = input("Escoge una opción del menú: ") #Solicitamos una opción del menú y la leemos
    try: #Abrimos Try catch por si introduce valores no parseables a int
        opcion = int(opcion) #Parseamos a int
        if opcion == 1: #Condicional en caso de que juguemos partida
            partida.comenzarPartida()
            partida.jugar()
            opcion = 0  #Reinicializamos a 0 para volver al menú y no salir del juego.
        elif opcion == 2: #Condicional que saldrá del juego y se despedirá
            print("Adiós jugadores.")
        else: #En caso de valor no valido del menu. lo indicamos y solicitamos nuevo valor
            print("El valor introducido no es correcto, intentalo de nuevo.")
    except ValueError: #Recogemos e indicamos el error del Try y reinicializamos opcion a 0 para volver a iterar.
        print("Por favor, introduce un número válido.")
        opcion=0