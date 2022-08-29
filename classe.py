# Gérer une feuille d'appel/classe
# Dans une classe douze apprenants
# Gérer des absences/présences
# Ajouter/Supprimer des élèves
# Groupe d'élèves
# Tri par ordre alphabétique croissant, décroissant
# Ajouter des noms, prénoms, mail, age, sexe

# Listes : d'ID -> indice de la premiere liste
# Chaque ID renvoie à une liste comportant les informations des élèves
# [["Tramoy","Raphael","tramoy.raphael@hotmail.fr",18,"H"],["Yack", "Stephanie", "yack.stephanie@outlook.fr", 18, "F"],
# [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
# Ex : print list[0][1] -> les informations de raphael : Raphael

def ajouterEleve(nom, prenom, mail, age, sexe, list):
    list.append([nom, prenom, mail, age, sexe])

    return list

def supprimerEleve(list):

    print("Quel est le nom de l eleve a supprimer? ")
    nom=input()

    for i in  range(len(list)):
        if list[i][0] == nom:
            del list[i]

    return list

def menuSuppEleve(list):
    print("De quelle manière souhaitez-vous supprimer l'élève ?")
    print("1 : Par nom")
    print("2 : Par prenom")
    print("3 : Par mail")
    print("4 : Par age")
    print("5 : Par sexe")
    choix = input()

    match choix:
        case "1": suppNom(list)
        case "2": suppPrenom(list)
        case "3": suppMail(list)
        case "4": suppAge(list)
        case "5": suppSexe(list)
        case _:
            print("erreur")

def suppNom(list):
        print("Quel est le nom de l'élève à supprimer ?")
        nom = input()

        for i in range(len(list)):
            if list[i][0] == nom:
                del list[i]
                return list

def suppPrenom(list):
        print("Quel est le prenom de l'élève à supprimer ?")
        prenom = input()

        for i in range(len(list)):
            if list[i][1] == prenom:
                del list[i]
                return list

def suppMail(list):
        print("Quel est le mail de l'élève à supprimer ?")
        mail = input()

        for i in range(len(list)):
            if list[i][4] == mail:
                del list[i]
                return list

def suppAge(list):
    print("Quel est l'age de l'élève à supprimer ?")
    age = input()
    listtmp = []
    for i in range(len(list)):
        if list[i][2] >= age:
            listtmp.insert(0, list[i])
    confirmation(listtmp, list)

def suppSexe(list):
    print("Quel est le sexe des élèves à supprimer ?")
    sexe = input()

    if sexe != "h" and sexe !="f":
        print("erreur entrez h ou f")
        return list

    listtmp = []
    for i in range(len(list)):
        if list[i][3] == sexe:
            listtmp.insert(0, list[i])
    confirmation(listtmp, list)

def confirmation(listtmp, list):
    print(listtmp)
    print("Entrez yes pour confirmer la supression ou entrez no pour quitter")
    confirmation = input()
    if confirmation == "yes":
        for j in range(len(listtmp)):
            list.remove(listtmp[j])
    elif confirmation == "no":
        return list
    return list

def absence():
    print("hello")

def presence():
    print("hello")

def triCroissant():
    print("hello")

def triDecroissant():
    print("hello")

def afficherEleves(list):
    print(list)
    return list

def menuAjoutEleve(list):
    print("entrez le nom")
    nom = input()
    print("entrez le prénom")
    prenom = input()
    print("entrez l'age")
    age = input()
    print("entrez le sexe de l'eleve")
    sexe = input()
    mail = nom + "." + prenom + "@hotmail.fr"
    print(mail)
    list = ajouterEleve(nom, prenom, mail, age, sexe, list)
    afficherEleves(list)
    return list

    # A un moment un autre, cette fonction devra appeler ajouterEleve()
    # Cette fonction demande à l'utilisateur de renseigner les informations de l'élève
    # Après l'ajout de l'élève dans la liste, le menu retournera sur la page principale (menu())

def menu():

    list = [["bellakhal", "prenom", "50", "h", "mail"], ["bernier", "prenom", "89", "f", "mail"]]
    flag = True


    print("Bonjour formateur, vous pouvez ici choisir moultes options pour gérer votre classe :")
    while flag == True:

        print("1 : Ajouter un élève")
        print("2 : Supprimer un élève")
        print("3 : Rendre présent un élève")
        print("4 : Rendre absent un élève")
        print("5 : Afficher tous les élèves")
        print("6 : Afficher les élèves dans l'ordre croisssant-alphabétique des noms")
        print("7 : Afficher les élèves dans l'ordre décroisssant-alphabétique des noms")
        print("q : Quitter")

        choix = input()

        match choix:
            case "1": list = menuAjoutEleve(list)
            case "2": list = menuSuppEleve(list)
            case "3": presence()
            case "4": absence()
            case "5": afficherEleves(list)
            case "6": triCroissant()
            case "7": triDecroissant()
            case "q": return
            case _: print("erreur entrez un chiffre entre 1 et 7, ou q pour quitter")

def main():
    menu()

if __name__ == '__main__':
    main()

