# -*- coding: utf-8 -*-

import random
import pygame

from maze import Maze


class UserInterface:
    """ Manage graphical user interface. """

    # main elements used by interface
    ELEMENTS = ['player', 'wall_background', 'tile', 'keeper', 'crossbow', 'sword', 'axe']

    def __init__(self):
        pygame.init()
        # make a window 600 by 600 pixel
        self.window = pygame.display.set_mode((600, 600))
        self.font = pygame.font.Font(None, 40)
        self.load_element()

        self.position = self.player.get_rect()
        self.keeper_position = (14 * 40, 14 * 40)

        self.text = None
        self.textpos = None

        my_maze = Maze()
        self.allowed_tiles = my_maze.get_map()

        # generate 3 random object coordinates
        self.first_object = [position for position in random.sample(self.allowed_tiles, 1)]
        self.second_object = [position for position in random.sample(self.allowed_tiles, 1)]
        self.third_object = [position for position in random.sample(self.allowed_tiles, 1)]
        self.objects = [self.first_object, self.second_object, self.third_object]

    def load_element(self):
        """Loading all sprites"""
        for sword in UserInterface.ELEMENTS:
            setattr(self, sword, pygame.image.load('img/' + sword + ".png").convert_alpha())
        for axe in UserInterface.ELEMENTS:
            setattr(self, axe, pygame.image.load('img/' + axe + ".png").convert_alpha())
        for crossbow in UserInterface.ELEMENTS:
            setattr(self, crossbow, pygame.image.load('img/' + crossbow + ".png").convert_alpha())

    def show_text(self, message):
        """Show remaining item on the top left"""
        self.text = self.font.render((str(message)), 1, (10, 10, 10))
        self.textpos = self.text.get_rect()
        self.window.blit(self.text, self.textpos)

    def show_element(self):
        """
        Element showed in this order :
        background, tiles, object, text, MacGyver and keeper
        """
        self.window.blit(self.wall_background, (0, 0))
        # show the maze path
        for tile in self.allowed_tiles:
            self.window.blit(self.tile, tile)
        # show  item that will be taken by player
        for sword in self.first_object:
            self.window.blit(self.sword, sword)
        for axe in self.second_object:
            self.window.blit(self.axe, axe)
        for crossbow in self.third_object:
            self.window.blit(self.crossbow, crossbow)

        self.show_text(str(len(self.objects)))
        self.window.blit(self.player, self.position)
        self.window.blit(self.keeper, self.keeper_position)
