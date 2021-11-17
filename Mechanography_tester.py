#!/usr/bin/python

import pynput
import random
import time
import os

metadata = dict(
    __title__='Mechanography tester',
    __author__="Jose Gracia Berenguer",
    __email__="jgracia9988@gmail.com",
    __status__="Production",
    __copyright__='Free Software License',
    __license__='MIT',
    __version__='1.0.0',
    __summary__='A Python3 script that simulates the user typing a text on their keyboard. (control the speed, '
                'randomness, rate of typos and more!)',
    __uri__='https://jgracia.es',
)

globals().update(metadata)

KEYBOARD = pynput.keyboard.Controller()  # Create the controller
ERROR_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ` '
COLOUR_RED = "\033[1;31;40m"
COLOUR_GREEN = "\033[1;32;40m"
COLOUR_RESET = "\033[0;0m"

if os.name == 'nt':  # If we are running on Windows remove all the colours
    COLOUR_RED = COLOUR_GREEN = COLOUR_RESET = ""


def write_keyboard_with_delay_and_randomness(text: str, error: int, speed: float, speed_rate_added: float) -> None:
    error_rate = error
    i = len(text)
    for character in text:  # Loop over each character in the string
        error_rate = error_rate - random.uniform(0, 1)
        if error_rate < 0:  # type an error
            KEYBOARD.type(random.choice(ERROR_LETTERS))
            error_rate = error
        else:  # Type the character
            KEYBOARD.type(character)
        time.sleep(random.uniform(0, speed) +
                   random.uniform(0, speed_rate_added))  # Sleep for the amount of seconds generated
        i = i - 1
        print("Carácteres restantes: %d  " %
              i, end='\r')  # yes, theese spaces are useful


def yes_or_no(question) -> bool:
    reply = input(question + ' (s/n): ').lower().strip()
    if reply[0] == 'S' or reply[0] == 's':
        return True
    if reply[0] == 'N' or reply[0] == 'n':
        return False
    else:
        return yes_or_no("Por favor, introduce 's' o 'n''.")


def ask_and_execute() -> None:
    start_time = 5
    error_rate = int(
        input("Introduce cada cuántos carácteres se realizará un fallo: "))
    speed = float(input("Introduce tasa de pulsaciones (ej: 0.1): "))
    speed_rate_added = float(
        input("Introduce tasa de aleatoriedad de pulsaciones a añadir (ej: 0.05): "))
    print("Introduce el texto a escribir: (doble intro para validarlo)\n")

    text = '\n'.join(iter(input, ""))
    text_parsed = text.replace("\n", " ").strip()

    for _ in range(5):
        print("%sPor favor, situa el ratón donde desees escribir, el programa empezará en %d segundos%s"
              % (COLOUR_GREEN, start_time, COLOUR_RESET), end='\r')
        start_time = start_time - 1
        time.sleep(1)

    print("\n%sEscribiendo %d carácteres...%s\n" %
          (COLOUR_RED, len(text_parsed), COLOUR_RESET))

    write_keyboard_with_delay_and_randomness(
        text_parsed, error_rate, speed, speed_rate_added)  # Execute the function


# -- MAIN -- #

print("Programa hecho por @Josee9988 | Jose Gracia Berenguer ;)\n\n")

ask_and_execute()
input("Pulsa cualquier tecla para continuar... ")

while yes_or_no("\nDeseas volver a ejecutar el programa (con otros datos)"):
    ask_and_execute()
    input("Pulsa cualquier tecla para continuar... ")
