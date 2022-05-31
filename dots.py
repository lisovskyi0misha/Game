import random
from list import cord_list, color_list


class Dot:
    def __init__(self, canvas):
        self.dot = None
        self.canvas = canvas
        y = 5
        self.y = y
        self.x = None

    @staticmethod
    def create_color():
        c = random.choice(color_list)
        return c

    def create(self):
        color = self.create_color()
        self.y = 5
        self.x = random.choice(cord_list)
        self.dot = self.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10,
                                                fill=color)
        
    def move_down(self):
        self.y = self.y + 5
        self.canvas.coords(self.dot, self.x, self.y, self.x + 10, self.y + 10)

    def remove(self):
        self.canvas.delete(self.dot)
