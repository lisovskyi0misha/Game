from platform import Platform
from tkinter import *
from dots import Dot
from score import Score


time = Score.speed_list[0]
p = 0

pos_dict = {'x1': 300, 'x2': 350}

window = Tk()
window.minsize(width=650, height=600)
window.title('Game')

canvas = Canvas(width=650, height=500, bg='black')
canvas.pack()

canvas.create_line(0, 491, 650, 491, fill='white')

s = Score(canvas, window)

score_lab = Label(text=f'Your score is: {s.score}', font=('arial', 15))
score_lab.place(x=260, y=565)

platform = Platform(canvas, pos_dict['x1'], pos_dict['x2'])

dot1 = Dot(canvas)
dot2 = Dot(canvas)
dot3 = Dot(canvas)


def l(k):
    move_l()


def r(k):
    move_r()


def st(k):
    start_game()


def move_l():
    if pos_dict['x1'] > 0:
        platform.move_left(pos_dict['x1'], pos_dict['x2'])
        pos_dict['x1'] = platform.pos_x1
        pos_dict['x2'] = platform.pos_x2
    else:
        pass


def move_r():
    if pos_dict['x2'] < 650:
        platform.move_right(pos_dict['x1'], pos_dict['x2'])
        pos_dict['x1'] = platform.pos_x1
        pos_dict['x2'] = platform.pos_x2
    else:
        pass


def move_d1():
    time = Score.speed_list[0]
    if p == 2:
        if dot1.y == 300:
            start2()
        dot1.move_down()
        if dot1.y + 10 == 485:
            if platform.pos_x1 <= dot1.x <= platform.pos_x2 or \
                    platform.pos_x1 <= dot1.x + 10 <= platform.pos_x2:
                s.win()
                score_up()
                dot1.remove()
            else:
                stop()
                return 0
            return 0
        else:
            window.after(time, move_d1)
    else:
        pass


def move_d2():
    time = Score.speed_list[0]
    if p == 2:
        if dot2.y == 300:
            start3()
        dot2.move_down()
        if dot2.y + 10 == 485:
            if platform.pos_x1 <= dot2.x <= platform.pos_x2 or \
                    platform.pos_x1 <= dot2.x + 10 <= platform.pos_x2:
                s.win()
                score_up()
                dot2.remove()
            else:
                stop()
                return 0
            return 0
        else:
            window.after(time, move_d2)
    else:
        pass


def move_d3():
    time = Score.speed_list[0]
    if p == 2:
        if dot3.y == 300:
            start1()
        dot3.move_down()
        if dot3.y + 10 == 485:
            if platform.pos_x1 <= dot3.x <= platform.pos_x2 or \
                    platform.pos_x1 <= dot3.x + 10 <= platform.pos_x2:
                s.win()
                score_up()
                dot3.remove()
            else:
                stop()
                return 0
            return 0
        else:
            window.after(time, move_d3)
    else:
        pass


def start3():
    dot3.create()
    move_d3()


def start2():
    dot2.create()
    move_d2()


def start1():
    global p
    p = 2
    dot1.create()
    move_d1()


def score_up():
    score_lab.config(text=f'Your score is: {s.score}')


def stop():
    global p, text
    p = 1
    text = canvas.create_text(330, 250, text='Game Over', fill='white', font=20)
    dot1.remove()
    dot2.remove()
    dot3.remove()
    try:
        s.canvas.delete(s.label)
    except:
        pass


def start_game():
    global p, dot1, dot2, dot3
    if p == 0:
        start1()
    elif p == 2:
        pass
    else:
        canvas.delete(text)
        p = 0
        Score.renew()
        dot1 = Dot(canvas)
        dot2 = Dot(canvas)
        dot3 = Dot(canvas)
        start1()
        s.rewrite()
        score_lab.config(text=f'Your score is: {s.score}')


canvas.bind_all('<KeyPress-Left>', l)
canvas.bind_all('<KeyPress-Right>', r)
canvas.bind_all('<KeyPress-space>', st)

button_l = Button(text='<', width=7, command=move_l)
button_l.place(x=50, y=530)

button_r = Button(text='>', width=7, command=move_r)
button_r.place(x=550, y=530)

start_button = Button(text='Start', width=7, command=start_game)
start_button.place(x=295, y=530)

window.mainloop()
