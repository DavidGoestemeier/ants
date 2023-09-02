import random
from src.ants.ant import Ant


class Colony:
    def __init__(self, name, amount_of_ants, ant_size, color):
        self.name = name
        self.ants = []
        self.amount_of_ants = amount_of_ants
        self.ant_size = ant_size
        self.color = color
        self.__create_ants()

    def __create_ants(self):
        for i in range(self.amount_of_ants):
            pos_x = random.randint(0, 1280 - self.ant_size)
            pos_y = random.randint(0, 720 - self.ant_size)
            self.ants.append(Ant(pos_x, pos_y, self.ant_size, self.ant_size, self.color))

    def draw(self, screen):
        for ant in self.ants:
            ant.draw(screen)

    def update(self):
        for ant in self.ants:
            ant.update()
