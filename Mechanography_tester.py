#!/usr/bin/python

import os
import random
import time
from typing import Union

import pynput

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
COUNTDOWN_TIME = 5  # seconds
ERROR_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ` '
COLOUR_RED = "\033[1;31;40m"
COLOUR_GREEN = "\033[1;32;40m"
COLOUR_RESET = "\033[0;0m"

if os.name == 'nt':  # If we are running on Windows remove all the colours
    COLOUR_RED = COLOUR_GREEN = COLOUR_RESET = ""


def write_as_keyboard(text: str = "", error: int = 0, speed: float = 1, speed_rate_added: float = 0.5) -> None:
    error_rate = error
    i = len(text)
    for character in text:  # Loop over each character in the string
        error_rate = error_rate - random.uniform(0, 1)
        if error_rate < 0:  # type an error
            KEYBOARD.type(random.choice(ERROR_LETTERS))
            error_rate = error
        else:  # Type the character
            KEYBOARD.type(character)
        time.sleep(random.uniform(0, speed) + random.uniform(0, speed_rate_added))  # Sleep
        i = i - 1
        print("Carácteres restantes: %d     " % i, end='\r')  # yes, theese spaces are useful


def yes_or_no(question) -> bool:
    reply = input(question + 'yes/no (y/n): ').lower().strip()
    if reply[0] == 'Y' or reply[0] == 'y':
        return True
    if reply[0] == 'N' or reply[0] == 'n':
        return False
    else:
        return yes_or_no("Por favor, introduce 'Y' o 'N''.")


# returns text, error, speed and speed_rate
def obtain_parameters() -> dict[str, Union[int, float, str]]:
    parameters = {"Text": "", "Error": int(
        input("Introduce cada cuántos carácteres se realizará un fallo: ")), "Speed": float(
        input("Introduce tasa de pulsaciones (ej: 0.1): ")), "Speed_rate_added": float(
        input("Introduce tasa de aleatoriedad de pulsaciones a añadir (ej: 0.05): "))}

    print("Introduce el texto a escribir: (doble intro para validarlo)\n")

    text = '\n'.join(iter(input, ""))
    parameters["Text"] = text.replace("\n", " ").strip()

    return parameters


def announce_countdown(text: str, countdown_duration: int) -> None:
    for _ in range(5):
        print("%sPor favor, situa el ratón donde desees escribir, el programa empezará en %d segundos%s"
              % (COLOUR_GREEN, countdown_duration, COLOUR_RESET), end='\r')
        countdown_duration = countdown_duration - 1
        time.sleep(1)

    print("\n%sEscribiendo %d carácteres...%s\n" %
          (COLOUR_RED, len(text), COLOUR_RESET))


def main_handler() -> None:
    parameters = obtain_parameters()
    announce_countdown(parameters["Text"], COUNTDOWN_TIME)
    write_as_keyboard(parameters["Text"], parameters["Error"],
                      parameters["Speed"], parameters["Speed_rate_added"])
    input("Pulsa cualquier tecla para continuar... ")


# -- MAIN -- #
print("Programa hecho por @Josee9988 | Jose Gracia Berenguer ;)\n\n")
main_handler()

while yes_or_no("\nDeseas volver a ejecutar el programa (con otros datos)"):
    main_handler()
