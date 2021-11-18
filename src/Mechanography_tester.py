#!/usr/bin/python

import locale
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
LANGUAGE_OUTPUT = {}

if os.name == 'nt':  # If we are running on Windows remove all the colours
    COLOUR_RED = COLOUR_GREEN = COLOUR_RESET = ""

if 'es' in locale.getlocale():  # spanish
    LANGUAGE_OUTPUT = {"Greeting": "Programa hecho por @Josee9988 | Jose Gracia Berenguer ;)\n\n",
                       "Text_parameter": "Introduce el texto a escribir: (doble intro para validarlo)\n",
                       "Error_parameter": "Introduce cada cuántos carácteres se realizará un fallo (cada X +- un "
                                          "ratio aleatorio para que ocurra un error tipográfico): ",
                       "Type_rate_parameter": "Introduce tasa de pulsaciones (ej: 0.1): ",
                       "Type_rate_added_parameter": "Introduce tasa de aleatoriedad de pulsaciones a añadir (ej: "
                                                    "0.05): ",
                       "Countdown": "%sPor favor, situa el ratón donde desees escribir, el programa empezará en %d "
                                    "segundos%s",
                       "Remaining_characters": "Carácteres restantes: %d     ",
                       "Writing_characters": "\n%sEscribiendo %d carácteres...%s\n",
                       "Press_any": "Pulsa cualquier tecla para continuar... ",
                       "Restart": "\nDeseas volver a ejecutar el programa (con otros datos)"}
else:  # english
    LANGUAGE_OUTPUT = {"Greeting": "Script made by @Josee9988 | Jose Gracia Berenguer ;)\n\n",
                       "Text_parameter": "Introduce the text to be written: (double enter to start)\n",
                       "Error_parameter": "Introduce the rate of typos (every X +- randomness a typo will occur): ",
                       "Type_rate_parameter": "Introduce the pulsation speed (eg: 0.1): ",
                       "Type_rate_added_parameter": "Introduce typing rate to be added randomly (eg: 0.05): ",
                       "Countdown": "%sPlease, point the mouse wherever you want to write, the script will begin in "
                                    "%d seconds%s",
                       "Remaining_characters": "Characters remaining: %d     ",
                       "Writing_characters": "\n%sWriting %d characters...%s\n",
                       "Press_any": "Press any key to continue... ",
                       "Restart": "\nDo you wish to restart the script (with different data)"}


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
        print(LANGUAGE_OUTPUT["Remaining_characters"] % i, end='\r')  # yes, theese spaces are useful


def yes_or_no(question) -> bool:
    reply = input(question + ' yes/no (y/n): ').lower().strip()
    if reply[0] == 'Y' or reply[0] == 'y':
        return True
    if reply[0] == 'N' or reply[0] == 'n':
        return False
    else:
        return yes_or_no("Introduce 'Y' or 'N''.")


# returns text, error, speed and speed_rate
def obtain_parameters() -> dict[str, Union[int, float, str]]:
    parameters = {"Text": "", "Error": int(input(LANGUAGE_OUTPUT["Error_parameter"])),
                  "Speed": float(input(LANGUAGE_OUTPUT["Type_rate_parameter"])),
                  "Speed_rate_added": float(input(LANGUAGE_OUTPUT["Type_rate_added_parameter"]))}

    print(LANGUAGE_OUTPUT["Text_parameter"])

    text = '\n'.join(iter(input, ""))
    parameters["Text"] = text.replace("\n", " ").strip()

    return parameters


def announce_countdown(text: str, countdown_duration: int) -> None:
    for _ in range(5):
        print(LANGUAGE_OUTPUT["Countdown"] % (COLOUR_GREEN, countdown_duration, COLOUR_RESET), end='\r')
        countdown_duration = countdown_duration - 1
        time.sleep(1)

    print(LANGUAGE_OUTPUT["Writing_characters"] % (COLOUR_RED, len(text), COLOUR_RESET))


def main_handler() -> None:
    parameters = obtain_parameters()
    announce_countdown(parameters["Text"], COUNTDOWN_TIME)
    write_as_keyboard(parameters["Text"], parameters["Error"],
                      parameters["Speed"], parameters["Speed_rate_added"])
    input(LANGUAGE_OUTPUT["Press_any"])


# -- MAIN -- #
print(LANGUAGE_OUTPUT["Greeting"])
main_handler()

while yes_or_no(LANGUAGE_OUTPUT["Restart"]):
    main_handler()
