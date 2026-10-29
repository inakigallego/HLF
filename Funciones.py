import numpy as np
import random


#Función para crear tableros
def crear_tablero():
    """
    Apartado 1 - Crea un tablero de 10x10
    """
    tablero = np.full((10, 10), "_")# Rellenar con espacios vacíos es un problema a la hora de mirar las coordenadas en las columnas. Meto con guión bajo
    return tablero

def crear_barco(eslora):
    """
    Apartado 4 - Crea una lista de casillas aleatorias para un barco según su eslora.
    Ejemplo: si eslora = 3, devolverá algo como [(2, 4), (2, 5), (2, 6)]
    """
    # 1. Elijo al azar la orientación: 'H' (horizontal) o 'V' (vertical)
    orientacion = random.choice(["H", "V"])
    # 2. Elijo la fila y la columna de inicio de forma aleatoria
    if orientacion == "H":
        # Si es horizontal, la fila puede ser de 0 a 9, 
        # pero la columna debe dejar espacio para que quepa el barco (de 0 a 10 - eslora)
        fila = random.randint(0, 9)
        columna = random.randint(0, 10 - eslora)
    else:
        # Si es vertical, la fila debe dejar espacio hacia abajo (de 0 a 10 - eslora)
        # y la columna puede ser de 0 a 9
        fila = random.randint(0, 10 - eslora)
        columna = random.randint(0, 9)
    # 3. Construyo la lista con todas las casillas que ocupa el barco
    barco = []
    for i in range(eslora):
        if orientacion == "H":# Si es horizontal, avanzamos en la columna
            casilla = (fila, columna + i)
        else:# Si es vertical, avanzamos en la fila
            casilla = (fila + i, columna)
        barco.append(casilla)        
    return barco

def colocar_barcos(tablero):
    """
    Apartado 2 - Coloca los 6 barcos de la flota (1 de 4, 2 de 3 y 3 de 2) 
    de manera aleatoria y sin que se choquen entre ellos.
    """
    esloras = [4, 3, 3, 2, 2, 2]# 1. Defino la lista con las esloras de los 6 barcos (de mayor a menor)
    for eslora in esloras:# 2. Recorro cada eslora para ir colocando los barcos uno a uno
        colocado = False        
        while not colocado:# Este bucle 'while' intenta colocar el barco una y otra vez hasta que encuentra un hueco libre que no choque con otro barco.
            barco = crear_barco(eslora) # Creo un barco usando la función del apartado 4           
            espacio_libre = True # Se comprueba si todas las casillas de este barco están libres (' ')
            for casilla in barco:
                fila = casilla[0]
                columna = casilla[1]
                if tablero[fila, columna] != "_": # Si en esa casilla ya hay una 'O', significa que choca
                    espacio_libre = False
                    break # Salgo del bucle porque este sitio no nos sirve
            if espacio_libre: # Si el espacio está libre, coloco el barco en el tablero
                for casilla in barco:
                    tablero[casilla[0], casilla[1]] = "O"
                colocado = True # Marco el barco como colocado y se sale del while
    return tablero

"""No me vale, lo terminaré borrando
def disparar(casilla, tablero):
    
    Apartado 3 - Recibe una casilla (fila, columna) y el tablero.
    Comprueba si acierta en un barco o cae en agua y actualiza el tablero.
        1-Mira qué hay en esa casilla concreta del tablero.
        2-Si encuentra una "O" (un barco), la borra y pone una "X" (¡Tocado!).
        3-Si encuentra un espacio vacío "_" (agua), lo borra y pone una "A" (¡Agua!).
    
    fila = casilla[0]
    columna = casilla[1]
        
    if tablero[fila, columna] == "O": # 1. Compruebo si hay un barco ('O')
        tablero[fila, columna] = "X"   # Como SÍ hay barco, cambio la casilla a X de Tocado y lanzo el mensaje
        print("¡Tocado!")
        
    elif tablero[fila, columna] == "_": # 2. Compruebo si hay espacio vacío (' ')
        tablero[fila, columna] = "A"   # Como NO hay un barco, SÍ está vacio, cambio la casilla A de Agua
        print("¡Agua!")
        
    else: # 3. Por si acaso ya se había disparado ahí antes. Tengo que pensar si corre turno o no: no lo he decidido
        print("No te enteras!!! Ya habías disparado en esta casilla.")
    
    OJO!!! con esta función tengo un problema: disparo, me lo marca en el tablero del rival pero no lo recoge en el mío
"""


def disparar(casilla, tablero_rival, tablero_disparos):
    """
    Apartado 3 - Recibe una casilla (fila, columna) y el tablero.
    Dispara a una casilla del tablero del rival y anota el resultado en el tablero
    en el tablero de disparos del jugador y en el de barcos del rival (No es necesario).    
        Comprueba si acierta en un barco o cae en agua y actualiza el tablero.
            1-Mira qué hay en esa casilla concreta del tablero.
            2-Si encuentra una "O" (un barco), la borra y pone una "X" (¡Tocado!).
            3-Si encuentra un espacio vacío "_" (agua), lo borra y pone una "A" (¡Agua!).
            4-Si disparo sobre un disparo y ejecutado, estoy por decidir si pasa turno o no
            5-De momento no he resuelto que cada vez que corra el main no se reinicien los tableros
    """
    fila = casilla[0]
    columna = casilla[1]
    
    if tablero_rival[fila, columna] == "O": # 1. Compruebo en el tablero del rival si hay barco ('O') o agua ('_')
        tablero_rival[fila, columna] = "X"       # Marco tocado en el rival
        tablero_disparos[fila, columna] = "X"    # Guardo la X en mis disparos de jugador
        print("¡Tocado!")
        
    elif tablero_rival[fila, columna] == "_":
        tablero_rival[fila, columna] = "A"       # Marco agua en el rival
        tablero_disparos[fila, columna] = "A"    # Guardo la A en mis disparos
        print("¡Agua!")
        
    else:
        print("No te enteras!!! Ya habías disparado en esta casilla.")
        
    return tablero_rival, tablero_disparos

def disparo_maquina(tablero_jugador):
    """
    La máquina elige una coordenada aleatoria (0-9) que no haya sido disparada antes,
    dispara contra el tablero de barcos del jugador y devuelve el resultado.
    """
    disparo_valido = False
    
    while not disparo_valido:# Se genera una fila y columna al azar
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        # Compruebo que la casilla esté libre de disparos previos (es decir, que no sea X ni A)
        if tablero_jugador[fila, columna] != "X" and tablero_jugador[fila, columna] != "A":
            disparo_valido = True  # ¡La coordenada es válida y sale del bucle!
    # Ahora toca el impacto en mi tablero de barcos
    if tablero_jugador[fila, columna] == "O":
        tablero_jugador[fila, columna] = "X"
        print(f"¡La máquina ha disparado a ", fila,",", columna, "y... ¡TE HA DADO (Tocado)! 💥")
        return True #Como ha acertado, debe repetir disparo
    else:
        tablero_jugador[fila, columna] = "A"
        print(f"¡La máquina ha disparado a ", fila,",", columna, "y... ha caído al agua! 🌊")
        return False # cede el turno por fallar
    