import Variables as v
import Funciones as f

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
    print("ESTADO DE MI FLOTA (TBJ):")
    print(tbj)
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