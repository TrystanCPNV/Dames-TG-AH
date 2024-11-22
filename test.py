
#Name    : Code_perso.py
#Authors : Alex Huber
#Date    : 08.11.2024

import pygame

def affichage_plateau() :
    plateau_case = nb_ligne * nb_ligne / 2


pygame.init()

screen = pygame.display.set_mode((500, 50))
screen.fill((255,255,255))


pion = pygame.image.load("image\\MA-24_pion.png")
pion = pygame.transform.scale(pion, (50, 50))
screen.blit(pion,(0,0))

pygame.display.flip()

tbl_largeur = 10
nb_colonne = 10
nb_ligne = 10
pion_position = 0
hauteur = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pion_position = min(pion_position + 1, nb_colonne - 1)
            elif event.key == pygame.K_LEFT:
                pion_position = max(pion_position - 1, 0)


    screen.fill((255, 255, 255))
    for i in range(affichage_plateau()):
        x_case = i * 50
        y_case = 0
        if i % 2 == 0:
            pygame.draw.rect(screen, (0, 0, 0), (x_case, y_case, 50, 50))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (x_case, y_case, 50, 50))

    screen.blit(pion, (pion_position * 50, 0))

    pygame.display.flip()

pygame.quit()

