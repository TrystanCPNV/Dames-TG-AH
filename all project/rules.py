"""
    Nom        : Jeux_De_Dame
    Author     : Alex_trystan
    Date       : 05.12.2024
"""

import pygame
from display import plateau, afficher_pions  # Importation des modules pour l'affichage

# Initialisation des positions des pions
pions = {
    "blanc": [[1, 0], [3, 0], [5, 0], [7, 0], [9, 0],
              [0, 1], [2, 1], [4, 1], [6, 1], [8, 1],
              [1, 2], [3, 2], [5, 2], [7, 2], [9, 2],
              [0, 3], [2, 3], [4, 3], [6, 3], [8, 3]],  # Positions des pions blancs

    "noir": [[0, 9], [2, 9], [4, 9], [6, 9], [8, 9],
             [1, 8], [3, 8], [5, 8], [7, 8], [9, 8],
             [0, 7], [2, 7], [4, 7], [6, 7], [8, 7],
             [1, 6], [3, 6], [5, 6], [7, 6], [9, 6]]  # Positions des pions noirs
}

# Variable pour stocker le pion ou la dame sélectionné(e)
pion_selectionne = None

tour = "blanc"  # Le joueur "blanc" commence

# Chargement des images des pions et dames
image_pion_blanc = pygame.image.load("MA-24_pion_blanc.png")
image_pion_blanc = pygame.transform.scale(image_pion_blanc, (50, 50))  # Redimensionner l'image du pion blanc

image_pion_noir = pygame.image.load("MA-24_pion_noir.png")
image_pion_noir = pygame.transform.scale(image_pion_noir, (50, 50))  # Redimensionner l'image du pion noir

image_dame_blanche = pygame.image.load("MA-24_dame_blanche.png")
image_dame_blanche = pygame.transform.scale(image_dame_blanche, (50, 50))  # Redimensionner l'image de la dame blanche

image_dame_noire = pygame.image.load("MA-24_dame_noire.png")
image_dame_noire = pygame.transform.scale(image_dame_noire, (50, 50))  # Redimensionner l'image de la dame noire

# Création de l'écran
fenetre = pygame.display.set_mode((500, 500))  # Fenêtre de 500x500 pixels


def selectionner_pion(position): #def fait part chatpgt
    """Sélectionne un pion ou une dame à la position donnée."""
    global pion_selectionne
    for couleur, positions in pions.items():  # Parcours des positions des pions
        for pion in positions:
            if pion[:2] == position:  # Si la position du pion correspond à la case cliquée
                if couleur == tour:  # Vérifie que c'est le tour de la bonne couleur
                    pion_selectionne = (couleur, pion)  # Sélectionne le pion
                    return True
    return False  # Aucun pion trouvé à cette position


def peut_manger(pion, couleur): #def fait part chatpgt
    """Vérifie si un pion ou une dame peut effectuer une capture."""
    directions = [(-2, -2), (2, -2), (-2, 2), (2, 2)]  # Directions de capture pour un pion normal
    if "dame" in pion:
        # Directions pour une dame (peut se déplacer et capturer dans toutes les directions)
        directions = [(-i, -i) for i in range(1, 10)] + [(i, -i) for i in range(1, 10)] + \
                     [(-i, i) for i in range(1, 10)] + [(i, i) for i in range(1, 10)]

    for dx, dy in directions:
        nouvelle_pos = [pion[0] + dx, pion[1] + dy]  # Nouvelle position après déplacement
        x_mange = pion[0] + dx // 2 if abs(dx) == 2 else None  # Position du pion mangé en x
        y_mange = pion[1] + dy // 2 if abs(dy) == 2 else None  # Position du pion mangé en y
        pion_mange = [x_mange, y_mange] if x_mange is not None and y_mange is not None else None  # Position du pion capturé

        # Vérification si la nouvelle position est valide et s'il y a bien un pion à manger
        if (0 <= nouvelle_pos[0] < 10 and 0 <= nouvelle_pos[1] < 10 and
                (pion_mange is None or
                 any(pion_mange in positions for c, positions in pions.items() if c != couleur)) and
                not any(nouvelle_pos in positions for positions in pions.values())):
            return True
    return False  # Pas de capture possible


def deplacer_pion(nouvelle_pos): #def fait part chatpgt
    """Déplace un pion ou une dame si le déplacement est valide."""
    global pion_selectionne, tour
    if pion_selectionne:
        couleur, pion = pion_selectionne
        dx = nouvelle_pos[0] - pion[0]  # Calcul du déplacement en x
        dy = nouvelle_pos[1] - pion[1]  # Calcul du déplacement en y

        if abs(dx) == 1 and abs(dy) == 1 and "dame" not in pion:
            # Déplacement simple (pion uniquement)
            if not any(nouvelle_pos in positions for positions in pions.values()):
                pion[0], pion[1] = nouvelle_pos  # Déplacement du pion
                verifier_promotion(pion, couleur)  # Vérifie si le pion doit être promu
                pion_selectionne = None
                tour = "noir" if tour == "blanc" else "blanc"  # Change le tour

        elif abs(dx) == 2 and abs(dy) == 2:
            # Capture (déplacement de deux cases)
            x_mange = (pion[0] + nouvelle_pos[0]) // 2
            y_mange = (pion[1] + nouvelle_pos[1]) // 2
            pion_mange = [x_mange, y_mange]

            if any(pion_mange in positions for c, positions in pions.items() if c != couleur):
                # Retire le pion capturé
                for c in pions:
                    if pion_mange in pions[c]:
                        pions[c].remove(pion_mange)
                        break

                # Déplace le pion
                pion[0], pion[1] = nouvelle_pos
                verifier_promotion(pion, couleur)

                # Vérifie si une autre capture est possible
                if peut_manger(pion, couleur):
                    pion_selectionne = (couleur, pion)
                else:
                    pion_selectionne = None
                    tour = "noir" if tour == "blanc" else "blanc"  # Change le tour

        elif "dame" in pion:
            # Déplacement pour les dames
            if all(0 <= nouvelle_pos[i] < 10 for i in range(2)) and not any(
                    nouvelle_pos in positions for positions in pions.values()):
                delta_x = 1 if dx > 0 else -1
                delta_y = 1 if dy > 0 else -1
                x, y = pion[0] + delta_x, pion[1] + delta_y

                valid_move = True
                pion_mange = None

                while (x, y) != tuple(nouvelle_pos):
                    if any([x, y] in positions for positions in pions.values()):
                        if pion_mange is None and any(
                                [x, y] in positions for c, positions in pions.items() if c != couleur):
                            pion_mange = [x, y]
                        else:
                            valid_move = False
                            break
                    x += delta_x
                    y += delta_y

                if valid_move:
                    if pion_mange:
                        for c in pions:
                            if pion_mange in pions[c]:
                                pions[c].remove(pion_mange)
                                break

                    pion[0], pion[1] = nouvelle_pos

                    if peut_manger(pion, couleur):
                        pion_selectionne = (couleur, pion)
                    else:
                        pion_selectionne = None
                        tour = "noir" if tour == "blanc" else "blanc"  # Change le tour


def verifier_promotion(pion, couleur): #def fait part chatpgt
    """Vérifie si un pion doit être promu en dame."""
    if (couleur == "blanc" and pion[1] == 9) or (couleur == "noir" and pion[1] == 0):
        pion.append("dame")  # Ajoute "dame" à la position du pion pour le promouvoir


def afficher_pions(pions, pion_selectionne=None): #l'image hoisie en fonctino du type du pino fait par gpt le reste fait par nous
    """Affiche les pions et les dames sur le plateau."""
    for couleur, positions in pions.items():
        for pion in positions:
            # Choix de l'image en fonction du type de pion
            if "dame" in pion:
                image = image_dame_blanche if couleur == "blanc" else image_dame_noire
            else:
                image = image_pion_blanc if couleur == "blanc" else image_pion_noir
            fenetre.blit(image, (pion[0] * 50, pion[1] * 50))  # Affichage des pions à leur position

        # Affiche un contour rouge autour du pion sélectionné
        if pion_selectionne:
            _, pion = pion_selectionne
            pygame.draw.rect(fenetre, (255, 0, 0), (pion[0] * 50, pion[1] * 50, 50, 50), 3)


def mouvement():
    """Gère les événements de jeu."""
    global pion_selectionne
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # Quitte le jeu
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            position = [x // 50, y // 50]  # Conversion des coordonnées de la souris en position sur le plateau
            if not selectionner_pion(position):
                if pion_selectionne:
                    deplacer_pion(position)  # Déplace le pion sélectionné
                    pion_selectionne = None
    plateau()  # Affiche le plateau
    afficher_pions(pions, pion_selectionne)  # Affiche les pions
    pygame.display.flip()  # Met à jour l'écran


def start():
    """Démarre le jeu."""
    running = True
    while running:
        mouvement()  # Gère le mouvement des pions et la mise à jour du jeu
