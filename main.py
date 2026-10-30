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

    # 3.1 TURNO DE DISPARO DEL JUGADOR
    if f.turno_disparo_jugador(tbr, tdj):
        break # Si devuelve True, he ganado y salimos del juego.

    # TURNO DE DISPARO DE LA MÁQUINA
    if f.turno_disparo_maquina(tbj):
        break # Si devuelve True, la máquina gana y salimos del juego.+

# 4 --- VISUALIZACIÓN DE MIS BARCOS TRAS EL FIN DEL TURNO RIVAL ---
print("\n" + "="*50)
print("MIRA TU TABLERO DE BARCOS (TBJ) TRAS EL ATAQUE RIVAL:")
print("="*50)
print(tbj)
print("="*50 + "\n")

