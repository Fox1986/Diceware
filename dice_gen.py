#!/usr/bin/env python
# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------------------------------------------------#

# Titel:            dice_gen.py
# Beschreibung:     Erstellen eines Passworts auf Basis des Diceware-Verfahrens
# Autor:            Hinrik Taeger
# Version:          1.0
# Kategorie:        IT-Grundschutz-Tool
# Ziel:             MacOS

# Passwörter bestehen aus Wörtern.
# Die Anzahl der Wörter kann bestimmt werden.
# Zwischen den Wörtern wird ein Spezial-Zeichen gesetzt (z.B. /()*_).
# Das Zeichen kann random oder vorgegeben werden.
# Letzteres vereinfacht das Merken.

#----------------------------------------------------------------------------------------------------------------------#

#                           Importe

import random
import string

#----------------------------------------------------------------------------------------------------------------------#

#                           Funktionen


# Hauptfunktion zur Erstellung des Passworts
def create_dice_password(pass_len, spec_char_choice):
    # Passwortlänge festlegen
    if pass_len == "":
        pass_len = 7
    else:
        pass_len = int(pass_len)
    # Die Nummern für das Finden der Wörter erstellen
    random_dic = []
    for i in range(0, pass_len):
        random_word = ""
        for j in range(0, 5):
            random_word += str(random.randint(1, 6))
        random_dic.append(random_word)
    # Die Wörter zu den Nummern finden
    password = ""
    with open("wordlist_ge.txt", "r") as file:
        lines = file.readlines()
    for word in random_dic:
        for line in lines:
            if line.startswith(word):
                # Festlegen, welche Trennzeichen zwischen den Wörtern genutzt werden
                if spec_char_choice == "":
                    spec_char = ''.join([random.choice(string.punctuation)])
                else:
                    spec_char = spec_char_choice
                # Bauen des Passworts
                password += line.strip().split(" ")[1] + spec_char
    # Rückgabe ohne den letzten Special-Character
    return password[:-1]


# Funktion zum Schreiben einer Datei für die Passwortausgabe
def write_pw_file(pwd):
    with open("password", "w") as pw_file:
        pw_file.write("Bitte Passwort in Passwort-Manager eintragen oder auswendig lernen.\n")
        pw_file.write("\n")
        pw_file.write("-----------------------------\n")
        pw_file.write("\n")
        pw_file.write(pwd)
        pw_file.write("\n")
        pw_file.write("\n")
        pw_file.write("-----------------------------\n")
        pw_file.write("\nPASSWORD-DATEI DIREKT LÖSCHEN UND NICHT AUFBEWAHREN!.\n")


#----------------------------------------------------------------------------------------------------------------------#

#                           MAIN

if __name__ == '__main__':
    # Notwendige Eingaben
    pwd_len = input("Wie viele Wörter brauchen Sie? (Enter für:7): ")
    choice = input("Bitte Trennzeichen für Wörter eingeben (Enter für:Random): ")
    # Passwort erzeugen
    pw = create_dice_password(pwd_len, choice)
    # Speichern abfragen
    save = input("Passwort Speichern? (Y/N): ")
    if save == "Y":
        write_pw_file(pw)
    else:
        print(pw)
