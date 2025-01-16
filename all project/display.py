"""
    Nom        : Jeux_De_Dame
    Author     : Alex_trystan
    Date       : 05.12.2024
"""

import pygame

# Définition des dimensions du plateau
nb_colonne = 10
nb_ligne = 10

# Création de la fenêtre de jeu avec une taille de 500x500 pixels
screen = pygame.display.set_mode((500, 500))

# Remplissage initial de l'écran en blanc
screen.fill((255, 255, 255))

# Chargement et redimensionnement des images des pions
pion_blanc = pygame.image.load("MA-24_pion_blanc.png")  # Chargement de l'image du pion blanc
pion_blanc = pygame.transform.scale(pion_blanc, (50, 50))  # Redimensionnement de l'image à 50x50 pixels

pion_noir = pygame.image.load("MA-24_pion_noir.png")  # Chargement de l'image du pion noir
pion_noir = pygame.transform.scale(pion_noir, (50, 50))  # Redimensionnement de l'image à 50x50 pixels


# Fonction pour dessiner le plateau de jeu
def plateau():
    for i in range(nb_ligne):  # Parcours des lignes
        for y in range(nb_colonne):  # Parcours des colonnes
            x_case = i * 50  # Calcul de la position x de la case
            y_case = y * 50  # Calcul de la position y de la case
            # Alternance des couleurs (blanc et noir) selon la position
            if (i + y) % 2 == 0:
                pygame.draw.rect(screen, (255, 255, 255), (x_case, y_case, 50, 50))  # Case blanche
            else:
                pygame.draw.rect(screen, (0, 0, 0), (x_case, y_case, 50, 50))  # Case noire


# Fonction pour afficher les pions sur le plateau
def afficher_pions(pions, pion_selectionne=None):
    for couleur, positions in pions.items():  # Parcours des pions par couleur et positions
        # Sélection de l'image du pion selon sa couleur
        pion_image = pion_blanc if couleur == "blanc" else pion_noir
        for pos in positions:  # Parcours des positions de chaque pion
            # Placement de l'image du pion sur la case correspondante
            screen.blit(pion_image, (pos[0] * 50, pos[1] * 50))

    # Si un pion est sélectionné, dessiner un contour rouge autour
    if pion_selectionne:
        _, pion = pion_selectionne  # Récupération des coordonnées du pion sélectionné
        pygame.draw.rect(screen, (255, 0, 0), (pion[0] * 50, pion[1] * 50, 50, 50), 3)  # Contour rouge
