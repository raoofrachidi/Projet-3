# -*- coding: utf-8 -*-

import random as r
import pygame as pyg

from maze import Maze

DIR = 'img/'


def refresh():
    """Clean all graphics elements"""
    pyg.display.flip()


class UserInterface:
    """ Manage graphical user interface. """

    # main elements used by interface
    ELEMENTS = ['player', 'wall_background', 'tile', 'keeper', 'item']

    def __init__(self):
        pyg.init()
        # make a window 600 by 600 pixel
        self.window = pyg.display.set_mode((600, 600))
        self.font = pyg.font.Font(None, 40)
        self.load_element()

        self.position = self.player.get_rect()
        self.keeper_position = (14 * 40, 14 * 40)

        self.text = None
        self.textpos = None

        my_maze = Maze()
        self.allowed_tiles = my_maze.get_map()

        # generate 3 random object coordinates
        self.objects = [position for position in r.sample(self.allowed_tiles, 3)]

    def load_element(self):
        """Loading all sprites"""
        for item in UserInterface.ELEMENTS:
            setattr(self, item, pyg.image.load(DIR + item + ".png").convert())

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
        for item in self.objects:
            self.window.blit(self.item, item)

        self.show_text(str(len(self.objects)))
        self.window.blit(self.player, self.position)
        self.window.blit(self.keeper, self.keeper_position)
