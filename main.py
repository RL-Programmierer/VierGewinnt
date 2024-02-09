from tkinter import *

gui = Tk()
w, h = gui.winfo_screenwidth(), gui.winfo_screenheight()
gui.geometry("%dx%d+0+0" % (w, h))
gui.title('VierGewinnt')
activeplayer = 1

# Feld Größe Einstellung
size = 130

horizontalFeldNumber = 7
verticalFeldNumber = 8


# Repräsentiert ein Feld
class VierGewinntFeld:
    feld = 0

    def __init__(self, feldX, feldY):
        self.feldX = feldX
        self.feldY = feldY

    def createCanvas(self, background):
        if self.feld == 0:
            feld_y = 50 + size * self.feldX
            feld_x = 375 + size * self.feldY

            self.feld = background.create_rectangle(feld_x, feld_y, feld_x + size,
                                                    feld_y + size, fill="white")
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

        buttemporaer = Button(gui, width=20, height=6, bg='grey')
        buttemporaer["text"] = "temporaer"
        buttemporaer["command"] = lambda: restartGame(background)
        buttemporaer.place(x=1020, y=740)

    else:
        print("Keine Namen sind gesetzt")


spielfeld = []


def setupPlayerListBar(background):
    global var1
    global var2
    global var3
    global var4

    var1 = background.create_rectangle(0, 0, 1920, 60, fill="#585B5F")

    if activeplayer == 1:
        var2 = background.create_text(820, 30, text=getPlayer1().name, fill='#000000', font=('Purisa', 18))
    else:
        var3 = background.create_text(820, 30, text=getPlayer1().name, fill='#847B79', font=('Purisa', 18))

    var4 = background.create_text(960, 30, text='-', fill='#000000', font=('Purisa', 22))

    if activeplayer == 2:
        background.create_text(1100, 30, text=getPlayer2().name, fill='#000000', font=('Purisa', 18))
    else:
        background.create_text(1100, 30, text=getPlayer2().name, fill='#847B79', font=('Purisa', 18))


def setupSpielFeld(background):
    # x Koordinate Berechnung
    for x in range(1, horizontalFeldNumber):
        # y Koordinate Berechnung
        for y in range(1, verticalFeldNumber):
            feld = VierGewinntFeld(x, y)
            feld.createCanvas(background)
            spielfeld.append(feld)


# bei game reset


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
    butrestart["text"] = "Start"
    butrestart["command"] = lambda: restartGame()
    butrestart.place(x=820, y=500)

    background.delete(var1)
    background.delete(var2)
    background.delete(var3)
    background.delete(var4)


gui.mainloop()
