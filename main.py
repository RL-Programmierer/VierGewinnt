from tkinter import *

gui = Tk()
w, h = gui.winfo_screenwidth(), gui.winfo_screenheight()
gui.geometry("%dx%d+0+0" % (w, h))
gui.title('VierGewinnt')

class VierGewinntFeld:
    feld = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def createCanvas(self, background):
        if self.feld == 0:
            this_width = 1920 / self.x
            this_height = 1080 / self.y
            self.feld = background.create_rectangle(this_height - 5, this_height - 5, this_width + 5,
                                                    this_height + 5)
        return self.feld


class Player:
    spielerFeld = VierGewinntFeld(0, 0)
    playerColor = ""
    name = ""

    def __init__(self, playerColor, name):
        self.playerColor = playerColor
        self.name = name

    def setPlayerField(self, spielerFeld):
        self.spielerFeld = spielerFeld


# Kreise im Startgame Bildschirm
canvas_width = 200
canvas_height = 40

background_start = Canvas(width=canvas_width, height=canvas_height, bg='grey')
background_start.pack(expand=YES, fill=BOTH)
oval1 = background_start.create_oval(100, 50, 160, 110, fill="yellow")
oval2 = background_start.create_oval(100, 150, 160, 210, fill="red")

# Button und Textfeld code(Startbildschirm)

but1 = Button(gui, width=20, height=6, bg='grey')
but1["text"] = "Start"
but1["command"] = lambda: startGame()
but1.place(x=920, y=540)

tf_player1 = Entry(gui, bg='grey')
tf_player1.place(x=175, y=70)

tf_player2 = Entry(gui, bg='grey')

tf_player2.place(x=175, y=170)

player1 = Player("yellow", tf_player1.get())
player2 = Player("red", tf_player2.get())


def startGame():
    background_start.delete(oval1)
    background_start.delete(oval2)
    background_start.destroy()
    tf_player1.destroy()
    tf_player2.destroy()
    but1.destroy()
    background = Canvas(width=gui.winfo_screenwidth(), height=gui.winfo_screenheight(), bg='grey')
    background.pack(expand=YES, fill=BOTH)
    setupSpielFeld(background)
    setupPlayerListBar(background)


verticalFeldNumber = 7
horizontalFeldNumber = 6

spielfeld = []


def setupPlayerListBar(background):

    background.create_rectangle(0, 0, 1920, 60, fill="#585B5F")
    background.create_text(50,70, text=player1.name , fill='#000000')




def setupSpielFeld(background):
    # ToDo: implement this

    for ix in range(verticalFeldNumber):
        x = ix + 1

        print(x)
        for iy in range(horizontalFeldNumber):
            y = iy + 1
            feld = VierGewinntFeld(x, y)
            feld.createCanvas(background)
            spielfeld.append(feld)
            print(y)
    print("Setting Up Spielfeld!")


gui.mainloop()