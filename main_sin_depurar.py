import Variables as v
import Funciones as f

"""
print("**********TABLERO_BARCOS_JUGADOR**********")
tbj = v.t_barcos_jugador # 1.1 Creo el tablero de los barcos del jugador
print(tbj)
print("\n")
print("**********TABLERO_DISPAROS_JUGADOR**********")
tdj = v.t_disparos_jugador # 1.2 Creo el tablero de disparos del jugador
print(tdj)
print("\n")
f.colocar_barcos(tbj) # 2 llamo a la función para que coloque los 6 barcos
print("**********TABLERO DEL JUGADOR CON LOS 6 BARCOS COLOCADOS**********")
print(tbj)
print("\n")

print("********** TABLERO DE BARCOS DEL RIVAL (VISIBLE PARA PRUEBAS) **********")
tbr = v.t_barcos_rival 
f.colocar_barcos(tbr) # 3 Coloco los 6 barcos de la máquina en su tablero y lo imprimo
print(tbr)
print("\n")

print("********** HACIENDO UN DISPARO DE PRUEBA **********")
f.disparar((1, 5), tbr) # Disparo: ojo a las coordenadas que van de 0 a 9
print("\n")
print("********** TABLERO DEL RIVAL DESPUÉS DEL DISPARO **********")
print(tbr)# Vuelvo a imprimir el tablero del rival para comprobar si marca el disparo con la 'X' o la 'A'
"""
"""
print("********** 1. TABLERO DE BARCOS DEL JUGADOR **********")
tbj = v.t_barcos_jugador
print(tbj)
print("\n")

print("********** 2. TABLERO DE DISPAROS del JUGADOR (INICIALMENTE VACÍO) **********")
tdj = v.t_disparos_jugador
print(tdj)
print("\n")

print("**********3. TABLERO DEL JUGADOR CON LOS 6 BARCOS COLOCADOS**********")
f.colocar_barcos(tbj) # 2 llamo a la función para que coloque los 6 barcos
print(tbj)
print("\n")

print("********** 3.1 TABLERO DE BARCOS DEL RIVAL (VISIBLE PARA MIS PRUEBAS) **********")
tbr = v.t_barcos_rival
f.colocar_barcos(tbr)  # Coloca los 6 barcos del rival (la máquina)
print(tbr)
print("\n")
"""
"""print("********** 4. REALIZANDO UN DISPARO DE PRUEBA **********")
# Elijo una coordenada (fila, columna) que vea en el tablero del rival (tbr)
# Por ejemplo, voy a disparar a la casilla (1, 2). 
# La función disparar actualizará 'tbr' y guardará el resultado en mi 'tdj'.
f.disparar((1, 2), tbr, tdj)
print("\n")"""
"""
print("********** 4. TURNO DE DISPARO INTERACTIVO **********")

# Que me pida la fila y la columna por pantalla mediante input()
# Indico int() porque el input devuelve un texto y necesito números enteros (0 a 9)
fila_usuario = int(input("Introduce la fila (de 0 a 9): "))
columna_usuario = int(input("Introduce la columna (de 0 a 9): "))
coordenada = (fila_usuario, columna_usuario) # Junto los dos números en una tupla, tal y como espera la función disparar
f.disparar(coordenada, tbr, tdj) # Ejecuto el disparo con la coordenada introducida


print("********** 5.TABLERO DE DISPAROS DEL JUGADOR (TDJ) TRAS EL DISPARO **********")
# ¡Aquí es donde veo reflejado el resultado ('X' si impacto o 'A' si fue agua)!
print(tdj)
"""
"""print("********** ¡COMIENZA LA PARTIDA DE HUNDIR LA FLOTA! **********\n")

# 1. CREACIÓN DE TABLEROS Y COLOCACIÓN DE BARCOS (¡Solo se hace UNA VEZ aquí al principio!)
tbj = v.t_barcos_jugador        # Mis barcos
f.colocar_barcos(tbj)           # Se colocan y se quedan fijos para toda la partida

tbr = v.t_barcos_rival          # barcos del rival
f.colocar_barcos(tbr)           # se colocan y se quedan fijos para toda la partida

tdj = v.t_disparos_jugador      # mi tablero de disparos (empieza vacío)

# 2. BUCLE PRINCIPAL DE LA PARTIDA
# Uso un bucle while True para ir alternando turnos de forma continua
turno_jugador = True
while turno_jugador:
    print("\n" + "="*50)
    print("ESTADO DE TUS DISPAROS (TDJ):")
    print(tdj)
    print("="*50)
    
    # --- TURNO DEL JUGADOR ---
    print("\n--- TU TURNO DE DISPARO ---")
    try:
        fila_usuario = int(input("Introduce la fila (de 0 a 9): "))
        columna_usuario = int(input("Introduce la columna (de 0 a 9): "))
        
        # Valido que estén dentro del tablero
        if 0 <= fila_usuario <= 9 and 0 <= columna_usuario <= 9:
            coordenada = (fila_usuario, columna_usuario)
            f.disparar(coordenada, tbr, tdj)
        else:
            print("Coordenadas fuera de rango. Deben estar entre 0 y 9. Pierdes el turno por bobo.")
    except ValueError:
        print("Por favor, introduce un número válido.")

    # --- TURNO DE LA MÁQUINA ---
    print("\n--- TURNO DE LA MÁQUINA ---")
    f.disparo_maquina(tbj)  # llamada a la función de disparo de la máquina
    
    # (Opcional) Si quier0 ver cómo va mi tablero de barcos tras el ataque de la máquina:
    # print(tbj)

    # Aquí más adelante añadiré la condición para romper el while (break) cuando alguien gane.
    # De momento, pulsar Ctrl + C en la terminal cuando quiera parar la partida."""


print("********** ¡COMIENZA LA PARTIDA DE HUNDIR LA FLOTA! **********\n")

# 1. Cre0 los tableros y coloco los barcos UNA SOLA VEZ (se quedan fijos)
tbj = v.t_barcos_jugador        # mis barcos
f.colocar_barcos(tbj)           

tbr = v.t_barcos_rival          # Barcos del rival
f.colocar_barcos(tbr)           

tdj = v.t_disparos_jugador      # Mi tablero de disparos (empieza vacío)

# 2. BUCLE PRINCIPAL DE LA PARTIDA
while True:
    print("\n" + "="*50)
    print("ESTADO DE TUS DISPAROS (TDJ):")
    print(tdj)
    print("="*50)
    
    # --- BUCLE DE MI TURNO (Permite repetir si acierto) ---
    turno_jugador = True
    while turno_jugador:
        print("\n--- TU TURNO DE DISPARO ---")
        try:
            fila_usuario = int(input("Introduce la fila (de 0 a 9): "))
            columna_usuario = int(input("Introduce la columna (de 0 a 9): "))
            
            if 0 <= fila_usuario <= 9 and 0 <= columna_usuario <= 9:
                coordenada = (fila_usuario, columna_usuario)
                
                # Compruebo qué hay en el tablero del rival antes de disparar
                # para saber si voy a acertar y repetir turno
                valor_casilla_antes = tbr[fila_usuario, columna_usuario]
                
                # Ejecuto el disparo
                f.disparar(coordenada, tbr, tdj)
                
                # Si he acertado un barco ('O'), ¡repito turno!
                if valor_casilla_antes == "O":
                    print("¡Has acertado! ¡Repites turno!")
                    print(tdj) # Muestro cómo va mi tablero de disparos actualizado
                else:
                    # Si fue agua o ya estaba disparado, pierdo el turno
                    turno_jugador = False
            else:
                print("Coordenadas fuera de rango. Deben estar entre 0 y 9.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    if f.comprobar_ganador(tbr):
        print("VICTORIA - HAS HUNDIDO LA FLOTA RIVAL")
        break

    # --- TURNO DE LA MÁQUINA ---
    print("\n" + "-"*30)
    print("TURNO DE LA MÁQUINA ATACANDO...")
    print("-"*30)
        
    turno_maquina = True
    while turno_maquina:
        # La función nos devuelve True si acertó y False si falló
        acerto = f.disparo_maquina(tbj)
            
        if acerto:
            print("¡La máquina ha acertado! ¡Vuelve a disparar!")
        else:
            print("La máquina ha fallado. Cede el turno.")
            turno_maquina = False
    if f.comprobar_ganador(tbj):
        print("GAME OVER")
        break
                
    # --- VISUALIZACIÓN DE TUS BARCOS TRAS EL FIN DEL TURNO RIVAL ---
    print("\n" + "="*50)
    print("MIRA TU TABLERO DE BARCOS (TBJ) TRAS EL ATAQUE RIVAL:")
    print("="*50)
    print(tbj)
    print("="*50 + "\n")

    