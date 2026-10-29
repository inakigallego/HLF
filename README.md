# HLF

# Hundir la Flota en Python 

Proyecto de desarrollo del clásico juego de mesa **Hundir la Flota** (*Battleship*) programado en Python utilizando matrices de numpy y random con una programación modular en consola.

---

## Descripción del Proyecto
Este proyecto simula una partida completa de Hundir la Flota entre un **Jugador** y la **Máquina**. El sistema genera tableros de 10x10, coloca los barcos de forma aleatoria (con diferentes esloras 4, 3 y 2 unidades) y gestiona los turnos de ataque, repetición por acierto, control de coordenadas, manejo de excepciones (`try...except`) y la comprobación de victoria o derrota en tiempo real.

---

## Estructura del Proyecto
El código está estructurado de manera modular para separar la lógica, las variables y la ejecución principal:

* **`main.py`**: archivo principal que inicializa los tableros, gestiona el bucle general de la partida y llama a las funciones de los turnos.
* **`Funciones.py`**: archivo que contiene toda la lógica del juego (creación de tableros, creación de barcos, posicionamiento aleatorio de barcos, validación de disparos, turnos del jugador y de la máquina, y comprobación de fin de partida).
* **`Variables.py`**: archivo donde se ubican los tableros iniciales tanto para el jugador como para el rival.

---

## Tecnologías y Librerías Utilizadas
* **Python 3.12.10**
* **NumPy 2.5.4**: para la gestión y manipulación eficiente de las matrices de los tableros.
* **Random**: para la generación aleatoria de la orientación y posición de los barcos, así como los disparos de la máquina.

---

## Cómo Ejecutar la Partida
1. Asegúrate de tener Python y la librería NumPy instalados en tu entorno de desarrollo (por ejemplo, VS Code).
2. Abre la terminal en la carpeta del proyecto.
3. Ejecuta el archivo principal con el siguiente comando:
                                                            **python main.py**