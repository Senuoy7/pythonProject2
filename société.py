import datetime



def ajouterEmploye(nom, prenom, sexe, date, tel, list):
    list.append([nom, prenom, sexe, date, tel])
    return list

def menuAjouterEmploye(list):
    print("Entrez le nom de l'employé")
    nom = input()
    print("Entrez le prenom de l'employé")
    prenom = input()
    print("Entrez le sexe de l'employé")
    sexe = input()
    while sexe != "h" and sexe !="f":
        print("Erreur, entrez h ou f")
        return menuAjouterEmploye(list)
    print("Entrez la date d'arrivée de l'employé")
    year = input()
    month = input()
    day = input()
    date = datetime.date(year, month, day)
    print("Entrez son numero de telephone")
    tel = input()
    list = ajouterEmploye(nom, prenom, sexe, date, tel, list)
    afficherEmploye(list)
    return list




def supprimerEmploye(list):
    print()

def menuSupprimerEmploye(list):
    print("Par quel moyen souhaitez vous supprimer le dossier de/des employé(es) : ")
    print("1 : Supprimer par son nom")
    print("2 : Supprimer par son prenom")
    print("3 : Supprimer par son sexe")
    print("4 : Supprimer par la date d'arrivée")
    choix = input()
    match choix:
        case "1":
            suppNom(list)
        case "2":
            suppPrenom(list)
        case "3":
            suppSexe(list)
        case "4":
            suppDate(list)
    return list

def suppNom(list):
    print("Entrez le nom de l'employé que vous souhaitez supprimer")
    nom = input()

    for i in range(len(list)):
        if list[i][0] == nom:
            del list[i]
            return list

def suppPrenom(list):
    print("Entrez le prenom de l'employé que vous souhaitez supprimer")
    prenom = input()

    for i in range(len(list)):
        if list[i][1] == prenom:
            del list[i]
            return list

def suppSexe(list):
    print("Quel est le sexe des employés à supprimer ?")
    sexe = input()

    if sexe != "h" and sexe != "f":
        print("erreur entrez h ou f")
        return list

    listtmp = []
    for i in range(len(list)):
        if list[i][3] == sexe:
            listtmp.insert(0, list[i])
            return list


def suppDate(list):
    print()





def modifierEmploye(list):
    print("h")


def afficherEmploye(list):
    print(list)
    return list





















def menu():
    list = [["Bellakhal", "Younes", "h", "", "06 56 67 89 90"], ["Bernier", "Sylvie", "f", "10 Janvier 2019", "06 56 78 90 56"],
            ["Breaud", "Gaetan", "h", "28 Decembre 2021", "07 67 54 34 12"]]
    continuer = True
    while continuer:

        print("Choisissez une option : ")

        print("1 : Ajoutez le dossier d'un employé")
        print("2 : Supprimer le dossier d'un employé")
        print("3 : Modifier le dossier d'un employé")
        print("4 : Afficher la liste des employés")
        print("Q : Quitter ")
        choix = input()

        match choix:
            case "1": list = menuAjouterEmploye(list)
            case "2": list = menuSupprimerEmploye(list)
            case "3": modifierEmploye(list)
            case "4": afficherEmploye(list)
            case "Q":
                return
            case _:
                print("erreur, entrez une des options ci-dessus")
                return list






def main():
        menu()

if __name__ == '__main__':
        main()
