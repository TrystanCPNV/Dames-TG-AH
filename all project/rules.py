import pygame

from display import pion_position_blanc, pion_position_noir, nb_colonne, nb_ligne, plateau


def deplacer_pion_bas_gauche():
    if pion_position_blanc[0] > 0 and pion_position_blanc[1] < 9:
        pion_position_blanc[0] -= 1
        pion_position_blanc[1] += 1


def deplacer_pion_bas_droite():
    if pion_position_blanc[0] < 9 and pion_position_blanc[1] < 9:
        pion_position_blanc[0] += 1
        pion_position_blanc[1] += 1


def deplacer_pion_haut_gauche():
    if pion_position_noir[0] > 0 and pion_position_noir[1] > 0:
        pion_position_noir[0] -= 1
        pion_position_noir[1] -= 1


def deplacer_pion_haut_droite():
    if pion_position_noir[0] < 9 and pion_position_noir[1] > 0:
        pion_position_noir[0] += 1
        pion_position_noir[1] -= 1


def mouvement():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                deplacer_pion_bas_droite()
            if event.key == pygame.K_LEFT:
                deplacer_pion_bas_gauche()
            if event.key == pygame.K_UP:
                deplacer_pion_haut_gauche()
            if event.key == pygame.K_DOWN:
                deplacer_pion_haut_droite()

            plateau()
            pygame.display.flip()