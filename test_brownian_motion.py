import tkinter as tk
from brownian_motion import Molecule, check_collisions
import math
import random


def main():
    canvas_width = 800
    canvas_height = 400
    canvas = tk.Canvas(width=canvas_width, height=canvas_height, bg='white')

    molecules = []

    for i in range(40):
        size = random.randint(5, 15)
        color = '#{:06x}'.format(random.randint(0, 256**3 - 1))
        speed = random.randint(1, 5)
        molecule = Molecule(canvas, size, color, speed)

        while any(math.sqrt((molecule.x - other.x) ** 2 + (molecule.y - other.y) ** 2) <
                  molecule.size / 2 + other.size / 2 for other in molecules):
            molecule.x = random.random() * canvas_width
            molecule.y = random.random() * canvas_height

        molecules.append(molecule)

    def update():
        canvas.delete('all')

        for mlcl in molecules:
            mlcl.move()
            mlcl.bounce_from_edge()

        check_collisions(molecules)

        for molec in molecules:
            molec.draw()

        canvas.after(5, update)

    update()

    window = tk.Tk()
    canvas.pack()
    window.mainloop()


if __name__ == '__main__':
    main()
