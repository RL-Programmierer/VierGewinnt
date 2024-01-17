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

    def createCanvas(self):
        if self.feld == 0:
            this_width = 1920 / self.x
            this_height = 1080 / self.y
            self.feld = Canvas(width=this_width, height=this_height,
                               bg='yellow', highlightthickness=5, highlightbackground="black")
            self.feld.pack(expand=YES, fill=BOTH)
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
but1.place(x=20, y=540)

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
    background = Canvas(width=canvas_width, height=canvas_height, bg='grey')
    background.pack(expand=YES, fill=BOTH)
    setupSpielFeld()
    setupPlayerListBar()


verticalFeldNumber = 7
horizontalFeldNumber = 6

spielfeld = []


def setupPlayerListBar():
    # ToDo: füge die Spielerleiste hinzu für das Spiel
    print("This is work in progress")


def setupSpielFeld():
    # ToDo: implement this

    for ix in range(verticalFeldNumber):
        x = ix + 1

        print(x)
        for iy in range(horizontalFeldNumber):
            y = iy + 1
            feld = VierGewinntFeld(x, y)
            feld.createCanvas()
            spielfeld.append(feld)
            print(y)
    print("Setting Up Spielfeld!")


gui.mainloop()