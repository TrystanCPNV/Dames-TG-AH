import pygame

nb_colonne = 10
nb_ligne = 10
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))

# Chargement et redimensionnement des images des pions
pion_blanc = pygame.image.load("MA-24_pion_blanc.png")
pion_blanc = pygame.transform.scale(pion_blanc, (50, 50))

pion_noir = pygame.image.load("MA-24_pion_noir.png")
pion_noir = pygame.transform.scale(pion_noir, (50, 50))

# Positions initiales des pions
pion_position_blanc = [0, 0]
pion_position_noir = [1, 9]

# Plateau de jeu
def plateau():
    for i in range(nb_ligne):
        for y in range(nb_colonne):
            x_case = i * 50
            y_case = y * 50
            if (i + y) % 2 == 0:
                pygame.draw.rect(screen, (255, 255, 255), (x_case, y_case, 50, 50))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (x_case, y_case, 50, 50))

# Placement des pions
def afficher_pions(pions):
    for couleur, positions in pions.items():
        pion_image = pion_blanc if couleur == "blanc" else pion_noir
        for pos in positions:
            screen.blit(pion_image, (pos[0] * 50, pos[1] * 50))


