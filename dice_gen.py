import random
import string

long = int(input("Wie viele Wörter brauchen Sie? "))
special = input("Bitte Trennzeichen für Wörter eingeben (sonst Random):")
spec_char = special
pw = ""
random_dic = []
for i in range(0,long):
    random_word = ""
    for j in range(0,5):
        random_word += str(random.randint(1,6))
    random_dic.append(random_word)

with open("wordlist_ge.txt", "r") as file:
    lines = file.readlines()
for word in random_dic:
    for line in lines:
        if line.startswith(word):
            if special == "":
                spec_char = ''.join([random.choice(string.punctuation) for n in range(1)])
            pw += line.strip().split(" ")[1] + spec_char
with open("password", "w") as pw_file:
    pw_file.write("Bitte Passwort in Passwort-Manager eintragen oder auswendig lernen.\n")
    pw_file.write("\n")
    pw_file.write("-----------------------------\n")
    pw_file.write("\n")
    pw_file.write(pw[:-1])
    pw_file.write("\n")
    pw_file.write("\n")
    pw_file.write("-----------------------------\n")
    pw_file.write("\nPASSWORD-DATEI DIREKT LÖSCHEN UND NICHT AUFBEWAHREN!.\n")


