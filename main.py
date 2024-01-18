from tkinter import *

gui = Tk()
w, h = gui.winfo_screenwidth(), gui.winfo_screenheight()
gui.geometry("%dx%d+0+0" % (w, h))
gui.title('VierGewinnt')


size = 100

# Repräsentiert ein Feld
class VierGewinntFeld:
    feld = 0

    def __init__(self, feldX, feldY):
        self.feldX = feldX
        self.feldY = feldY

    def createCanvas(self, background):
        if self.feld == 0:
            this_width = size * self.feldX
            this_height = size * self.feldY

            print("width: ", this_width)
            print("height: ", this_height)

            self.feld = background.create_rectangle(this_height, this_height, this_width + size,
                                                    this_height + size, fill="white")
        return self.feld

# Repräsentiert einen Spieler
class Player:
    spielerFeld = VierGewinntFeld(0, 0)

    def __init__(self, playerColor, name):
        self.playerColor = playerColor
        self.name = name


# Kreise im Startgame Bildschirm
canvas_width = 200
canvas_height = 40


# create
def createPlayerChip(canvas, x, y, dx, dy, color):
    chip = canvas.create_oval(x, y, dx, dy, fill=color)
    return chip


background_start = Canvas(width=canvas_width, height=canvas_height, bg='grey')
background_start.pack(expand=YES, fill=BOTH)
oval1 = createPlayerChip(background_start, 100, 50, 160, 110, "yellow")
oval2 = createPlayerChip(background_start, 100, 150, 160, 210, "red")
background_start.create_text(960, 200, text="VierGewinnt", fill="black", font=("Purisa", 100))

# Button und Textfeld code(Startbildschirm)

but1 = Button(gui, width=20, height=6, bg='grey')
but1["text"] = "Start"
but1["command"] = lambda: startGame()
but1.place(x=920, y=540)

tf_player1 = Entry(gui, bg='grey')
tf_player1.place(x=175, y=70)

tf_player2 = Entry(gui, bg='grey')
tf_player2.place(x=175, y=170)


def getPlayer1():
    return Player("yellow", tf_player1.get())


def getPlayer2():
    return Player("red", tf_player2.get())


def startGame():
    if getPlayer1().name != "" and getPlayer2().name != "":
        background_start.delete(oval1)
        background_start.delete(oval2)
        background_start.destroy()
        but1.destroy()
        background = Canvas(width=gui.winfo_screenwidth(), height=gui.winfo_screenheight(), bg='grey')
        background.pack(expand=YES, fill=BOTH)
        setupSpielFeld(background)
        setupPlayerListBar(background)
        tf_player1.destroy()
        tf_player2.destroy()
    else:
        print("Keine Namen sind gesetzt")


verticalFeldNumber = 8
horizontalFeldNumber = 7

spielfeld = []


def setupPlayerListBar(background):
    background.create_rectangle(0, 0, 1920, 60, fill="#585B5F")
    background.create_text(820, 30, text=getPlayer1().name, fill='#000000', font=('Purisa', 18))
    background.create_text(960, 30, text='-', fill='#000000', font=('Purisa', 22))
    background.create_text(1100, 30, text=getPlayer2().name, fill='#000000', font=('Purisa', 18))


def setupSpielFeld(background):
    # ToDo: implement this

    # x Koordinate Berechnung
    for x in range(1, verticalFeldNumber):
        # y Koordinate Berechnung
        for y in range(1, horizontalFeldNumber):
            feld = VierGewinntFeld(x, y)
            feld.createCanvas(background)
            spielfeld.append(feld)
    print("Setting Up Spielfeld!")


gui.mainloop()
