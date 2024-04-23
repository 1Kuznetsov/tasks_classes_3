import pygame
import random
from brownian_motion import Molecule

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


molecules = []
for i in range(50):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    size = random.randint(5, 15)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    molecules.append(Molecule(x, y, size, color))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for molecule in molecules:
        molecule.move()

    for i in range(len(molecules)):
        for j in range(i + 1, len(molecules)):
            if molecules[i].check_collision(molecules[j]):
                molecules[i].bounce(molecules[j])

    screen.fill((255, 255, 255))
    for molecule in molecules:
        molecule.draw(screen)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
