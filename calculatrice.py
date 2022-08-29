import math
from math import *

def menu():
    continuer = True
    while continuer:

        print("Entrez 1 pour résolution de probleme")
        print("Entrez 2 pour untiliser la calculatrice simple")
        choix = input()
        if choix == "1":
            print ("Quel problème souhaitez vous résoudre : entrez 1 pour Pythagore / entrez 2 pour une équation du second degré")
            choix = input()
            if choix == "1":
                pythagore()
            elif choix == "2":
                equation()

        elif choix == "2":
            calculatrice()

        print("continuer ? o/n")
        reponse = input()
        if reponse == "o":
            continuer = True
        elif reponse == "n":
            continuer = False

def calculatrice():

        print("Bienvenue sur la calculate")
        print("Entrer un nombre")
        a = int(input())
        print("Entrer le deuxieme nombre")
        b = int(input())
        print("Choisir entre : plus, moins, multiple, division")
        ope = input()
        calculation(a, b, ope)

def plus(a, b):
    print("Resultat de l'addition = ", a + b)

def moins(a, b):
    print("Resultat de la soustraction = ", a - b)

def multipication(a, b):
    print("Resultat de la factorisation = ", a * b)

def division(a, b):
    print("Resultat de la division = ", a / b)

def erreur():
    print("Erreur")

def calculation(a, b, ope):
    if ope == "plus":
        plus(a, b)
    elif ope == "moins":
        moins(a, b)
    elif ope == "multiple":
        multipication(a, b)
    elif ope == "division":
        division(a, b)
    else:
        erreur()

def equation():
    print("entrez un nombre")
    a = int(input())
    print("entrez un deuxieme nombre")
    b = int(input())
    print("entrez un troisieme nombre")
    c = int(input())
    print("entrez un quatrieme nombre")
    d = int(input())
    delta = b*b - (4 * a * (c - d))

    if delta == 0:
        x1 = (-b - math.sqrt(delta))/(2*a)
    elif delta > 0:
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
    elif delta < 0:
        print("resultat impossible")
    print(x1, x2)

def pythagore():
    print("Veuillez entrer le premier côté du triangle rectangle :")
    a = input()
    a = int(a)
    print("Veuillez entrer le deuxième côté du triangle rectangle :")
    c = input()
    c = int(c)
    b = math.sqrt(a**2 + c**2)
    print(b)
    return b

def main():
    menu()

if __name__ == '__main__':
    main()