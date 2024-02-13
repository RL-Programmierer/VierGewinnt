from tkinter import *
import random

gui = Tk()
w, h = gui.winfo_screenwidth(), gui.winfo_screenheight()
gui.geometry("%dx%d+0+0" % (w, h))
gui.title('VierGewinnt')
spielerAnDerReihe = 1

print('max. Länge:', w)
print('max. Höhe:', h)

# Feld Größe Einstellung
size = 130

# Spielfeldgröße
horizontalFeldNumber = 7
verticalFeldNumber = 8

roundNumber = 0


class PlayerListBar:
    def __init__(self, background):
        # ToDo: Besprechen, ob Grau die Farbe des Spielers ist, der gerade an der Reihe ist oder nicht
        global spielerAnDerReihe
        self.background = background
        self.Rechteck = background.create_rectangle(0, 0, 1920, 60, fill="#585B5F")
        self.Bindestrich = background.create_text(960, 30, text='-', fill='#000000', font=('Purisa', 22))

        if spielerAnDerReihe == 1:
            self.Spieler1 = background.create_text(820, 30, text=getPlayer1().name, fill='#000000', font=('Purisa', 18))
        else:
            self.Spieler1 = background.create_text(820, 30, text=getPlayer1().name, fill='#847B79', font=('Purisa', 18))

        if spielerAnDerReihe == 2:
            self.Spieler2 = background.create_text(1100, 30, text=getPlayer2().name, fill='#000000',
                                                   font=('Purisa', 18))
        else:
            self.Spieler2 = background.create_text(1100, 30, text=getPlayer2().name, fill='#847B79',
                                                   font=('Purisa', 18))

    def tauscheSpielerAnDerReihe(self):
        global spielerAnDerReihe

        if spielerAnDerReihe == 1:
            spielerAnDerReihe = spielerAnDerReihe + 1
        elif spielerAnDerReihe == 2:
            spielerAnDerReihe = spielerAnDerReihe - 1
        else:
            print('Error!!! SpielerAnDerReihe:', spielerAnDerReihe)

        if spielerAnDerReihe == 1:
            self.background.itemconfig(self.Spieler1, fill='#000000')
            self.background.itemconfig(self.Spieler2, fill='#847B79')
        elif spielerAnDerReihe == 2:
            self.background.itemconfig(self.Spieler1, fill='#847B79')
            self.background.itemconfig(self.Spieler2, fill='#000000')


# Repräsentiert ein Feld
class VierGewinntFeld:
    farbe = 'white'

    def __init__(self, background, feldX, feldY):
        self.feldX = feldX
        self.feldY = feldY
        self.background = background

        feld_y = 50 + size * self.feldX
        feld_x = 375 + size * self.feldY

        self.feld = background.create_rectangle(feld_x, feld_y, feld_x + size,
                                                feld_y + size, fill=self.farbe)

    def setColor(self, color):
        self.farbe = color
        self.background.itemconfig(self.feld, fill=color)

    def getColor(self):
        return self.farbe


# Repräsentiert einen Spieler
class Player:

    def __init__(self, playerColor, name):
        self.playerColor = playerColor
        self.name = name


# Kreise im Startgame Bildschirm
canvas_width = 200
canvas_height = 40


# create
def createPlayerChip(canvas, x, y, chipSize, color):
    chip = canvas.create_oval(x, y, x + chipSize, y + chipSize, fill=color)
    return chip


background_start = Canvas(width=canvas_width, height=canvas_height, bg='grey')
background_start.pack(expand=YES, fill=BOTH)
oval1 = createPlayerChip(background_start, 850, 310, 60, "yellow")
oval2 = createPlayerChip(background_start, 850, 410, 60, "red")
background_start.create_text(960, 200, text="VierGewinnt", fill="black", font=("Purisa", 100))

# Button und Textfeld code(Startbildschirm)

but1 = Button(gui, width=30, height=6, bg='grey')
but1["text"] = "Start"
but1["command"] = lambda: startGame()
but1.place(x=890, y=540)

tf_player1 = Entry(gui, bg='grey', width=30)
tf_player1.place(x=950, y=330)
tf_player1.insert(0, 'Spieler 1')

tf_player2 = Entry(gui, bg='grey', width=30)
tf_player2.place(x=950, y=430)
tf_player2.insert(0, 'Spieler 2')


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

        buttemporaer = Button(gui, width=20, height=6, bg='grey')
        buttemporaer["text"] = "nextRoundTest"
        buttemporaer["command"] = lambda: nextRound()
        buttemporaer.place(x=500, y=740)

        buttemporaer = Button(gui, width=20, height=6, bg='grey')
        buttemporaer["text"] = "temporaer"
        buttemporaer["command"] = lambda: restartGame(background)
        buttemporaer.place(x=1020, y=740)

    else:
        print("Keine Namen sind gesetzt")


spielfeld = []
playerListBar = 0


def setupPlayerListBar(background):
    global playerListBar
    playerListBar = PlayerListBar(background)


def nextRound():
    global roundNumber
    global playerListBar
    roundNumber = roundNumber + 1
    print('Round Number:', roundNumber)
    playerListBar.tauscheSpielerAnDerReihe()
    getFeldFromIndex(random.randint(0, len(spielfeld))).setColor('green')


def setupSpielFeld(background):
    # x Koordinate Berechnung
    for x in range(1, horizontalFeldNumber):
        # y Koordinate Berechnung
        for y in range(1, verticalFeldNumber):
            feld = VierGewinntFeld(background, x, y)
            spielfeld.append(feld)
            if x == 1:
                feld.setColor('yellow')


def getFeldFromIndex(index):
    for i, j in enumerate(spielfeld):
        if i == index:
            return j


# bei game restart
def restartGame(background):
    global var1
    global var2
    global var3
    global var4

    # Button und Textfeld code(Startbildschirm)

    but1 = Button(gui, width=20, height=6, bg='grey')
    but1["text"] = "Start"
    but1["command"] = lambda: startGame()
    but1.place(x=920, y=540)

    tf_player1 = Entry(gui, bg='grey')
    tf_player1.place(x=175, y=70)

    tf_player2 = Entry(gui, bg='grey')
    tf_player2.place(x=175, y=170)

    butrestart = Button(gui, width=50, height=10, bg='grey')
    butrestart["text"] = "Restart"
    butrestart["command"] = lambda: restartGame(background)
    butrestart.place(x=820, y=500)

    background.delete(var1)
    background.delete(var2)
    background.delete(var3)
    background.delete(var4)


gui.mainloop()
