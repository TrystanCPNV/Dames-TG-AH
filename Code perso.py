"""
    Nom        : Jeux_De_Dame
    Author     : Alex_trystan
    Date       : 28.11.2024
"""

import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))


pion = pygame.image.load("image\\MA-24_pion.png")
pion = pygame.transform.scale(pion, (50, 50))


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

screen.blit(pion, (0, 0))

pion_position = [4, 0]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if pion_position[0] == 9:
                    pion_position[0] = 9
                elif pion_position[1] == 9:
                    pion_position[0] = pion_position[0]
                else:
                    pion_position[0] = min(pion_position[0] + 1, nb_colonne - 1)
                    pion_position[1] = min(pion_position[1] + 1, nb_ligne - 1)
            elif event.key == pygame.K_LEFT:
                if pion_position[0] == 0:
                    pion_position[0] = 0
                elif pion_position[1] == 9:
                    pion_position[0] = pion_position[0]
                else:
                    pion_position[0] = max(pion_position[0] - 1, 0,)
                    pion_position[1] = min(pion_position[1] + 1, nb_ligne - 1)

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


    screen.blit(pion, (pion_position[0] * 50, pion_position[1] * 50))
    pygame.display.flip()

pygame.quit()

