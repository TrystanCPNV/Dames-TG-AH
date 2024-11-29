"""
    Nom        : Jeux_De_Dame
    Author     : Alex_trystan
    Date       : 28.11.2024
"""

import pygame

pygame.init()


def deplacer_pion_b_g():
        if pion_position_blanc[0] == 9:
            pion_position_blanc[0] = 9
        elif pion_position_blanc[1] == 9:
            pion_position_blanc[0] = pion_position_blanc[0]
        else:
            pion_position_blanc[0] = min(pion_position_blanc[0] + 1, nb_colonne - 1)
            pion_position_blanc[1] = min(pion_position_blanc[1] + 1, nb_ligne - 1)


def deplacer_pion_b_d():
        if pion_position_blanc[0] == 0:
            pion_position_blanc[0] = 0
        elif pion_position_blanc[1] == 9:
            pion_position_blanc[0] = pion_position_blanc[0]
        else:
            pion_position_blanc[0] = max(pion_position_blanc[0] - 1, 0, )
            pion_position_blanc[1] = min(pion_position_blanc[1] + 1, nb_ligne + 1)


def deplacer_pion_h_g():
    if pion_position_noir[0] == 0:
        pion_position_noir[0] = 0
    elif pion_position_noir[1] == 0:
        pion_position_noir[0] = pion_position_noir[0]
    else:
        pion_position_noir[0] = max(pion_position_noir[0] + 1, 0, )
        pion_position_noir[1] = min(pion_position_noir[1] - 1, nb_ligne - 1)


def deplacer_pion_h_d():
    if pion_position_noir[0] == 0:
        pion_position_noir[0] = 0
    elif pion_position_noir[1] == 0:
        pion_position_noir[0] = pion_position_noir[0]
    else:
        pion_position_noir[0] = max(pion_position_noir[0] - 1, 0, )
        pion_position_noir[1] = min(pion_position_noir[1] - 1, nb_ligne - 1)


screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))


pion_blanc = pygame.image.load("Image/MA-24_pion_blanc.png")
pion_blanc = pygame.transform.scale(pion_blanc, (50, 50))

pion_noir = pygame.image.load("Image/MA-24_pion_noir.png")
pion_noir = pygame.transform.scale(pion_noir, (50, 50))


nb_colonne = 10
nb_ligne = 10
for i in range(nb_ligne + 1):
    for y in range(nb_colonne + 1):
        x_case = i * 50
        y_case = y * 50
        if y % 2 == 0:
            pygame.draw.rect(screen, (0, 0, 0), (x_case, y_case, 50, 50))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (x_case, y_case, 50, 50))

screen.blit(pion_blanc, (0, 0))
screen.blit(pion_noir, (9, 0))

pion_position_blanc = [0, 0]
pion_position_noir = [9, 9]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                deplacer_pion_b_g()
            if event.key == pygame.K_LEFT:
                deplacer_pion_b_d()
            if event.key == pygame.K_UP:
                deplacer_pion_h_g()
            if event.key == pygame.K_DOWN:
                deplacer_pion_h_d()

    screen.fill((255, 255, 255))

    screen.fill((255, 255, 255))
    for i in range(nb_ligne + 1):
        for y in range(nb_colonne + 1):
            x_case = i * 50
            y_case = y * 50
            if (i + y) % 2 == 0:
                pygame.draw.rect(screen, (0, 0, 0), (x_case, y_case, 50, 50))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (x_case, y_case, 50, 50))


screen.blit(pion_blanc, (pion_position_blanc[0] * 50, pion_position_blanc[1] * 50))
screen.blit(pion_noir, (pion_position_noir[0] * 50, pion_position_noir[1] * 50))
pygame.display.flip()

pygame.quit()

