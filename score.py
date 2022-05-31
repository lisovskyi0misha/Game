from list import text_dict


class Score:
    speed_list = [45, 40, 30, 20, 10]
    speed_list_r = [45, 40, 30, 20, 10]
    score_list = [9, 19, 29, 39]
    score_list2 = [10, 20, 30, 40]

    def __init__(self, canvas, window):
        self.window = window
        self.canvas = canvas
        self.label = None
        self.score = 0

    def win(self):
        if self.score in self.score_list:
            Score.speed_up()
            self.congrats()
        elif self.score in self.score_list2:
            self.uncongrats()
        self.score += 1

    def rewrite(self):
        self.score = 0

    def uncongrats(self):
        self.canvas.delete(self.label)

    def congrats(self):
        text = text_dict[self.score]
        self.label = self.canvas.create_text(330, 250, text=text, fill='white', font=20)

    @classmethod
    def renew(cls):
        cls.speed_list = cls.speed_list_r

    @classmethod
    def speed_up(cls):
        cls.speed_list.pop(0)
