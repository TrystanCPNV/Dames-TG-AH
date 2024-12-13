"""
    Nom        : Jeux_De_Dame
    Author     : Alex_trystan
    Date       : 05.12.2024
"""

import pygame
from display import plateau, start

if __name__ == "__main__":
    pygame.init()
    plateau()
    start()
    pygame.quit()