from tkinter import *
from pygame import *

gui = Tk()
gui.geometry('750x500')
gui.title('VierGewinnt')


class Player:
    verticalRow = 0
    horizontalRow = 0
    playerColor = ""
    name = ""

    def __init__(self, playerColor, name):
        self.verticalRow = 0
        self.horizontalRow = 0
        self.playerColor = playerColor
        self.name = name

    def move(self, verticalRow, horizontalRow):
        self.verticalRow = verticalRow
        self.horizontalRow = horizontalRow


canvas_width = 200
canvas_height = 40

myCanvas = Canvas(width=canvas_width, height=canvas_height, bg='grey')
myCanvas.pack(expand=YES, fill=BOTH)
myCanvas.create_oval(100, 50, 160, 110, fill="yellow")
myCanvas.create_oval(100, 150, 160, 210, fill="red")


def startGame():
    print('Sehr Gutt')


but1 = Button(gui, width=20, height=6)
but1["text"] = "Start"
but1["command"] = startGame()
but1.pack()

but1.place(x=275, y=300)

tf_player1 = Entry(gui)
tf_player1.pack()
tf_player1.place(x=175, y=70)

tf_player2 = Entry(gui)
tf_player2.pack()
tf_player2.place(x=175, y=170)

nameplayer1 = Player("yellow", tf_player1.get())
nameplayer2 = Player("red", tf_player2.get())

gui.mainloop()
