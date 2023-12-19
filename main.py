from tkinter import *

gui = Tk()
gui.geometry('750x500')
gui.title('Start')

class Player:
    x = 0
    y = 0

    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.x = x
        self.y = y


nameplayer1 = 0
nameplayer2 = 0

canvas_width = 200
canvas_height = 40

myCanvas = Canvas(width=canvas_width, height=canvas_height, bg='grey')
myCanvas.pack(expand=YES, fill=BOTH)
myCanvas.create_oval(100, 50, 160, 110, fill="yellow")
myCanvas.create_oval(100, 150, 160, 210, fill="red")

but1 = Button(gui, width=20, height=6)
but1["text"] = "Start"
but1["command"] = 'start'
but1.pack()

but1.place(x=275, y=300)


def start():
    print('ok')


tf_player1 = Entry(gui)
tf_player1.pack()
tf_player1.place(x=175, y=70)

tf_player2 = Entry(gui)
tf_player2.pack()
tf_player2.place(x=175, y=170)

gui.mainloop()
