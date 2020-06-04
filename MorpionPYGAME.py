import pygame
from random import randint

pygame.init() # Initiation de la fenetre

screen=pygame.display.set_mode((600,700)) # Création de la fenetre de taille 600 par 700 px
pygame.display.set_caption("Morpion") # Un titre pour la fenetre

fond = pygame.image.load("LignesMorpions.jpg").convert_alpha()
screen.blit(fond, (0,0))

rond = pygame.image.load("Rond.png").convert_alpha()
croix = pygame.image.load("Croix.jpg").convert_alpha()

continuer = True
plateau=[[" "," "," "],[" "," "," "],[" "," "," "]] # On crée le plateau
win=False
tour=0

WHITE=(255,255,255)
BLACK=(0,0,0)
font = pygame.font.SysFont('chalkduster.ttf', 50)

text = font.render('Tour du joueur X', True, BLACK)
screen.blit(text, (325, 630))
text = font.render('Tour du joueur O', True, WHITE)
screen.blit(text, (25, 630))

pygame.display.flip()
#Boucle infinie
while continuer:
    for event in pygame.event.get():   # On parcourt la liste de tous les événements reçus
        if event.type == pygame.QUIT:     # Si un de ces événements est de type QUIT
            continuer = False      # On arrête la boucle

    if win:
        break

    if pygame.mouse.get_pressed()[0]: # On check si click gauche
        coords = pygame.mouse.get_pos() #On prend la position du click
        x,y=0,0 # Préparation des variables de coordonnées matricielles
        caseCoords=[200,400,600] # On enregistre les limites des cases
        for i in caseCoords: # On passe dans les limites et
            if coords[0] < i: # Si on est en dessous de la limite actuelle,
                x=round((i/200)-1) # On enregistre la coordonnée matricielle qui correspond à la bonne case
                break
        for j in caseCoords: # Pareil ici
            if coords[1] < j:
                y=round((j/200)-1)
                break

        if plateau[y][x]==" ":
            print(coords)

            if tour%2==0:
                symbole="O"
                print("O")
                screen.blit(rond, (x*200+10, y*200+10))
                text = font.render('Tour du joueur O', True, BLACK)
                screen.blit(text, (25, 630))
                text = font.render('Tour du joueur X', True, WHITE)
                screen.blit(text, (325, 630))

            if tour%2==1:
                symbole="X"
                print("X")
                screen.blit(croix, (x*200+10, y*200+10))
                text = font.render('Tour du joueur X', True, BLACK)
                screen.blit(text, (325, 630))
                text = font.render('Tour du joueur O', True, WHITE)
                screen.blit(text, (25, 630))

            print(plateau)
            plateau[y][x]=symbole
            tour+=1

# <----------------- Test sur la colonne ------------------->
            compteur=0
            for col in range(3):
                if plateau[col][x]==symbole: # Check une colonne
                    compteur+=1
                    if compteur==3:
                        print("Colonne")
                        win=True
                        break
# <------------------ Test sur la ligne -------------------->
            compteur=0
            for lin in range(3):
                if plateau[y][lin]==symbole: # Check une ligne
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
                        if plateau[col][lin]==symbole: # ...On check la diagonnale
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
                        if plateau[col][lin]==symbole: # ...On check la diagonnale
                            compteur+=1
                            if compteur==3:
                                print("D2")
                                win=True
                                break
            if win:
                print("Le joueur",symbole,"à gagné")





    pygame.display.flip()

pygame.quit() # Fin de la fenetre