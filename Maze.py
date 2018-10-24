def read_data_file():
    """Get level of labyrinth from data file"""
    with open('data', 'r') as my_file:
        data = my_file.read().split('\n')
        return data
    # if fail to read file
    return False


class Maze:
    """ Read data file to generate maze. """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.ok_tiles_positions = []

    def get_map(self):
        """Convert data file into list of coordinates"""
        data = read_data_file()

        if data:
            for ordinate, item in enumerate(data):
                self.y = ordinate
                for abscisse, letter in enumerate(item):
                    if letter == 'O':
                        self.x = abscisse
                        self.ok_tiles_positions.append((self.x * 40, self.y * 40))
            return self.ok_tiles_positions
