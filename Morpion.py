import tabulate

affichage = tabulate.tabulate(grille,tablefmt='fancy_grid')

def joueur1(choix):
    choix = input()
    if choix == "a1":
        grille [0 , 0] = "X"

    if choix == "a2":
        grille[0,1]="X"

    if choix == "a3":
        grille[0,2]="X"

    if choix == "b1":
        grille[1,0]="X"

    if choix == "b2":
        grille[1,1]="X"

    if choix == "b3":
        grille[1,2]="X"

    if choix == "c1":
        grille[2,0]="X"

    if choix == "c2":
        grille[2,1]="X"

    if choix == "c3":
        grille[2,2]="X"

        &taberror=[]
        for i in taberror
            taberror[i]=choix

def joueur2(choix):
    choix = input()
    if choix == "a1":
        grille[0,0]="O"

    if choix == "a2":
        grille[0,1]="O"

    if choix == "a3":
        grille[0,2]="O"

    if choix == "b1":
        grille[1,0]="O"

    if choix == "b2":
        grille[1,1]="O"

    if choix == "b3":
        grille[1,2]="O"

    if choix == "c1":
        grille[2,0]="O"

    if choix == "c2":
        grille[2,1]="O"

    if choix == "c3":
        grille[2,2]="O"

def Partie():
    termine=False
#Conditions pour que J1 gagne
    if grille[0,0]=="X" and grille[0,1]=="X" and grille[0,2]=="X"
        termine=True
    if grille[1,0]=="X" and grille[1,1]=="X" and grille[1,2]=="X"
        termine=True
    if grille[2,0]=="X" and grille[2,1]=="X" and grille[2,2]=="X"
        termine=True
    if grille[0,0]=="X" and grille[1,1]=="X" and grille[2,2]=="X"
        termine=True
    if grille[0,2]=="X" and grille[1,1]=="X" and grille[2,0]=="X"
        termine=True

#Conditions pour que J2 gagne
    if grille[0,0]=="O" and grille[0,1]=="O" and grille[0,2]=="O"
        termine=True
    if grille[1,0]=="O" and grille[1,1]=="O" and grille[1,2]=="O"
        termine=True
    if grille[2,0]=="O" and grille[2,1]=="O" and grille[2,2]=="O"
        termine=True
    if grille[0,0]=="O" and grille[1,1]=="O" and grille[2,2]=="O"
        termine=True
    if grille[0,2]=="O" and grille[1,1]=="O" and grille[2,0]=="O"
        termine=True

