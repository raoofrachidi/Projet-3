#!/usr/bin/env python
# -*- coding:Utf-8 -*-

"""

Jeu Macgyver Labyrinthe

Jeu dans lequel on doit déplacer Macgyver jusqu'au gardien à travers un labyrinthe.


Script Python

Fichiers : gameplay.py, maze.py, userinterface.py,  main.py, data + images

"""

import pygame

from gameplay import GamePlay
from userinterface import UserInterface, refresh

keyboard_input = {pygame.K_DOWN: 'player.move_y(40)',
                  pygame.K_UP: 'player.move_y(-40)',
                  pygame.K_LEFT: 'player.move_x(-40)',
                  pygame.K_RIGHT: 'player.move_x(40)', }


def start_game():
    """Instanciate class
    and awaiting user keybord input from player
    """

    interface = UserInterface()
    player = GamePlay(interface)
    continue_game = True

    while 'user playing' and continue_game:

        for event in pygame.event.get():
            # waiting input key from user
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # end game when pressed escape key
                    continue_game = False
                if event.key in keyboard_input:
                    eval(keyboard_input[event.key])

        interface.show_element()
        if not player.check_objects():
            # when player is next to the keeper, the game ends
            break
        refresh()


if __name__ == '__main__':
    start_game()
