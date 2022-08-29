
def ajouterEmploye(nom, prenom, sexe, date, tel, list):
    list.append(nom, prenom, sexe, date, tel)

def menuAjouterEmploye(list):
    print("Entrez le nom de l'employé")
    nom = input()
    print("Entrez le prenom de l'employé")
    prenom = input()
    print("Entrez le sexe de l'employé")
    sexe = input()
    while sexe != "h" or sexe !="f":
        print("Erreur, entrez h ou f")
    print("Entrez la date d'arrivée de l'employé")
    date = input()
    print("Entrez son numero de telephone")
    tel = input()
    ajouterEmploye(nom, prenom, sexe, date, tel)
    return list



def supprimerEmploye(list):


def modifierEmploye(list):


def afficherEmploye(list):





















def menu():
    list = [[]]

    print("Choisissez une option")
    choix = input()

    print("1 : Ajoutez le dossier d'un employé")
    print("2 : Supprimer le dossier d'un employé")
    print("3 : Modifier le dossier d'un employé")
    print("4 : Afficher la liste des employés")
    print("Q : Quitter ")

    match choix:
        case "1": menuAjouterEmploye(list)
        case "2": supprimerEmploye(list)
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
