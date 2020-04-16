plateau=[[" "," "," "],[" "," "," "],[" "," "," "]]
print(plateau)
win=False

for i in range(9):
    if win==True:
        break
    if i%2==0:
        symbol="X"
    else:
        symbol="O"

    posX,posY=3,3
    while not(0<=posX<=2) or not(0<=posY<=2):
        posX= int(input("Valeur de x -->"))
        posY= int(input("Valeur de y -->"))

    plateau[posY][posX]=symbol
    print(plateau)
    for y in range(3):
        if win==True:
            break
        for x in range(3):
            if win==True:
                break
            if plateau[y][x]!=" ":
                checkSymb=plateau[y][x]
                compteur=0
                for col in range(3):
                    if plateau[col][x]==checkSymb:
                        compteur+=1
                        if compteur==3:
                            print("Colonne")
                            win=True
                            break
                compteur=0
                for lin in range(3):
                    if plateau[y][lin]==checkSymb:
                        compteur+=1
                        if compteur==3:
                            print("Ligne")
                            win=True
                            break
                compteur=0
                for col in range(3):
                    if win==True:
                        break
                    for lin in range(3):
                        if col==lin:
                            if plateau[col][lin]==checkSymb:
                                compteur+=1
                                if compteur==3:
                                    print("D1")
                                    win=True
                                    break
                compteur=0
                for col in range(3):
                    if win==True:
                        break
                    for lin in range(3):
                        if col+lin==2:
                            if plateau[col][lin]==checkSymb:
                                compteur+=1
                                if compteur==3:
                                    print("D2")
                                    win=True
                                    break

print("Le joueur gagnant est le joueur",checkSymb)