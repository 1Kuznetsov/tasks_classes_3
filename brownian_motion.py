import random
import math


class Molecule:
    """
    Class representing Molecule
    """

    def __init__(self, canvas, size, color, speed):
        """
        Sets all the necessary attributes for the class Molecule
        :param canvas:
        :param size:
        :param color:
        :param speed:
        """

        self.canvas = canvas
        self.size = size
        self.color = color
        self.speed = speed

        self.x = random.random() * canvas.winfo_width()
        self.y = random.random() * canvas.winfo_height()

        self.angle = random.random() * 360

    def draw(self):
        """
        Method of drawing circle for molecule
        :return:
        """

        self.canvas.create_oval(self.x - self.size / 2, self.y - self.size / 2,
                                self.x + self.size / 2, self.y + self.size / 2,
                                fill=self.color)

    def move(self):
        """
        Method of moving molecule depending on its speed and direction
        :return:
        """

        self.x += self.speed * math.cos(self.angle * math.pi / 180)
        self.y += self.speed * math.sin(self.angle * math.pi / 180)

    def bounce_from_edge(self):
        """
        Method of bouncing from the corners
        :return:
        """

        if self.x < 0 or self.x > self.canvas.winfo_width():
            self.angle = 180 - self.angle

        if self.y < 0 or self.y > self.canvas.winfo_height():
            self.angle = 360 - self.angle

    def bounce_from_molecule(self, other):
        """
        Method of bounce from the other molecule
        :param other:
        :return:
        """

        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance < self.size / 2 + other.size / 2:
            # Определение нормали к линии соединяющей центры молекул
            nx = dx / distance
            ny = dy / distance

            # Разложение скоростей на тангенциальную и нормальную компоненты
            self.speedx = self.speed * nx
            self.speedy = self.speed * ny
            other.speedx = other.speed * nx
            other.speedy = other.speed * ny

            # Отражение тангенциальных компонент
            self.speedx = -self.speedx
            other.speedx = -other.speedx

            # Обновление координат на основе отраженных компонент
            self.x += self.speedx
            self.y += self.speedy
            other.x += other.speedx
            other.y += other.speedy
