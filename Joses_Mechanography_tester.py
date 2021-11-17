#!/usr/bin/python

import pynput
import random
import time

metadata = dict(
    __title__='Jose mechanography tester',
    __author__="Jose Gracia Berenguer",
    __email__="jgracia9988@gmail.com",
    __status__="Production",
    __copyright__='MIT',
    __license__='MIT',
    __version__='1.0.0',
    __summary__='Program to write as if it were the keyboard to test mechanography programs and pretend that you are writing (super fast)',
    __uri__='https://jgracia.es',
)

globals().update(metadata)

KEYBOARD = pynput.keyboard.Controller()  # Create the controller
ERROR_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ` '


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
        i = i-1
        print("Carácteres restantes: %d" % (i), end='\r')


def yes_or_no(question) -> bool:
    reply = input(question+' (s/n): ').lower().strip()
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
    print(("Introduce el texto a escribir: (doble intro para validarlo)\n"))

    text = '\n'.join(iter(input, ""))
    text_parsed = text.replace("\n", " ").strip()

    for _ in range(5):
        print("\033[1;32;40mPor favor, situa el ratón donde desees escribir, el programa empezará en %d segundos\033[0;0m" %
              start_time, end='\r')
        start_time = start_time - 1
        time.sleep(1)

    print("\n\033[1;31;40mEscribiendo %s carácteres...\033[0;0m\n" %
          len(text_parsed))

    write_keyboard_with_delay_and_randomness(
        text_parsed, error_rate, speed, speed_rate_added)  # Execute the function


### MAIN ###

print("Programa hecho por @Josee9988 \ Jose Gracia Berenguer ;)\n\n")

ask_and_execute()
input("Pulsa cualquier tecla para continuar... ")

while(yes_or_no("\nDeseas volver a ejecutar el programa (con otros datos)")):
    ask_and_execute()
    input("Pulsa cualquier tecla para continuar... ")
