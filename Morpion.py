import tabulate
import sys
tabulate.PRESERVE_WHITESPACE=True

reponses={'a1','a2','a3','b1','b2','b3','c1','c2','c3','quit'}

grille = ([" "," ", " "], [" " , " ", " "], [" ", " ", " "])

def jouer(joueur):
    if joueur == "X":
        print("Le J1 doit choisir une case :")
    else:
        print("Le J2 doit choisir une case :")

    choix = input()

    global reponses

    while choix not in reponses:
        print(choix," n'est pas une case valide \n Choisir une autre case :")
        choix=input()

    if choix=="quit":
        if joueur == "X":
            print("Le joueur 1 n'a pas assumé :/")
            sys.exit(0)
        else:
            print("Le joueur 2 n'a pas assumé :/")
            sys.exit(0)

    if choix == "a1":
        grille[0][0] = joueur
        reponses-={'a1'}

    if choix == "a2":
        grille[0][1]=joueur
        reponses-={'a2'}

    if choix == "a3":
        grille[0][2]=joueur
        reponses-={'a3'}

    if choix == "b1":
        grille[1][0]=joueur
        reponses-={'b1'}

    if choix == "b2":
        grille[1][1]=joueur
        reponses-={'b2'}

    if choix == "b3":
        grille[1][2]=joueur
        reponses-={'b3'}

    if choix == "c1":
        grille[2][0]=joueur
        reponses-={'c1'}

    if choix == "c2":
        grille[2][1]=joueur
        reponses-={'c2'}

    if choix == "c3":
        grille[2][2]=joueur
        reponses-={'c3'}


def has_win(tab):

    for i in range(3):
        if tab[0][i] == tab[1][i] == tab[2][i] and tab[0][i]!=' ':
            return True
        if tab[i][0] == tab[i][1] == tab[i][2] and tab[i][0]!=' ':
            return True

    if tab[0][0] == tab[1][1] == tab[2][2] and tab[0][0]!=' ':
        return True
    if tab[2][0] == tab[1][1] == tab[0][2] and tab[0][2]!=' ':
        return True

    return False

def main():

    joueur1="X"
    joueur2="O"
    nbtours=0
    print("'quit' pour quitter le programme")
    while True:
        jouer(joueur1)
        print(tabulate.tabulate(grille,tablefmt='fancy_grid'))
        if has_win(grille):
            print("J1 a gagné")
            return
        nbtours +=1
        if nbtours==9:
            break
        jouer(joueur2)
        print(tabulate.tabulate(grille,tablefmt='fancy_grid'))
        if has_win(grille):
            print("J2 a gagné")
            return
        nbtours +=1
    print("Match nul")

if __name__ == '__main__':
    main()
