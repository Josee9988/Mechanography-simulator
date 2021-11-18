#!/usr/bin/python

from os import name
from random import uniform, choice
from time import sleep
from typing import Union

from pynput import keyboard

from Language_dictionary import obtain_mechanography_language_dictionary

globals().update(dict(
    __title__='Mechanography tester',
    __author__="Jose Gracia Berenguer",
    __email__="jgracia9988@gmail.com",
    __status__="Production",
    __copyright__='Free Software License',
    __license__='MIT',
    __version__='1.1.0',
    __summary__='A Python3 script that simulates the user typing a text on their keyboard. (control the speed, '
                'randomness, rate of typos and more!)',
    __uri__='https://jgracia.es',
))  # metadata

KEYBOARD = keyboard.Controller()  # Create the controller
LANGUAGE_OUTPUT: dict = obtain_mechanography_language_dictionary()
COUNTDOWN_TIME: int = 5  # seconds
ERROR_LETTERS: str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ` '
COLOUR_RED: str = "\033[1;31;40m"
COLOUR_GREEN: str = "\033[1;32;40m"
COLOUR_RESET: str = "\033[0;0m"

if name == 'nt':  # If we are running on Windows remove all the colours
    COLOUR_RED = COLOUR_GREEN = COLOUR_RESET = ""


def write_as_keyboard(text: str = "", error: int = 0, speed: float = 1, speed_rate_added: float = 0.5) -> None:
    error_rate: float = error
    i = len(text)
    for character in text:  # Loop over each character in the string
        error_rate = error_rate - uniform(0, 1)
        if error_rate < 0:  # type an error
            KEYBOARD.type(choice(ERROR_LETTERS))
            KEYBOARD.type(character)
            error_rate = error
        else:  # Type the character
            KEYBOARD.type(character)
        sleep(uniform(0, speed) + uniform(0, speed_rate_added))  # Sleep
        i = i - 1
        print(LANGUAGE_OUTPUT["Remaining_characters"] % i, end='\r')  # yes, theese spaces are useful


def yes_or_no(question) -> bool:
    reply: str = input(question + ' yes/no (y/n): ').lower().strip()
    if reply[0] == 'Y' or reply[0] == 'y':
        return True
    if reply[0] == 'N' or reply[0] == 'n':
        return False
    else:
        return yes_or_no("Introduce 'Y' or 'N''.")


# returns text, error, speed and speed_rate
def obtain_parameters() -> {str, Union[int, float, str]}:
    parameters: dict = {"Text": "", "Error": int(input(LANGUAGE_OUTPUT["Error_parameter"])),
                  "Speed": float(input(LANGUAGE_OUTPUT["Type_rate_parameter"])),
                  "Speed_rate_added": float(input(LANGUAGE_OUTPUT["Type_rate_added_parameter"]))}

    print(LANGUAGE_OUTPUT["Text_parameter"])

    text: str = '\n'.join(iter(input, ""))
    parameters["Text"] = text.replace("\n", " ").strip()

    return parameters


def announce_countdown(text: str, countdown_duration: int) -> None:
    for _ in range(5):
        print(LANGUAGE_OUTPUT["Countdown"] % (COLOUR_GREEN, countdown_duration, COLOUR_RESET), end='\r')
        countdown_duration = countdown_duration - 1
        sleep(1)

    print(LANGUAGE_OUTPUT["Writing_characters"] % (COLOUR_RED, len(text), COLOUR_RESET))


def main_handler() -> None:
    parameters: dict = obtain_parameters()
    announce_countdown(parameters["Text"], COUNTDOWN_TIME)
    write_as_keyboard(parameters["Text"], parameters["Error"],
                      parameters["Speed"], parameters["Speed_rate_added"])
    input(LANGUAGE_OUTPUT["Press_any"])


# -- MAIN -- #
print(LANGUAGE_OUTPUT["Greeting"])
main_handler()

while yes_or_no(LANGUAGE_OUTPUT["Restart"]):
    main_handler()
