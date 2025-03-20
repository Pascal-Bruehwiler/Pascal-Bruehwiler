# Hinweise und Lösungen

## Inhaltsverzeichnis

- [Hinweise und Lösungen](#hinweise-und-lösungen)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Hinweise](#hinweise)
    - [Error-Schnitzeljagd Hinweise](#error-schnitzeljagd-hinweise)
      - [Aufgabe 1](#aufgabe-1)
      - [Aufgabe 2](#aufgabe-2)
      - [Aufgabe 3](#aufgabe-3)
      - [Aufgabe 4](#aufgabe-4)
      - [Aufgabe 5](#aufgabe-5)
      - [Aufgabe 6](#aufgabe-6)
      - [Aufgabe 7](#aufgabe-7)
      - [Aufgabe 8](#aufgabe-8)
      - [Aufgabe 9](#aufgabe-9)
      - [Aufgabe 10](#aufgabe-10)
  - [Lösungen](#lösungen)
    - [Error-Schnitzeljagd Lösungen](#error-schnitzeljagd-lösungen)

## Hinweise

### Error-Schnitzeljagd Hinweise

#### Aufgabe 1

Google, wie die Syntax von Python aussieht.

#### Aufgabe 2

Google nach einem Hello world Programm von Python.  
Google, wie man eine Variable in Python ausgeben kann.

#### Aufgabe 3

Google, wie man mit Listen (lists) in Python umgeht.

#### Aufgabe 4

Google, wie man eine Variabel inkrementieren (erhöhen) und ausgeben kann.

#### Aufgabe 5

Auf was muss man bei einer Division achten?  
Durch welche Zahl darf man nicht dividieren?

#### Aufgabe 6

Was sind die Regeln unter der Wurzel?  
Bei welchen Zahlen kann man die Wurzel nicht ziehen?

#### Aufgabe 7

Google, wie man eine while-Schleife verwendet.  
Gibt es Alternativen?  
Wie kann man das in der While-Schleife lösen?

#### Aufgabe 8

Sind alle Variabeln deklariert und iniziiert?

#### Aufgabe 9

Welche Funktion wird aufgerufen?

#### Aufgabe 10

Das Verschlüsselte Wort wurde mit der Cäsar-Verschlüsselung verschlüsselt.  
Google nach Tools, um die Verschlüsselung zu brechen (Brute Force Tools).

## Lösungen

### Error-Schnitzeljagd Lösungen

```py
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
Lösung:
Das Verschlüsselte Wort ist "encryption".
Es wurde mit der Cäsar-Verschlüsselung verschlüsselt.
Die Verschiebung beträgt 7 Zeichen.
"""


    
def task_1():

    """
    Aufgabe 1:
    Finde und korrigiere den Fehler.

    Lösung:
    IndentationError: Der Codeblock ist nicht eingerückt.
    """

    try:
        print("Aufgabe 1 gelöst!\n")
        return 1
    except Exception as e:
        print("Error:", e)
        return 0


def print_string():

    """
    Aufgabe 2:
    Dein Name soll ausgegeben werden.

    Lösung:
    Die Variable 'name' muss definiert werden.
    oder
    Der Name muss eingelesen werden
    oder
    Der Name muss direkt im print-Statement angegeben werden.
    """

    try:
        name = "Levin"
        print("Hallo", name)
        # print("Hallo Levin")

        #name = input("Gib deinen Namen ein: ")
        #print("Hallo", name)
        print("Aufgabe 2 gelöst!\n")
        return 1
    except Exception as e:
        print("Error:", e)
        return 0


def print_list():

    """
    Aufgabe 3:
    Ein Eintrag aus der Liste soll ausgegeben werden.

    Lösung:
    Der Index ist zu groß. Die Liste hat nur 5 Einträge, der Index beginnt bei 0. (Maximaler Index: 4)
    """

    try:
        zahlen_liste = [1, 2, 3, 4, 5]
        print(zahlen_liste[4])
        print("Aufgabe 3 gelöst!\n")
        return 1
    except Exception as e:
        print("Error:", e)
        return 0


def incremention():

    """
    Aufgabe 4:
    Der Wert einer Variable soll erhöht und ausgegeben werden.

    Lösung:
    Die Variable 'count' muss definiert werden.
    """

    try:
        count = 0
        count += 1
        print(count)
        print("Aufgabe 4 gelöst!\n")
        return 1
    except Exception as e:
        print("Error:", e)
        return 0


def division():

    """
    Aufgabe 5:
    Die Division von 2 Zufallszahlen soll berechnet werden

    Lösung:
    Division durch 0 ist nicht erlaubt.
    """

    a = random.randint(1, 100)
    b = random.randint(1, 100)
    try:
        result = a / b
        print(f"Die Division von {a} durch {b} ergibt {result}.\n")
        print("Aufgabe 5 gelöst!")
        return 1
    except Exception as e:
        print("Error:", e)
        return 0
    

def sqrt():

    """
    Aufgabe 6:
    Die Wurzel einer zufälligen Zahl soll berechnet werden.

    Lösung:
    Die Wurzel von negativen Zahlen kann nicht berechnet werden.
    """

    number = random.randint(1, 100)
    try:
        result = math.sqrt(number)
        print(f"Die Wurzel von {number} ergibt {result}.\n")
        print("Aufgabe 6 gelöst!")
        return 1
    except Exception as e:
        print("Error:", e)
        return 0
    

def loop():

    """
    Aufgabe 7:
    Die Zahlen 1 bis 10 sollen nacheinander ausgegeben werden.

    Lösung:
    Die Variable 'i' muss erhöht werden.
    """

    i = 1
    while i <= 10:
        print(i)
        i += 1
        if i == 10:
            print("Aufgabe 7 gelöst!\n")
            return 1


def circle(radius=5):

    """
    Aufgabe 8:
    Die Fläche eines Kreises soll berechnet werden.

    Lösung:
    Der Parameter 'radius' muss definiert werden.
    """

    try:
        print("Die Fläche des Kreises beträgt:", math.pi * radius ** 2)
        print("Aufgabe 8 gelöst!\n")
        return 1
    except Exception as e:
        print("Error:", e)
        return 0


def conditions():
    
    """
    Aufgabe 9:
    Die Überprüfung einer Funktion soll zu einem True-Wert führen.

    Lösung:
    Die Funktion ruft sich selbst auf. Das führt zu einer Rekursion und einem Stack-Overflow.
    Die aufgerufene Funktion heisst 'condition' und nicht 'conditions'.
    """

    try:
        if condition():
            print("Aufgabe 9 gelöst!\n")
            return 1
    except Exception as e:
        print("Error:", e)
        return 0

def condition():
    return True



if __name__ == "__main__":
    main()
```
