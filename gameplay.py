# -*- coding: utf-8 -*-


class GamePlay:
    """ Manage mechanisms of game. """

    def __init__(self, player):
        self.player = player

    def move_x(self, x):
        """Manage horizontal moves"""
        # check next coordinates if are allowed
        next_position = self.player.position[0] + x, self.player.position[1]
        if not next_position in self.player.allowed_tiles:
            # if not, player not move
            x = 0
        self.player.position = self.player.position.move(x, 0)

    def move_y(self, y):
        """Manage vertical moves"""
        next_position = self.player.position[0], self.player.position[1] + y
        if not next_position in self.player.allowed_tiles:
            y = 0
        self.player.position = self.player.position.move(0, y)

    def check_objects(self):
        """When player is next to a chest, that remove item"""
        position = (self.player.position[0], self.player.position[1])
        self.player.objects = (self.player.first_object + self.player.second_object + self.player.third_object)

        # compare player position with objects
        if position in self.player.first_object:
            # delete item when taken
            self.player.first_object.remove(position)
        if position in self.player.second_object:
            self.player.second_object.remove(position)
        if position in self.player.third_object:
            self.player.third_object.remove(position)

        # compare player position with keeper position
        if position == self.player.keeper_position:
            self.check_end_game()
            # end game
            return False

        # continue game
        return True

    def check_end_game(self):
        """When player is next to keeper,
        that check if player have all items
        """
        if self.player.objects:
            print('You loose !')
        else:
            print('You win !')
