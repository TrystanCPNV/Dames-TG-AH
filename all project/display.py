import pygame

nb_colonne = 10
nb_ligne = 10

screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))

pion_blanc = pygame.image.load("images/MA-24_pion_blanc.png")
pion_blanc = pygame.transform.scale(pion_blanc, (50, 50))

pion_noir = pygame.image.load("images/MA-24_pion_noir.png")
pion_noir = pygame.transform.scale(pion_noir, (50, 50))

pion_position_blanc = [0, 0]
pion_position_noir = [1, 9]

def plateau():
    for i in range(nb_ligne):
        for y in range(nb_colonne):
            x_case = i * 50
            y_case = y * 50
            if (i + y) % 2 == 0:
                pygame.draw.rect(screen, (0, 0, 0), (x_case, y_case, 50, 50))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (x_case, y_case, 50, 50))


def pion_placement():
    for i in range(4):
        nb_pion = 0
        if i == 0 or i == 2:
            pion_position_blanc[0] = 0
            pion_position_noir[0] = 1
        elif i == 1 or i == 3:
            pion_position_blanc[0] = 0 + 1
            pion_position_noir[0] = 0
        for o in range(5):
            nb_pion += 1
            screen.blit(pion_blanc, (pion_position_blanc[0] * 50, pion_position_blanc[1] * 50))
            pion_position_blanc[0] += 2
            screen.blit(pion_noir, (pion_position_noir[0] * 50, pion_position_noir[1] * 50))
            pion_position_noir[0] += 2
        if nb_pion == 5:
            pion_position_blanc[1] += 1
            pion_position_blanc[0] = 0
            pion_position_noir[1] -= 1
            pion_position_noir[0] = 1


def start():
    from rules import mouvement
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        mouvement()
        pygame.display.flip()



