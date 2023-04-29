import random
import time
import os

def presentacion_1():

    
    print()
    print(  "JUEGO DE TOTITO ")
    print()
    print("1.- Nivel Facik")
    print("2.- Nivel Dificil")
    print()

    nivel = ""
    while nivel != "1" and nivel != "2":
        nivel = input("-->")

    return int(nivel)

def presentacion_2():

   
    print()
    print( "JUEGO DE TOTITO ")
    print()
    print()
    print("Sale la ficha O")
    print()
    print("Elige: O / X")
    print()
    print()

    ficha = ""
    while ficha != "O" and ficha != "X":
        ficha = input("            -->").upper()

    if ficha == "O":
        humano = "O"
        ordenador = "X"

    else:
        humano = "X"
        ordenador = "O"
        
    return humano, ordenador
        

def mostrar_tablero(tablero):

    print()
    print(  "           JUEGO DE TOTITO ")
    print()
    print("       1          |2            |3")
    print("          {}       |      {}      |     {}".format(tablero[0], tablero[1], tablero[2]))
    print("                  |             |")
    print("       -----------+-------------+--------------")
    print("       4          |5            |6")
    print("          {}       |      {}      |     {}".format(tablero[3], tablero[4], tablero[5]))
    print("                  |             |")
    print("       ----------------------------------------")
    print("       7          |8             |9")
    print("           {}      |     {}        |     {}".format(tablero[6], tablero[7], tablero[8]))
    print("                  |              |")
    print()


def seguir_jugando():


   
  
    print("presione enter para obtener respuesta del ordenador o elegir nuevo numero")
    respuesta = input("¿Otra partida (s)?").lower()
    if respuesta == "s" or respuesta == "si":
        return True
    
    else:
        return False

def hay_ganador(tablero, jugador):

  
    
    if tablero[0] == tablero[1] == tablero[2] == jugador or\
       tablero[3] == tablero[4] == tablero[5] == jugador or\
       tablero[6] == tablero[7] == tablero[8] == jugador or\
       tablero[0] == tablero[3] == tablero[6] == jugador or\
       tablero[1] == tablero[4] == tablero[7] == jugador or\
       tablero[2] == tablero[5] == tablero[8] == jugador or\
       tablero[0] == tablero[4] == tablero[8] == jugador or\
       tablero[2] == tablero[4] == tablero[6] == jugador:
        return True

    else:
        return False

def tablero_lleno(tablero):

    
    for i in tablero:
        if i == " ":
            return False
    else:
        return True

def casilla_libre(tablero, casilla):
    
    return tablero[casilla] == " "

def movimiento_jugador(tablero):
    
    
    posiciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input("          Te toca (1-9): ")
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion-1):
                print("      Esta posicion esta ocupada")
            else:
                return posicion-1

def mov_ordenador_facil(tablero, jugador):
    
   for i in range(9):
    copia = list(tablero)
    if casilla_libre(copia, i):
        copia[i] = jugador
        if hay_ganador(copia, jugador):
            return i
    
    while True:
        casilla = random.randint(0,8)
        if not casilla_libre(tablero, casilla):
            casilla = random.randint(0,8)
        else:
            return casilla


def mov_ordenador_dificil(tablero, maquina, usuario):

    
    for i in range(9):
        copia = list(tablero)
        if casilla_libre(copia, i):
            copia[i] = maquina
            if hay_ganador(copia, maquina):
                return i
    
    for i in range(9):
        copia = list(tablero)
        if casilla_libre(copia, i):
            copia[i] = usuario
            if hay_ganador(copia, usuario):
                return i
    
    if ordenandor == "X":
        if tablero[4] == " ":
            return 4
        esquina_vacia = []
        for i in [0, 2, 6, 8]:
            if casilla_libre(tablero, i):
                esquina_vacia.append(i)

        demas_vacias = []
        for i in [1, 3, 5, 7]:
                if casilla_libre(tablero, i):
                    demas_vacias.append(i)

        if len(esquina_vacia) > 0:
            return random.choice(esquina_vacia)
        
        else:
            return random.choice(demas_vacias)

    if ordenandor == "O":
        contador = 0
        for i in range(9):
            if casilla_libre(tablero, i):
                contador += 1

            if contador == 7:
                if tablero[4] == " ":
                    return 4
    
    while True:
        casilla = random.randint(0,8)
        if not casilla_libre(tablero, casilla):
            casilla = random.randint(0,8)
        else:
            return casilla

# Programa Principal 

jugando = True

while jugando:

    tablero = [" "] * 9
    nivel = presentacion_1()


    humano, ordenandor = presentacion_2()


    mostrar_tablero(tablero)

    if humano == "O":
        turno = "Humano"
    else:
        turno = "Ordenador"

    partida =   True

    while partida:
        if tablero_lleno(tablero):
            print("              EL JUEGO HA SIDO EMPATE...")
            partida = False
        
        elif turno == "Humano":
            casilla = movimiento_jugador(tablero)
            tablero[casilla] = humano
            turno = "Ordenador"
            #os.system("cls")
            mostrar_tablero(tablero)
            if hay_ganador(tablero, humano):
                print ("            HAS GANADO")
                partida = False
        
        elif turno == "Ordenador":
            print("        El ordenador esta pensando...")
            time.sleep(2)
            if nivel == 1:
                casilla = mov_ordenador_facil(tablero, humano)

            elif nivel == 2:
                casilla = mov_ordenador_dificil(tablero, ordenandor, humano)
            tablero[casilla] = ordenandor
            turno = "Humano"
            #os.system("cls")
            mostrar_tablero(tablero)
            if hay_ganador(tablero, ordenandor):
                print("          Has Perdido")
                partida = False

        jugando = seguir_jugando()


partida = True
while partida:

    jugando = seguir_jugando()

