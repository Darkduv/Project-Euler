from tkinter import *

fen = Tk()

cadre = Frame(fen, width=800, height=800, bg='dark grey')
cadre.pack()
support = Canvas(cadre, bg='white', height=800, width=800)
support.pack(side=LEFT)

LL = []
for i in range(400):
    l = []
    for j in range(400):
        l.append(support.create_rectangle(2*i, 2*j, 2*i+2, 2*j+2, fill='white'))
    LL.append(l)

i0, j0, side = 200, 200, 0


def motion():
    global i0, j0
    if side == 0:
        i0 -= 1
    elif side == 1:
        j0 += 1
    elif side == 2:
        i0 += 1
    else:
        j0 -= 1


def _next(event):
    if support._getconfigure(LL[i][j], 'fill') == 'black':
        print("ee")


def quitter(event):
    fen.destroy()

fen.bind("q", quitter)
fen.bind('n', _next)
fen.mainloop()