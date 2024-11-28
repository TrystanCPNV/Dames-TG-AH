import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))

# Load and scale the pion image
pion = pygame.image.load("image\\MA-24_pion.png")
pion = pygame.transform.scale(pion, (50, 50))

# Draw the grid
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

screen.blit(pion, (0, 0))  # Initial position of the pion

pion_position = [0, 0]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pion_position[0] = min(pion_position[0] + 1, nb_colonne - 1)
            elif event.key == pygame.K_LEFT:
                pion_position[0] = max(pion_position[0] - 1, 0)
            elif event.key == pygame.K_DOWN:
                pion_position[1] = min(pion_position[1] + 1, nb_ligne - 1)
            elif event.key == pygame.K_UP:
                pion_position[1] = max(pion_position[1] - 1, 0)

    screen.fill((255,255,255))

    # Refill the screen and redraw the grid
    screen.fill((255, 255, 255))  # Clear the screen
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

