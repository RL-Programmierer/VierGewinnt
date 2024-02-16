from tkinter import *
from tkinter import colorchooser

gui = Tk()
width, height = gui.winfo_screenwidth(), gui.winfo_screenheight()
gui.geometry("%dx%d+0+0" % (width, height))
gui.state('zoomed')
gui.title('VierGewinnt')

print('max. Länge:', width)
print('max. Höhe:', height)

# Feld Größe Einstellung
size = 130

# Spielfeldgröße
horizontalFeldNumber = 7
verticalFeldNumber = 8

roundNumber = 0

playerName1 = 'Spieler 1'
playerName2 = 'Spieler 2'


# Repräsentiert die Spieler Leiste
class PlayerListBar:
    def __init__(self, background):
        global spielerAnDerReihe
        self.background = background
        self.Rechteck = background.create_rectangle(0, 0, 1920, 60, fill="#585B5F")
        self.Bindestrich = background.create_text(960, 30, text='-', fill='#000000', font=('Purisa', 22))

        if spielerAnDerReihe.getPlayerNumber() == 1:
            self.Spieler1 = background.create_text(820, 30, text=player1.name, fill='#000000',
                                                   font=('Purisa', 18, 'bold'))
        else:
            self.Spieler1 = background.create_text(820, 30, text=player1.name, fill='#847B79', font=('Purisa', 18))

        if spielerAnDerReihe.getPlayerNumber() == 2:
            self.Spieler2 = background.create_text(1100, 30, text=player2.name, fill='#000000',
                                                   font=('Purisa', 18, 'bold'))
        else:
            self.Spieler2 = background.create_text(1100, 30, text=player2.name, fill='#847B79',
                                                   font=('Purisa', 18))

    def tauscheSpielerAnDerReihe(self):
        global spielerAnDerReihe

        if spielerAnDerReihe.getPlayerNumber() == 1:
            spielerAnDerReihe = player2
        elif spielerAnDerReihe.getPlayerNumber() == 2:
            spielerAnDerReihe = player1
        else:
            print('Error!!! SpielerAnDerReihe:', spielerAnDerReihe)

        if spielerAnDerReihe.getPlayerNumber() == 1:
            self.background.itemconfig(self.Spieler1, fill='#000000', font=('Purisa', 18, 'bold'))
            self.background.itemconfig(self.Spieler2, fill='#847B79', font=('Purisa', 18))
        elif spielerAnDerReihe.getPlayerNumber() == 2:
            self.background.itemconfig(self.Spieler1, fill='#847B79', font=('Purisa', 18))
            self.background.itemconfig(self.Spieler2, fill='#000000', font=('Purisa', 18, 'bold'))


# Repräsentiert ein Feld
class VierGewinntFeld:
    farbe = 'blue'

    def __init__(self, background, feldX, feldY):
        self.playerChip = None
        self.playerNumber = 0
        self.feldX = feldX
        self.feldY = feldY
        self.background = background

        feld_y = 100 + size * self.feldX
        feld_x = 375 + size * self.feldY

        self.feld = background.create_rectangle(feld_x, feld_y, feld_x + size,
                                                feld_y + size, fill=self.farbe)

    def setColor(self, color):
        self.farbe = color
        self.background.itemconfig(self.feld, fill=color)

    def getColor(self):
        return self.farbe

    def setPlayerNumber(self, numberOfPlayer):
        self.playerNumber = numberOfPlayer

    def getPlayerNumber(self):
        return self.playerNumber

    def isEmpty(self):
        return self.playerNumber == 0

    def placeChip(self, color, playerNumber):
        self.playerNumber = playerNumber
        feld_y = 100 + size * self.feldX
        feld_x = 375 + size * self.feldY
        offset = 20
        self.playerChip = createPlayerChip(self.background, feld_x + offset, feld_y + offset, size - offset * 2, color)

    def deleteChip(self):
        if self.playerChip is not None and not self.isEmpty():
            self.background.delete(self.playerChip)


# Repräsentiert einen Spieler
class Player:

    def __init__(self, playerColor, name, playerNumber):
        self.playerNumber = playerNumber
        self.playerColor = playerColor
        self.name = name

    def getName(self):
        return self.name

    def getPlayerColor(self):
        return self.playerColor

    def setPlayerColor(self, playerColor):
        self.playerColor = playerColor

    def setName(self, name):
        self.name = name

    def getPlayerNumber(self):
        return self.playerNumber


# Kreise im Startgame Bildschirm
canvas_width = 200
canvas_height = 40

colorOfPlayer1 = 'red'
colorOfPlayer2 = 'yellow'

player1 = Player(colorOfPlayer1, playerName1, 1)
player2 = Player(colorOfPlayer2, playerName2, 2)

spielerAnDerReihe = player1


# create
def createPlayerChip(canvas, x, y, chipSize, color):
    chip = canvas.create_oval(x, y, x + chipSize, y + chipSize, fill=color)
    return chip


background = Canvas(width=gui.winfo_screenwidth(), height=gui.winfo_screenheight(), bg='grey')
background.pack(expand=YES, fill=BOTH)


def chooseColorPlayer1():
    global colorOfPlayer1
    colorOfPlayer1 = colorchooser.askcolor(title="Choose color", initialcolor=colorOfPlayer1)[1]
    background.itemconfig(chip1, fill=colorOfPlayer1)


def chooseColorPlayer2():
    global colorOfPlayer2
    colorOfPlayer2 = colorchooser.askcolor(title="Choose color", initialcolor=colorOfPlayer2)[1]
    background.itemconfig(chip2, fill=colorOfPlayer2)


chip1 = createPlayerChip(background, 800, 310, 80, colorOfPlayer1)
chip2 = createPlayerChip(background, 800, 410, 80, colorOfPlayer2)

background.tag_bind(chip1, '<Button-1>', lambda a: chooseColorPlayer1())
background.tag_bind(chip2, '<Button-1>', lambda a: chooseColorPlayer2())

vierGewinnt = background.create_text(960, 200, text="VierGewinnt", fill="black", font=("Purisa", 100))
# Button und Textfeld code(Startbildschirm)

startButton = Button(gui, width=30, height=6, bg='grey')
startButton["text"] = "Start"
startButton["command"] = lambda: startGame()
startButton.place(x=890, y=540)

tf_player1 = Entry(gui, bg='grey', width=25, font=("Purisa", 14))
tf_player1.place(x=900, y=340)
tf_player1.insert(0, 'Spieler 1')

tf_player2 = Entry(gui, bg='grey', width=25, font=("Purisa", 14))
tf_player2.place(x=900, y=440)
tf_player2.insert(0, 'Spieler 2')


def startGame():
    global player1
    global player2
    global background
    global vierGewinnt
    if player1.name != "" and player2.name != "":
        player1.setName(tf_player1.get())
        player2.setName(tf_player2.get())
        player1.setPlayerColor(colorOfPlayer1)
        player2.setPlayerColor(colorOfPlayer2)

        background.delete(chip1)
        background.delete(chip2)
        background.delete(vierGewinnt)
        startButton.destroy()
        setupSpielFeld()
        setupPlayerListBar()

        tf_player1.destroy()
        tf_player2.destroy()

        createControlButtons()

        buttemporaer2 = Button(gui, width=20, height=6, bg='grey')
        buttemporaer2["text"] = "RestartTest"
        buttemporaer2["command"] = lambda: restartGame()
        buttemporaer2.place(x=1020, y=740)

        buttemporaer3 = Button(gui, width=20, height=6, bg='grey')
        buttemporaer3["text"] = "Back To Start Menu"
        buttemporaer3["command"] = lambda: backToStartMenu()
        buttemporaer3.place(x=520, y=740)

    else:
        print("Keine Namen sind gesetzt")


spielfeld = []
playerListBar = 0


def setupPlayerListBar():
    global background
    global playerListBar
    playerListBar = PlayerListBar(background)


def nextRound():
    global roundNumber
    global playerListBar
    roundNumber = roundNumber + 1
    print('Round Number:', roundNumber)
    playerListBar.tauscheSpielerAnDerReihe()


def setupSpielFeld():
    global background
    # x Koordinate Berechnung
    for v in range(1, verticalFeldNumber):
        # y Koordinate Berechnung
        horizontalLineList = []
        for h in range(1, horizontalFeldNumber):
            feld = VierGewinntFeld(background, h, v)
            horizontalLineList.append(feld)
        spielfeld.append(horizontalLineList)


def createControlButtons():
    for y in range(1, verticalFeldNumber):
        createControlButton(y)


def createControlButton(row):
    button_x = 375 + size * row
    if row != 1:
        button_x = button_x + 1
    controlButton = Button(gui, width=17, height=3, bg='grey')
    controlButton["text"] = "↓"
    controlButton["command"] = lambda: handlePlayerChip(row)
    controlButton.place(x=button_x, y=172)


def handlePlayerChip(row):
    feld = getPositonForChip(row)
    if feld is not None:
        feld.placeChip(spielerAnDerReihe.getPlayerColor(), spielerAnDerReihe)
        nextRound()


def getPositonForChip(row):
    felderReihe = getFelderReihe(row - 1)
    for feld in reversed(felderReihe):
        if feld.isEmpty():
            return feld


def getFelderReihe(index):
    for i, j in enumerate(spielfeld):
        if i == index:
            return j


def getFeld(horizontal, vertical):
    for i, j in enumerate(spielfeld):
        if i == horizontal:
            for i2, j2 in enumerate(j):
                if i2 == vertical:
                    return j2


# bei game restart
def restartGame():
    # Button und Textfeld code(Startbildschirm)
    print('Restarted!')


def backToStartMenu():
    global tf_player1
    global tf_player2
    global spielerAnDerReihe
    global chip1
    global chip2
    global startButton
    global spielfeld
    global vierGewinnt
    global player1
    global player2

    chip1 = createPlayerChip(background, 850, 310, 80, player1.getPlayerColor())
    chip2 = createPlayerChip(background, 850, 410, 80, player2.getPlayerColor())

    background.tag_bind(chip1, '<Button-1>', lambda a: chooseColorPlayer1())
    background.tag_bind(chip2, '<Button-1>', lambda a: chooseColorPlayer2())

    vierGewinnt = background.create_text(960, 200, text="VierGewinnt", fill="black", font=("Purisa", 100))

    # Button und Textfeld code(Startbildschirm)

    startButton = Button(gui, width=30, height=6, bg='grey')
    startButton["text"] = "Start"
    startButton["command"] = lambda: startGame()
    startButton.place(x=890, y=540)

    tf_player1 = Entry(gui, bg='grey', width=30)
    tf_player1.place(x=950, y=330)
    tf_player1.insert(0, 'Spieler 1')

    tf_player2 = Entry(gui, bg='grey', width=30)
    tf_player2.place(x=950, y=430)
    tf_player2.insert(0, 'Spieler 2')

    spielerAnDerReihe = player1
    spielfeld.clear()


gui.mainloop()
