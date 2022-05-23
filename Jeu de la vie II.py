import pygame # importation de pygame qui permet de gérer l'interface graphique
import time # importation de time qui permet de mettre en pause le programme pour un durée déterminer
import sys # importation de sys qui permet ici la fermeture du jeu
import os # importation de os qui permet ici l'ouverture de fichier externe au programme
from pygame.locals import *
#initialisation de pygame
pygame.init()

police = pygame.font.Font(None,175)  #définition d'une police d'écriture
jouer = police.render("Jeu de la Vie II",1,(70,50,0))
commentjouer = police.render("Comment Jouer ?",1,(70,50,0))

valzoom=5
vitessedujeu=0.3

# creation de la fenetre de jeu
fenetre = pygame.display.set_mode((1500, 1000), pygame.RESIZABLE)

# chargement des images, elles sont stockées dans le répertoire image
pygame.display.flip()
d = pygame.image.load("image/carre.jpg")
blanc = pygame.image.load("image/blanc.jpg")
f = pygame.image.load("image/imagefond.jpg")

menutempoplay = pygame.image.load("image/menutempojeudelavie.jpg")
menutempohowto = pygame.image.load("image/menutempocommentjouer.jpg")
menubois = pygame.image.load("image/Imageboismenu.jpg")
txtinfos = pygame.image.load("image/commentJouermenu.png")



tableauattented=[]
tableauattente0=[]
nb_mini = 2
nb_maxi = 3
nb_crea_mini=3
nb_crea_maxi=3
pasdemort=0
pasdevie=0

d = pygame.transform.scale(d, (50, 50))
blanc = pygame.transform.scale(blanc, (50, 50))
principale = 1
menu=1
jeu=0
selection=0
matrice=[['h', 'h', 'h', 'h', 'h','h', 'h', 'h', 'h', 'h','h','h', 'h', 'h', 'h','h', 'h', 'h', 'h', 'h'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['p', 'p', 'p', 'p', 'p','p', 'p', 'p', 'p', 'p','p', 'p', 'p', 'p', 'p','p', 'p', 'p', 'p', 'p']]

matrice2=[['h', 'h', 'h', 'h', 'h','h', 'h', 'h', 'h', 'h','h','h', 'h', 'h', 'h','h', 'h', 'h', 'h', 'h'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['g', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', '0','0', '0', '0', '0', 'n'],
        ['p', 'p', 'p', 'p', 'p','p', 'p', 'p', 'p', 'p','p', 'p', 'p', 'p', 'p','p', 'p', 'p', 'p', 'p']]

while principale == 1:
    while menu==1:
        fenetre.blit(menubois, (0,0))
        fenetre.blit(jouer, (200,250))
        fenetre.blit(commentjouer, (200,700))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==QUIT: #Fermeture de la fenêtre (avec la croix de la fenêtre windows)
                    principale = 0 #la boucle infinie s'arrête
                    menu=0  #la boucle du menu s'arrête
                    sys.exit
                    pygame.quit() #la fenêtre se ferme

            if event.type == MOUSEBUTTONDOWN:
                x_clic=pygame.mouse.get_pos()[0]
                y_clic=pygame.mouse.get_pos()[1]
                if 200<=x_clic<=1242 and 200<=y_clic<=630: # si un clic se fait sur le bouton Jouer
                    selection = 1
                    fenetre.blit(f, (0,0))
                    fenetre.blit(menubois, (0,0))
                if 200<=x_clic<=1242 and 500<=y_clic<=930: # si un clic se fait sur le bouton pour l'aide
                    #os.startfile(r'aide.txt')   #----------------------------------------------------------------------------------------------------------------------------------------------------------
                    menu = 2

        while menu == 2:
            fenetre.blit(menubois, (0,0))
            fenetre.blit(txtinfos, (0,0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type==QUIT: #Fermeture de la fenêtre (avec la croix de la fenêtre windows)
                    principale = 0 #la boucle infinie s'arrête
                    menu=0  #la boucle du menu s'arrête
                    sys.exit
                    pygame.quit() #la fenêtre se ferme

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        menu = 1

        while selection==1:

            for i in range(len(matrice)): #Scan de la grille, et affiche de celle-ci
                for o in range(len(matrice[i])):
                    if matrice[i][o]=='d':
                        fenetre.blit(d, (valzoom*10*o,valzoom*10*i))
                        pygame.display.flip()
                    if matrice[i][o]=='0':
                        fenetre.blit(blanc, (valzoom*10*o,valzoom*10*i))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == KEYDOWN: #Pour retourner au menu
                        if event.key == K_ESCAPE:
                            matrice=matrice2
                            fenetre.blit(f, (0,0))
                            time.sleep(0.5)
                            selection = 0
                            jeu = 0

                if event.type==QUIT: #Fermeture de la fenêtre
                    principale = 0 #la boucle infinie s'arrête
                    menu=0  #la boucle du menu s'arrête
                    sys.exit
                    pygame.quit() #la fenêtre se ferme

                if event.type == MOUSEBUTTONDOWN: # Pour selection de case noir
                    if event.button == 1:
                        posisourie0=pygame.mouse.get_pos()[0]
                        posisourie1=pygame.mouse.get_pos()[1]
                        matrice[posisourie1//valzoom//10][posisourie0//valzoom//10]='d'
                        for i in range(len(matrice)): #Rescan de la grille, et affichage de la nouvelle case
                            for o in range(len(matrice[i])):
                                if matrice[i][o]=='d':
                                    fenetre.blit(d, (valzoom*10*o,valzoom*10*i))
                    pygame.display.flip()

                    if event.button == 3: # Pour selection de case blanche (supprimer)
                        posisourie0=pygame.mouse.get_pos()[0]
                        posisourie1=pygame.mouse.get_pos()[1]
                        matrice[posisourie1//valzoom//10][posisourie0//valzoom//10]='0'
                        for i in range(len(matrice)): #rescan de la grille, et affichage de la nouvelle case
                            for o in range(len(matrice[i])):
                                if matrice[i][o]=='0':
                                    fenetre.blit(blanc, (valzoom*10*o,valzoom*10*i))
                    pygame.display.flip()

                if event.type == KEYDOWN:  #Pour lancer le jeu
                    if event.key == K_SPACE:
                        menu = 0
                        selection = 0
                        jeu=1

    while jeu==1:
        pasdemort=0  #mise à zéro des variables (et liste) le nécessitant
        pasdevie=0
        aggrdessus=0
        aggrcotedroite=0
        aggrcotegauche=0
        aggrdessous=0
        caseadjacente=0 #Initialisation du jeu
        nombred=0
        longueur=0
        largeur=0
        pasconti=0
        matricpouraggr=[]
        matricpouraggr2=[]
        tableauattented=[]
        tableauattente0=[]

        for event in pygame.event.get():
            if event.type == KEYDOWN: #Pour retourner au menu
                if event.key == K_ESCAPE:
                    matrice=matrice2
                    fenetre.blit(f, (0,0))
                    time.sleep(0.5)
                    menu = 1
                    jeu = 0

                if event.key == K_UP:   #Pour ajuster la vitesse du jeu (ici le rendre plus rapide)
                    if vitessedujeu > 0.1:
                        vitessedujeu = vitessedujeu-0.1
                if event.key == K_DOWN:   #(ici le rendre plus lent)
                    if vitessedujeu < 1:
                        vitessedujeu = vitessedujeu+0.1

            if event.type==QUIT: #Fermeture de la fenêtre
                principale = 0 #la boucle infinie s'arrête
                menu=0  #la boucle menu s'arrête
                jeu=0
                sys.exit
                pygame.quit() #la fenêtre se ferme

            if event.type == MOUSEBUTTONDOWN: # Pour Zoom
                if event.button == 4: #zoom avant
                    valzoom=valzoom+1
                    fenetre.blit(menubois, (0,0))
                    pygame.display.flip()
                if valzoom > 1:
                    if event.button == 5: #zoom arrière
                        valzoom=valzoom-1
                        fenetre.blit(menubois, (0,0))
                        pygame.display.flip()

        for i in range(len(matrice)): #Scan de la grille
            for o in range(len(matrice[i])):
                caseadjacente=0
                if matrice[i][o]=='0':     #Si morte, scan des alentours, et application de la règles
                    if matrice[i+1][o]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i-1][o]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i][o+1]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i+1][o+1]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i-1][o+1]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i][o-1]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i+1][o-1]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i-1][o-1]=='d':
                        caseadjacente=caseadjacente+1
                    if caseadjacente==3:         #la dite règle
                        tableauattented.append([i,o])  #Mise des coordonnée dans tableau (pour pouvoir toute les faire vivre d'un seul coup)
                        pasdevie = pasdevie+1


                if matrice[i][o]=='d':      #Si vivante, scan des alentours, et application de la règles
                    nombred=nombred+1       #Pour compter le nombre de case vivante.
                    if matrice[i+1][o]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i-1][o]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i][o+1]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i+1][o+1]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i-1][o+1]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i][o-1]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i+1][o-1]=='d':
                        caseadjacente=caseadjacente+1
                    if matrice[i-1][o-1]=='d':
                        caseadjacente=caseadjacente+1
                    if caseadjacente<2 or caseadjacente>3:  #la dite règle
                        tableauattente0.append([i,o])  #Mise des coordonnée dans tableau (pour pouvoir toute les tuer d'un seul coup)
                        pasdemort = pasdemort+1

                if matrice[i][o]=='h':  #voir si cellule en vie proche de la bordure du haut
                    if matrice[i+2][o]=='d':
                        aggrdessus = aggrdessus + 1 #ajout d'un valeur, qui permettra d'entrer dans la partie permettant l'agrandissment
                if matrice[i][o]=='g':  #voir si cellule en vie proche de la bordure de gauche
                    if matrice[i][o+2]=='d':
                        aggrcotegauche = aggrcotegauche + 1
                if matrice[i][o]=='p':  #voir si cellule en vie proche de la bordure du bas
                    if matrice[i-2][o]=='d':
                        aggrdessous = aggrdessous + 1
                if matrice[i][o]=='n':  #voir si cellule en vie proche de la bordure de droite
                    if matrice[i][o-2]=='d':
                        aggrcotedroite = aggrcotedroite + 1

        longueur=0
        largeur=0
        for o in range(len(matrice[0])):  #calcul de la longeur (horizontal) de la grille
            longueur=longueur + 1
        for i in range(len(matrice)):  #calcul de la largeur (hauteur) de la grille
            largeur = largeur + 1

        if aggrdessus >= 1:  #Agrangissement au dessus (à cause de la position des case (en haut à gauche), on a l'impression que l'agrandissment ce déroule en dessous, ça n'est pas le cas dans la matrice)
            matrice[0][0]='g'
            for i in range(longueur-2):
                matrice[0][1+i]='0'
            matrice[0][longueur-1]='n'
            for j in range(longueur):
                matricpouraggr.append('h')
            matrice.insert(0, matricpouraggr)
            pasconti=1

        longueur=0
        largeur=0
        for o in range(len(matrice[0])):  #calcul de la longeur (horizontal) de la grille
            longueur=longueur + 1
        for i in range(len(matrice)):  #calcul de la largeur (hauteur) de la grille
            largeur = largeur + 1

        if aggrcotegauche >= 1:  #Agrangissement au dessus (à cause de la position des case (en haut à gauche), on a l'impression que l'agrandissment ce déroule en dessous, ça n'est pas le cas dans la matrice)
            for i in range(largeur-2):
                matrice[1+i][0]='0'
            matrice[largeur-1][0]='n'
            matrice[0].insert(0, 'h')
            for j in range(largeur-2):
                matrice[1+j].insert(0,'g')
            matrice[largeur-1].insert(0, 'p')
            pasconti=1

        longueur=0
        largeur=0
        for o in range(len(matrice[0])):  #calcul de la longeur (horizontal) de la grille
            longueur=longueur + 1
        for i in range(len(matrice)):  #calcul de la largeur (hauteur) de la grille
            largeur = largeur + 1

        if aggrdessous >= 1:  #Agrangissement au dessus (à cause de la position des case (en haut à gauche), on a l'impression que l'agrandissment ce déroule en dessous, ça n'est pas le cas dans la matrice)
            matrice[largeur-1][0]='g'
            for i in range(longueur-2):
                matrice[largeur-1][1+i]='0'
            matrice[largeur-1][longueur-1]='n'
            for j in range(longueur):
                matricpouraggr.append('p')
            matrice.insert(largeur, matricpouraggr)
            pasconti=1
            print(matrice)

        longueur=0
        largeur=0
        for o in range(len(matrice[0])):  #calcul de la longeur (horizontal) de la grille
            longueur=longueur + 1
        for i in range(len(matrice)):  #calcul de la largeur (hauteur) de la grille
            largeur = largeur + 1

        if aggrcotedroite >= 1:  #Agrangissement au dessus (à cause de la position des case (en haut à gauche), on a l'impression que l'agrandissment ce déroule en dessous, ça n'est pas le cas dans la matrice)
            for i in range(largeur-2):
                matrice[i+1][longueur-1]='0'
            matrice[0].append('h')
            matrice[largeur-1].append('p')
            for j in range(largeur-2):
                matrice[j+1].append('n')
            print(matrice)

        if nombred==0 :   #Si il n'y a plus de case en vie
            matrice=matrice2
            fenetre.blit(f, (0,0))
            time.sleep(1)
            menu = 1
            jeu =0

        if pasdemort==0 and pasdevie==0 : #Si il n'y a plus de mouvements (de case qui doivent vivre ou doivent mourir)
            fenetre.blit(f, (0,0))
            time.sleep(1)
            menu = 1
            jeu =0
            matrice=matrice2

        if pasconti==0:
            for j in range(len(tableauattented)):    #Application règle pour faire naitre
                val1=tableauattented[j][0]
                val2=tableauattented[j][1]
                matrice[val1][val2]='d'

            for e in range(len(tableauattente0)):    #Application règle pour tuer
                val1=tableauattente0[e][0]
                val2=tableauattente0[e][1]
                matrice[val1][val2]='0'

        for i in range(len(matrice)): #Scan de la grille, et nouvelle affichage des cases
            for o in range(len(matrice[i])):
                if matrice[i][o]=='d':
                    d = pygame.transform.scale(d, (valzoom*10, valzoom*10))
                    fenetre.blit(d, (valzoom*10*o,valzoom*10*i))
                    pygame.display.flip()
                if matrice[i][o]=='0':
                    blanc = pygame.transform.scale(blanc, (valzoom*10, valzoom*10))
                    fenetre.blit(blanc, (valzoom*10*o,valzoom*10*i))
                    pygame.display.flip()

##            time.sleep(vitessedujeu)  #Pour test et debug
        pygame.display.flip()

#Vous nous aviez demander pourquoi tout dans un même boucle, c'est simplement pour pouvoir revenir au menu à n'importe qu'elle moment, sans uiliser de boucle infinie externe, ce que nous avons déjà essayer, et ce qui n'a pas très bien marché.