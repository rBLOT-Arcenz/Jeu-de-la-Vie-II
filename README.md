# Jeu-de-la-Vie-II

Ce "Jeu de la Vie II" avec moins de fonctionnalités que le jeu de base (Celui de Conway) est le 1er projet que j'ai du rendre en 1ère.
Il s'agit d'un jeu de la vie sous Pygame, tout simplement.
Le principe du "jeu" est simple. Au début, vous vous retrouvé avec une grille vide. Dans celle-ci, vous pouvez doser des cellules avec clique gauche (clique droit pour les effacer), puis appuyez sur entrée pour lancer le jeu. Ensuite, les cellules se "déplacerons" celon certaines règles :

    -Si une case vide à 3 cellules à côté d'elle, elle devient vivante.
    
    -Si une case à exactement 2 cellules à côté d'elle, elle reste dans son état.
    
    -Si une celulle à moins de 2, ou plus de 3 cellules à côté d'elle, elle meurt.
    
En jeu, échap retourne au menu, les flèche du haut et du bas augmentent et baissent la vitesse du jeu, et la molette elle permet de zoomer et de dézoomer.

NOTE : Je n'ai pu retrouver la version finale du jeu, la version que vous voyez donc ici est une plus vieille, tout de même assez buggée (plante si le tableau devient trop grand)
