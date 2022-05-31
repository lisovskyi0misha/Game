class Platform:
    def __init__(self, canvas, pos_x1, pos_x2):
        self.canvas = canvas
        self.pos_x1 = pos_x1
        self.pos_x2 = pos_x2
        self.platform = canvas.create_rectangle(pos_x1, 480, pos_x2, 490, fill='yellow')

    def move_left(self, pos_x1, pos_x2):
        pos_x1 = pos_x1 - 50
        pos_x2 = pos_x2 - 50
        self.canvas.coords(self.platform, pos_x1, 480, pos_x2, 490)
        self.pos_x1 = pos_x1
        self.pos_x2 = pos_x2

    def move_right(self, pos_x1, pos_x2):
        pos_x1 = pos_x1 + 50
        pos_x2 = pos_x2 + 50
        self.canvas.coords(self.platform, pos_x1, 480, pos_x2, 490)
        self.pos_x1 = pos_x1
        self.pos_x2 = pos_x2
