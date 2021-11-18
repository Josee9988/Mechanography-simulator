from locale import getlocale


def obtain_mechanography_language_dictionary() -> {str, str, str, str, str, str, str, str, str, str}:
    # Obtains the system language and writes the print texts in English or Spanish. The function returns the dict
    language_dict = {}
    if 'es' in getlocale():  # SPANISH 🇪🇸
        language_dict = {"Greeting": "Programa hecho por @Josee9988 | Jose Gracia Berenguer ;)\n\n",
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
    else:  # ENGLISH 🇬🇧🇺🇸
        language_dict = {"Greeting": "Script made by @Josee9988 | Jose Gracia Berenguer ;)\n\n",
                         "Text_parameter": "Introduce the text to be written: (double enter to start)\n",
                         "Error_parameter": "Introduce the rate of typos (every X +- randomness a typo will occur): ",
                         "Type_rate_parameter": "Introduce the pulsation speed (eg: 0.1): ",
                         "Type_rate_added_parameter": "Introduce typing rate to be added randomly (eg: 0.05): ",
                         "Countdown": "%sPlease, point the mouse wherever you want to write, the script will begin "
                                      "in %d seconds%s",
                         "Remaining_characters": "Characters remaining: %d     ",
                         "Writing_characters": "\n%sWriting %d characters...%s\n",
                         "Press_any": "Press any key to continue... ",
                         "Restart": "\nDo you wish to restart the script (with different data)"}
    return language_dict
