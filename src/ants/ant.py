import pygame
import random
import math

from src.game_settings import GAME_BOUNDARY_X, GAME_BOUNDARY_Y


class Ant:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.is_facing = "up"
        self.moved_times = 0
        self.direction = 0
        self.speed = 1
        self.change_direction_freq = random.randint(10, 100)
        self.randomize_direction()

    def rect(self):
        return self.rect

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        if self.is_facing == "up":
            self.rect.y -= self.speed
        elif self.is_facing == "down":
            self.rect.y += self.speed
        elif self.is_facing == "left":
            self.rect.x -= self.speed
        elif self.is_facing == "right":
            self.rect.x += self.speed

    def calc_next_position(self):
        direction_rad = math.radians(self.direction)

        delta_x = self.speed * math.cos(direction_rad)
        delta_y = self.speed * math.sin(direction_rad)

        next_x = self.rect.x + delta_x
        next_y = self.rect.y + delta_y

        return round(next_x), round(next_y)

    def moveTo(self, x, y):
        if self.would_hit_boundary(x, y):
            self.randomize_direction()
            self.moved_times = 0
            return
        else:
            self.rect.x = x
            self.rect.y = y

    def would_hit_boundary(self, x, y):
        if x < 0 or x > GAME_BOUNDARY_X - self.rect.width:
            return True
        if y < 0 or y > GAME_BOUNDARY_Y - self.rect.height:
            return True
        return False

    def randomize_direction(self):
        random_direction = random.randint(0, 360)
        self.direction = random_direction

    def update(self):
        (next_position_x, next_position_y) = self.calc_next_position()
        self.moveTo(next_position_x, next_position_y)
        self.moved_times += 1
        if self.moved_times == self.change_direction_freq:
            self.randomize_direction()
            self.moved_times = 0
