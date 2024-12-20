import pygame
from display import screen, plateau, afficher_pions

# Initialisation des positions des pions
pions = {
    "blanc": [[0, 0], [2, 0], [4, 0], [6, 0], [8, 0]],
    "noir": [[1, 9], [3, 9], [5, 9], [7, 9], [9, 9]]
}

# Pion sélectionné
pion_selectionne = None

def selectionner_pion(position):
    global pion_selectionne
    for couleur, positions in pions.items():
        for pion in positions:
            if pion == position:
                pion_selectionne = (couleur, pion)
                return True
    return False

def deplacer_pion(direction):
    global pion_selectionne
    if pion_selectionne:
        couleur, pion = pion_selectionne
        if direction == "bas_gauche" and pion[0] > 0 and pion[1] < 9:
            pion[0] -= 1
            pion[1] += 1
        elif direction == "bas_droite" and pion[0] < 9 and pion[1] < 9:
            pion[0] += 1
            pion[1] += 1
        elif direction == "haut_gauche" and pion[0] > 0 and pion[1] > 0:
            pion[0] -= 1
            pion[1] -= 1
        elif direction == "haut_droite" and pion[0] < 9 and pion[1] > 0:
            pion[0] += 1
            pion[1] -= 1

def mouvement():
    global pion_selectionne
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            position = [x // 50, y // 50]
            selectionner_pion(position)
        elif event.type == pygame.KEYDOWN:
            if pion_selectionne:
                if event.key == pygame.K_RIGHT:
                    deplacer_pion("bas_droite")
                elif event.key == pygame.K_LEFT:
                    deplacer_pion("bas_gauche")
                elif event.key == pygame.K_UP:
                    deplacer_pion("haut_gauche")
                elif event.key == pygame.K_DOWN:
                    deplacer_pion("haut_droite")
                pion_selectionne = None

def start():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        plateau()
        afficher_pions(pions)
        mouvement()
        pygame.display.flip()