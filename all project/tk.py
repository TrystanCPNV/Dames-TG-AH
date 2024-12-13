#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : ma24_dames_rules.py
Authors : Pascal Benzonana and Vitor COVAL
Date    : 2024.12.05
Version : 0.02
Purpose : Librairie backend du jeu de dames développé dans le cadre
          du module MA-24

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-12-05 02 PBA & VCL
  - Ajouté les fonctions de déplacement haut, bas, gauche, droite

  2024-11-07 01 PBA & VCL
  - Version initiale
"""


def plateau(taille_plateau=(10,10)):
    """Définit la taille du plateau
    """
    global nb_lignes, nb_colonnes
    nb_colonnes = taille_plateau[0]
    nb_lignes = taille_plateau[1]
    cree_plateau()


def cree_plateau():
    """ Crée et initialise le plateau
    """
    global plateau_board, nb_lignes, nb_colonnes
    plateau_board = [1]*nb_lignes
    for ligne in range(nb_lignes):
        plateau_board[ligne] = [0,1]*(nb_colonnes//2) if not ligne % 2 else [1,0]*(nb_colonnes//2)
        if nb_colonnes % 2:
            plateau_board[ligne] += [plateau_board[ligne][0]]


def board_actuel():
    """Renvoie l'état du board actuel
        """
    global plateau_board
    return tuple(plateau_board)


mouvements = []
pion_pos = [0, 0]
nb_lignes = 10
nb_colonnes = 10
plateau_board = []
cree_plateau()

