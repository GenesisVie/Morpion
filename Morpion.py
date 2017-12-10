import tabulate
tabulate.PRESERVE_WHITESPACE=True

reponses={'a1','a2','a3','b1','b2','b3','c1','c2','c3'}

grille = ([" "," ", " "], [" " , " ", " "], [" ", " ", " "])

def jouer(joueur):
    print("Choisir une case")
    choix = input()
    global reponses

    while choix not in reponses:
        print(choix," n'est pas une case valide")
        choix=input()

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


def has_win():

    for i in range(3):
        if grille[0][i] == grille[1][i] == grille[2][i] and grille[0][i]!=' ':
            return True
        if grille[i][0] == grille[i][1] == grille[i][2] and grille[i][0]!=' ':
            return True

    if grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0]!=' ':
        return True
    if grille[2][0] == grille[1][1] == grille[0][2] and grille[0][2]!=' ':
        return True

    return False

def main():

    joueur1="X"
    joueur2="O"
    nbtours=0

    while nbtours <= 9:
        jouer(joueur1)
        print(tabulate.tabulate(grille,tablefmt='fancy_grid'))
        #import pdb; pdb.set_trace()
        if has_win():
            print("J1 a gagné")
            return
        nbtours +=1
        jouer(joueur2)
        print(tabulate.tabulate(grille,tablefmt='fancy_grid'))
        if has_win():
            print("J2 a gagné")
            return
        nbtours +=1
    print("Match nul")

if __name__ == '__main__':
    main()
