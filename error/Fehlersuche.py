"""
Name: Error Schnitzeljagd
Autor: Tobias
Datum: 04.02.2025
Version: 1.0
"""

import random
import math
import sys

def main():
    ls = []
    hint = "n"
    count = 0

    print("+----------------------------------------------------------------------------------------------------+")
    print("|                               Willkommen bei der Error Schnitzeljagd!                              |")
    print("|                                                                                                    |")
    print("|  In diesem Spiel ist es eure Aufgabe, die Fehler im Code zu finden und zu korrigieren (debuggen).  |")
    print("+----------------------------------------------------------------------------------------------------+\n\n")


    print("1: Aufgabe 1")
    if task_1() == 0:
        sys.exit()
    else:
        ls.append("l")

    print("2: Name ausgeben")
    if print_string() == 0:
        sys.exit()
    else:
        ls.append("u")

    
    print("3: Liste ausgeben")
    if print_list() == 0:
        sys.exit()
    else:
        ls.append("j")

    
    print("4: Variable erhöhen")
    if incremention() == 0:
        sys.exit()
    else:
        ls.append("y")
    

    print("5: Division")
    if division() == 0:
        sys.exit()
    else:
        ls.append("f")


    print("6: Wurzel berechnen")
    if sqrt() == 0:
        sys.exit()
    else:
        ls.append("w")


    print("7: Zahlen ausgeben")
    if loop() == 0:
        sys.exit()
    else:
        ls.append("a")


    print("8: Kreis berechnen")
    if circle() == 0:
        sys.exit()
    else:
        ls.append("p")

    
    print("9: Bedingung überprüfen")
    if conditions() == 0:
        sys.exit()
    else:
        ls.append("v")

    ls.append("u")



    print("10: Entschlüsselt das geheime Wort")
    print("------------------------------------------------------------------------------------------------------")
    print("Das verschlüsselte Wort lautet:", ''.join(ls))
    print("Wende dich für einen Tipp an den Lernenden.")
    print("Wenn du das geheime Wort entschlüsselt hast, wende dich an den Lernenden.")
    print("------------------------------------------------------------------------------------------------------\n")


"""
Die Aufgaben beginnen hier:
"""

    
def task_1():

    """
    Aufgabe 1:
    Finde und korrigiere den Fehler.
    """

try:
    print("Aufgabe 1 gelöst!\n")
    return 1
except Exception as e:
    print("Error:", e)
    return 0

###############################################################################################

def print_string():

    """
    Aufgabe 2:
    Dein Name soll ausgegeben werden.
    """

    try:
        print("Hallo", name)
        print("Aufgabe 2 gelöst!\n")
        return 1
    except Exception as e:
        print("Error:", e)
        return 0

###############################################################################################

def print_list():

    """
    Aufgabe 3:
    Ein Eintrag aus der Liste soll ausgegeben werden.
    """

    try:
        zahlen_liste = [1, 2, 3, 4, 5]
        print(zahlen_liste[5])
        print("Aufgabe 3 gelöst!\n")
        return 1
    except Exception as e:
        print("Error:", e)
        return 0

###############################################################################################

def incremention():

    """
    Aufgabe 4:
    Der Wert einer Variable soll erhöht und ausgegeben werden.
    """

    try:
        count += 1
        print(count)
        print("Aufgabe 4 gelöst!\n")
        return 1
    except Exception as e:
        print("Error:", e)
        return 0

###############################################################################################

def division():

    """
    Aufgabe 5:
    Die Division von 2 Zahlen soll berechnet werden
    """

    a = random.randint(1, 100)
    b = 0
    try:
        result = a / b
        print(f"Die Division von {a} durch {b} ergibt {result}.\n")
        print("Aufgabe 5 gelöst!")
        return 1
    except Exception as e:
        print("Error:", e)
        return 0

###############################################################################################

def sqrt():

    """
    Aufgabe 6:
    Die Wurzel einer zufälligen Zahl soll berechnet werden.
    """

    number = random.randint(1, 100)
    try:
        result = math.sqrt(-number)
        print(f"Die Wurzel von {number} ergibt {result}.\n")
        print("Aufgabe 6 gelöst!")
        return 1
    except Exception as e:
        print("Error:", e)
        return 0

###############################################################################################

def loop():

    """
    Aufgabe 7:
    Die Zahlen 1 bis 10 sollen nacheinander ausgegeben werden.
    """

    i = 1
    while i <= 10:
        print(i)
        if i == 10:
            print("Aufgabe 7 gelöst!\n")
            return 1

###############################################################################################

def circle(radius):

    """
    Aufgabe 8:
    Die Fläche eines Kreises soll berechnet werden.
    """

    try:
        print("Die Fläche des Kreises beträgt:", math.pi * radius ** 2)
        print("Aufgabe 8 gelöst!\n")
        return 1
    except Exception as e:
        print("Error:", e)
        return 0

###############################################################################################

def conditions():
    
    """
    Aufgabe 9:
    Die Überprüfung einer Funktion soll zu einem True-Wert führen.
    """

    try:
        if conditions():
            print("Aufgabe 9 gelöst!\n")
            return 1
    except Exception as e:
        print("Error:", e)
        return 0

def condition():
    return True

###############################################################################################

if __name__ == "__main__":
    main()