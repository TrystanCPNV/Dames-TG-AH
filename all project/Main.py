
"""
    Nom        : Jeux_De_Dame
    Author     : Alex_trystan
    Date       : 05.12.2024
"""

import pygame
from display import plateau, afficher_pions
from rules import start, pions

if __name__ == "__main__":
    # Initialisation de Pygame
    pygame.init()

    # Création du plateau et affichage initial
    plateau()
    afficher_pions(pions)

    # Lancement de la boucle principale du jeu
    start()

    # Nettoyage et fermeture de Pygame
    pygame.quit()