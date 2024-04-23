import random
import pygame


class Molecule:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def check_collision(self, other):
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        if distance < self.size + other.size:
            return True
        else:
            return False

    def bounce(self, other):
        self.vx = -self.vx
        self.vy = -self.vy
        other.vx = -other.vx
        other.vy = -other.vy
