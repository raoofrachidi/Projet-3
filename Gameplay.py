def read_data_file():
    """Get level of labyrinth from data file"""
    with open('data', 'r') as my_file:
        data = my_file.read().split('\n')
        return data
    # if fail to read file
    return False


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
        """When player is next to a chest, that remove item on UI"""
        pos = (self.player.position[0], self.player.position[1])

        # compare player position with objects
        if pos in self.player.objects:
            # delete item when taken
            self.player.objects.remove(pos)

        # compare player position with keeper position
        if pos == self.player.keeper_position:
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
