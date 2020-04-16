import pygame

pygame.init() # Initiation de la fenetre

screen=pygame.display.set_mode((600,700)) # Création de la fenetre de taille 600 par 700 px
pygame.display.set_caption("Morpion") # Un titre pour la fenetre

pygame.quit() # Fin de la fenetre

plateau=[[" "," "," "],[" "," "," "],[" "," "," "]] # On crée le plateau
print(plateau)
win=False # Variable de test de victoire

for i in range(9): # 9 cases --> 9 coups au max
    if win==True: # Ce morceau est répété plusieurs fois pour casser toutes les boucles si victoire
        break
    if i%2==0: # Changement de tour avec le modulo 1 sur 2 sera X, le reste O
        symbol="X"
    else:
        symbol="O"

    posX,posY=3,3
    while (not(0<=posX<=2) or not(0<=posY<=2)) or plateau[posY][posX]!=" ": # Check que la case choisie soit bien dans le tableau ET vide
        posX= int(input("Valeur de x -->"))
        posY= int(input("Valeur de y -->"))

    plateau[posY][posX]=symbol
    print(plateau)
# <-------- Passer à travers la matrice --------->
    for y in range(3):
        if win==True:
            break
        for x in range(3):
            if win==True:
                break
# <---------------------------------------------->
            if plateau[y][x]!=" ": # Si la case vérifiée est vide...
                checkSymb=plateau[y][x] # ...On en prend le symbole pour faire des tests
                compteur=0
# <----------------- Test sur la colonne ------------------->
                for col in range(3):
                    if plateau[col][x]==checkSymb: # Check une colonne
                        compteur+=1
                        if compteur==3:
                            print("Colonne")
                            win=True
                            break
# <------------------ Test sur la ligne -------------------->
                compteur=0
                for lin in range(3):
                    if plateau[y][lin]==checkSymb: # Check une ligne
                        compteur+=1
                        if compteur==3:
                            print("Ligne")
                            win=True
                            break
# <------------- Test sur la diagonnale SE/NO -------------->
                compteur=0
                for col in range(3):
                    if win==True:
                        break
                    for lin in range(3):
                        if col==lin: # Si on a 0-0, 1-1 ou 2-2...
                            if plateau[col][lin]==checkSymb: # ...On check la diagonnale
                                compteur+=1
                                if compteur==3:
                                    print("D1")
                                    win=True
                                    break
# <------------- Test sur la diagonnale SO/NE -------------->
                compteur=0
                for col in range(3):
                    if win==True:
                        break
                    for lin in range(3):
                        if col+lin==2: # Si on a 0-2, 1-1 ou 2-0...
                            if plateau[col][lin]==checkSymb: # ...On check la diagonnale
                                compteur+=1
                                if compteur==3:
                                    print("D2")
                                    win=True
                                    break

print("Le joueur gagnant est le joueur",checkSymb)
