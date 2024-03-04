from tkinter import *
from tkinter import colorchooser

gui = Tk()
width, height = gui.winfo_screenwidth(), gui.winfo_screenheight()
gui.geometry("%dx%d+0+0" % (width, height))
gui.state('zoomed')
gui.title('Vier Gewinnt')

print('max. Länge:', width)
print('max. Höhe:', height)


# Repräsentiert das Settings Menu im Hauptmenü
class Settings:
    def __init__(self):
        self.settingsButton = None
        self.controlButtons = False
        # Liste aller interaktiven Schaltfläschen, die Beteiligt sind
        self.options = []

    def createButton(self):
        self.settingsButton = Button(gui, width=30, height=6, bg='grey')
        self.settingsButton["text"] = "Einstellungen"
        self.settingsButton["command"] = lambda: self.createOptions()
        self.settingsButton.place(x=890, y=700)

    def deleteMenuButton(self):
        if self.settingsButton is not None:
            self.settingsButton: Button
            self.settingsButton.destroy()
            self.settingsButton = None

    def createOptions(self):
        # löschen des Menu Buttons
        self.deleteMenuButton()

        # löschen des Haupt Menus
        deleteHauptMenu()

        backButton = Button(gui, width=30, height=6, bg='grey')
        backButton["text"] = "Zurück"
        backButton["command"] = lambda: self.backToStartMenu()
        backButton.place(x=890, y=700)
        self.options.append(backButton)

        controlOption = Button(gui, width=30, height=6, bg='grey')
        controlOption["text"] = str(self.controlButtons)
        controlOption["command"] = lambda: self.switchControlButtonState()
        controlOption.place(x=890, y=550)
        self.options.append(controlOption)

    def deleteOptions(self):
        for index, button in enumerate(self.options):
            button: Button
            button.destroy()

        self.options.clear()

    def backToStartMenu(self):
        self.deleteMenuButton()
        self.deleteOptions()
        createStartMenu()

    def switchControlButtonState(self):
        if not self.controlButtons:
            self.controlButtons = True
            button = self.options[1]
            button['text'] = str(self.controlButtons)
            self.options[1] = button
        else:
            self.controlButtons = False
            button = self.options[1]
            button['text'] = str(self.controlButtons)
            self.options[1] = button


# Repräsentiert das in Game Menu
class InGameMenu:
    def __init__(self):
        # Button Variablen, um einzelne Buttons zu haben
        self.menuButton = None
        self.backToSMButton = None
        self.restartButton = None
        # Liste zum Speichern aller Buttons
        self.buttonList = []
        # Überprüfung, ob das Menu offen ist
        self.statusOpen = False

    # erstellt nur den Menu Button
    def createMenuButton(self):
        if self.menuButton is None:
            self.menuButton = Button(gui, width=15, height=5, bg='grey')
            self.menuButton["text"] = "Menü"
            self.menuButton["command"] = lambda: self.toggleMenu()
            self.menuButton.place(x=1780, y=70)
            self.buttonList.append(self.menuButton)
        else:
            print('Wie kam es zu diesem Fehler? der Menu Button ist schon da')

    # toggeln zwischen Menu an/aus
    def toggleMenu(self):
        if self.statusOpen:
            self.closeMenu()
        else:
            self.openMenu()

    def openMenu(self):
        if not self.statusOpen:
            self.backToSMButton = Button(gui, width=20, height=6, bg='grey')
            self.backToSMButton["text"] = "Back To Start Menu"
            self.backToSMButton["command"] = lambda: backToStartMenu()
            self.backToSMButton.place(x=1780, y=150)

            self.restartButton = Button(gui, width=20, height=6, bg='grey')
            self.restartButton["text"] = "Restart Button"
            self.restartButton["command"] = lambda: restartGame()
            self.restartButton.place(x=1780, y=250)

            self.buttonList.append(self.backToSMButton)
            self.buttonList.append(self.restartButton)
            self.statusOpen = True

    def closeMenu(self):
        if self.statusOpen:
            self.statusOpen = False

            # die backToSmButton-Variable wird der Button Klasse zugeordnet
            self.backToSMButton: Button
            self.backToSMButton.destroy()

            # die restartButton-Variable wird der Button Klasse zugeordnet
            self.restartButton: Button
            self.restartButton.destroy()

            self.buttonList.remove(self.backToSMButton)
            self.buttonList.remove(self.restartButton)

            self.backToSMButton = None
            self.restartButton = None

    # Um alle Buttons bei restart zu löschen
    def deleteAllButtons(self):
        for index, button in enumerate(self.buttonList):
            # die Button-Variable wird der Button Klasse zugeordnet
            button: Button
            button.destroy()

        self.menuButton = None
        self.backToSMButton = None
        self.restartButton = None

        self.buttonList.clear()
        self.statusOpen = False


# Repräsentiert die Spieler Leiste
class PlayerListBar:

    # erstellt die obere Leiste mit Spielernamen
    def __init__(self):
        self.Bindestrich = None
        self.Rechteck = None
        self.Spieler1 = None
        self.Spieler2 = None

    def createPlayerListBar(self):
        global background
        global spielerAnDerReihe
        self.Rechteck = background.create_rectangle(0, 0, 1920, 60, fill="#585B5F")
        self.Bindestrich = background.create_text(960, 30, text='-', fill='#000000', font=('Purisa', 22))

        if spielerAnDerReihe.getPlayerNumber() == 1:
            self.Spieler1 = background.create_text(820, 30, text=player1.name, fill=player1.getPlayerColor(),
                                                   font=('Purisa', 18, 'bold'))
        else:
            self.Spieler1 = background.create_text(820, 30, text=player1.name, fill='#847B79', font=('Purisa', 18))

        if spielerAnDerReihe.getPlayerNumber() == 2:
            self.Spieler2 = background.create_text(1100, 30, text=player2.name, fill=player2.getPlayerColor(),
                                                   font=('Purisa', 18, 'bold'))
        else:
            self.Spieler2 = background.create_text(1100, 30, text=player2.name, fill='#847B79',
                                                   font=('Purisa', 18))

    # tauscht den Spieler, der an der Reihe ist
    def tauscheSpielerAnDerReihe(self):
        global background
        global spielerAnDerReihe

        if spielerAnDerReihe.getPlayerNumber() == 1:
            spielerAnDerReihe = player2
        elif spielerAnDerReihe.getPlayerNumber() == 2:
            spielerAnDerReihe = player1
        else:
            print('Error!!! SpielerAnDerReihe:', spielerAnDerReihe)

        if spielerAnDerReihe.getPlayerNumber() == 1:
            background.itemconfig(self.Spieler1, fill=player1.getPlayerColor(), font=('Purisa', 18, 'bold'))
            background.itemconfig(self.Spieler2, fill='#847B79', font=('Purisa', 18))
        elif spielerAnDerReihe.getPlayerNumber() == 2:
            background.itemconfig(self.Spieler1, fill='#847B79', font=('Purisa', 18))
            background.itemconfig(self.Spieler2, fill=player2.getPlayerColor(), font=('Purisa', 18, 'bold'))

    def setSpielerAnDerReihe(self, playerNumber):
        global background
        global spielerAnDerReihe

        # überprüfen ob dieser Spieler nicht an der Reihe ist
        if spielerAnDerReihe.getPlayerNumber() != playerNumber:
            if playerNumber == 1:
                spielerAnDerReihe = player2
            elif playerNumber == 2:
                spielerAnDerReihe = player1
            else:
                print('Error!!! SpielerAnDerReihe:', spielerAnDerReihe)

            if playerNumber == 1:
                background.itemconfig(self.Spieler1, fill=player1.getPlayerColor(), font=('Purisa', 18, 'bold'))
                background.itemconfig(self.Spieler2, fill='#847B79', font=('Purisa', 18))
            elif playerNumber == 2:
                background.itemconfig(self.Spieler1, fill='#847B79', font=('Purisa', 18))
                background.itemconfig(self.Spieler2, fill=player2.getPlayerColor(), font=('Purisa', 18, 'bold'))

    def deletePlayerListBar(self):
        global background
        background.delete(self.Spieler1)
        background.delete(self.Spieler2)
        background.delete(self.Rechteck)
        background.delete(self.Bindestrich)


# Repräsentiert ein Feld → ein Viereck des Spielfelds
class VierGewinntFeld:

    # Erstellen des Vierecks
    def __init__(self, horizontal, vertikal):
        global background
        global defaultSpielfeldFarbe
        # erstellen eines leeren Feldes
        self.playerChip = None
        self.playerNumber = 0
        self.horizontal = horizontal
        self.vertikal = vertikal
        self.farbe = defaultSpielfeldFarbe

        feld_y = 100 + size * self.horizontal
        feld_x = 375 + size * self.vertikal

        self.feld = background.create_rectangle(feld_x, feld_y, feld_x + size,
                                                feld_y + size, fill=self.farbe)

        if not settingsMenu.controlButtons:
            # gibt dem Feld die Funktion bei einem Linksklick, den Chip mit Physics hinzusetzten
            background.tag_bind(self.feld, '<Button-1>', lambda a: handlePlayerChip(self.vertikal))

        self.placeChip('black', 0)

    def setColor(self, color):
        global background
        self.farbe = color
        background.itemconfig(self.feld, fill=color)

    def getColor(self):
        return self.farbe

    def setPlayerNumber(self, numberOfPlayer):
        self.playerNumber = numberOfPlayer

    def getPlayerNumber(self):
        return self.playerNumber

    # Überprüfung, ob das Viereck von einem Spieler besetzt ist oder nicht
    def isEmpty(self):
        return self.playerNumber == 0

    # setzt den Spieler Chip und ersetzt den Spieler 0 → Spieler 0 = leeres Feld
    def placeChip(self, color, playerNumber):
        global background
        if self.isEmpty():
            background.delete(self.playerChip)
        self.playerNumber = playerNumber
        feld_y = 100 + size * self.horizontal
        feld_x = 375 + size * self.vertikal
        offset = 20
        self.playerChip = createPlayerChip(background, feld_x + offset, feld_y + offset, size - offset * 2, color)

        if not settingsMenu.controlButtons:
            # gibt dem Chip die Funktion bei einem Linksklick, den Chip mit Physics hinzusetzten
            background.tag_bind(self.playerChip, '<Button-1>', lambda a: handlePlayerChip(self.vertikal))

    # löscht Spieler Chip, wenn es nicht ein leeres Feld
    def deleteChip(self):
        global background
        if self.playerChip is not None:
            background.delete(self.playerChip)


# Repräsentiert einen Spieler
class Player:

    # Initialisierung des Spielers
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


# Feld Größe Einstellung
size = 130

defaultSpielfeldFarbe = 'blue'

# Spielfeldgröße
horizontalFeldNumber = 7
verticalFeldNumber = 8

# default Spieler Name
playerName1 = 'Spieler 1'
playerName2 = 'Spieler 2'

# Kreise im Startgame Bildschirm
canvas_width = 200
canvas_height = 40

# default Spieler Farben
colorOfPlayer1 = 'red'
colorOfPlayer2 = 'yellow'

# Spieler Variablen
player1 = Player(colorOfPlayer1, playerName1, 1)
player2 = Player(colorOfPlayer2, playerName2, 2)

# Spieler an der Reihe
spielerAnDerReihe = player1

# Runden Nummer
roundNumber = 0

# Stellt dar, ob das Game restarted wurde oder nicht →
# wird gebraucht um in startGame() die Buttons und usw vom Hauptmenu zu löschen
restarted = False

# Erstellung des haupt Canvas
background = Canvas(width=gui.winfo_screenwidth(), height=gui.winfo_screenheight(), bg='grey')
background.pack(expand=YES, fill=BOTH)


# Hilfsfunktion um einen Spieler Chip auf dem Bildschirm darzustellen
def createPlayerChip(canvas, x, y, chipSize, color):
    chip = canvas.create_oval(x, y, x + chipSize, y + chipSize, fill=color)
    return chip


# setzen der Chip Variablen für die Spieler im Hauptmenü
chip1 = createPlayerChip(background, 800, 310, 80, colorOfPlayer1)
chip2 = createPlayerChip(background, 800, 410, 80, colorOfPlayer2)

# Wenn der <Button-1> gedrückt wird (links Klick) →
# wird die Farbe abgefragt über chooseColorPlayer1() / chooseColorPlayer2()
background.tag_bind(chip1, '<Button-1>', lambda a: chooseColorPlayer1())
background.tag_bind(chip2, '<Button-1>', lambda a: chooseColorPlayer2())

vierGewinnt = background.create_text(960, 200, text="Vier Gewinnt", fill="black", font=("Purisa", 100))

# Start Button wird gesetzt
startButton = Button(gui, width=30, height=6, bg='grey')
startButton["text"] = "Start"
startButton["command"] = lambda: startGame()
startButton.place(x=890, y=540)

# Textfeld für Spieler 1
tf_player1 = Entry(gui, bg='grey', width=25, font=("Purisa", 14))
tf_player1.place(x=900, y=340)
tf_player1.insert(0, 'Spieler 1')

# Textfeld für Spieler 2
tf_player2 = Entry(gui, bg='grey', width=25, font=("Purisa", 14))
tf_player2.place(x=900, y=440)
tf_player2.insert(0, 'Spieler 2')

# Settings Menu im Hauptmenü
settingsMenu = Settings()
settingsMenu.createButton()

# erstellen der InGameMenu Klasse
menu = InGameMenu()

# Liste enthält weitere Listen → diese Listen repräsentieren eine vertikale Linie von den Vierecken
spielfeld = []

# Spielerleisten Variable
playerListBar = PlayerListBar()


# öffnet das Coolor Chooser Menu für Spieler 1 und setzt die Farbe, wenn sie verändert wurde
def chooseColorPlayer1():
    global colorOfPlayer1
    colorOfPlayer1 = colorchooser.askcolor(title="Choose color", initialcolor=colorOfPlayer1)[1]
    background.itemconfig(chip1, fill=colorOfPlayer1)


# öffnet das Coolor Chooser Menu für Spieler 2 und setzt die Farbe, wenn sie verändert wurde
def chooseColorPlayer2():
    global colorOfPlayer2
    colorOfPlayer2 = colorchooser.askcolor(title="Choose color", initialcolor=colorOfPlayer2)[1]
    background.itemconfig(chip2, fill=colorOfPlayer2)


def deleteHauptMenu():
    global player1
    global player2
    global background
    global vierGewinnt
    global menu

    background.delete(chip1)
    background.delete(chip2)
    background.delete(vierGewinnt)
    startButton.destroy()
    settingsMenu.deleteMenuButton()
    tf_player1.destroy()
    tf_player2.destroy()
    settingsMenu.deleteMenuButton()
    settingsMenu.deleteOptions()


# Funktion fürs Starten vom Vier Gewinnt Spiel
def startGame():
    global player1
    global player2
    global background
    global vierGewinnt
    global menu
    if player1.name != "" and player2.name != "":
        player1.setName(tf_player1.get())
        player2.setName(tf_player2.get())
        player1.setPlayerColor(colorOfPlayer1)
        player2.setPlayerColor(colorOfPlayer2)

        # erstellt die Spieler Leiste und setzt die Variable
        global playerListBar
        playerListBar.createPlayerListBar()

        setupSpielFeld()
        createControlButtons()
        menu.createMenuButton()

        deleteHauptMenu()

        checkRestart()

    else:
        print("Keine Namen sind gesetzt")


# Überpruft, ob das Spiel restarted wurde → im Fall, das es restartet werden, muss werden die Hauptmenüelemente gelöscht
def checkRestart():
    global restarted
    global menu
    global settingsMenu
    if restarted:
        background.delete(chip1)
        background.delete(chip2)
        background.delete(vierGewinnt)
        startButton.destroy()
        tf_player1.destroy()
        tf_player2.destroy()
        settingsMenu.deleteMenuButton()
        restarted = False


# startet eine neue Runde
def nextRound():
    global roundNumber
    global playerListBar
    roundNumber = roundNumber + 1
    print('Round Number:', roundNumber)
    playerListBar.tauscheSpielerAnDerReihe()


# alle Vierecke werden in einer Reihe zu einem Spielfeld zusammen gesetzt
def setupSpielFeld():
    global background
    # x Koordinate Berechnung
    for v in range(1, verticalFeldNumber):
        # y Koordinate Berechnung
        horizontalLineList = []
        for h in range(1, horizontalFeldNumber):
            feld = VierGewinntFeld(h, v)
            horizontalLineList.append(feld)
        spielfeld.append(horizontalLineList)


# erstellt die Buttons, die in der Reihe einen neuen Chip hineinsetzten können
def createControlButtons():
    if settingsMenu.controlButtons:
        for y in range(1, verticalFeldNumber):
            createControlButton(y)


# Control Button Liste, um die Buttons später zu löschen
buttons = []


# Helferfunktion, um einen Control Button zu erstellen
def createControlButton(row):
    button_x = 375 + size * row
    if row != 1:
        button_x = button_x + 1
    controlButton = Button(gui, width=17, height=3, bg='grey')
    controlButton["text"] = "↓"
    controlButton["command"] = lambda: handlePlayerChip(row)
    controlButton.place(x=button_x, y=172)
    buttons.append(controlButton)


# setzt den Chip an der richtigen stelle, damit die Physics funtkionieren
def handlePlayerChip(row):
    feld = getPositonForChip(row)
    if feld is not None:
        feld.placeChip(spielerAnDerReihe.getPlayerColor(), spielerAnDerReihe)
        nextRound()


# berechnet die richtige Stelle im Spielfeld für den Spielerchip
def getPositonForChip(row):
    felderReihe = getFelderReihe(row - 1)
    for feld in reversed(felderReihe):
        if feld.isEmpty():
            return feld


# Helferfunktion, mit der man eine vertikale Reihe bekommt
def getFelderReihe(vertikaleReihenNummer):
    for index, vertikaleListe in enumerate(spielfeld):
        if index == vertikaleReihenNummer:
            return vertikaleListe


# Bekommt das Feld, mit den angegebenen Koordinaten
def getFeld(horizontaleNummer, vertikaleNummer):
    for indexVertikal, vertikaleListe in enumerate(spielfeld):
        if indexVertikal == horizontaleNummer:
            for indexHorizontal, viereck in enumerate(vertikaleListe):
                if indexHorizontal == vertikaleNummer:
                    return viereck


# löscht alle Elemente, die im Spielmenü da sind
def deleteInGameItems():
    global menu
    global background
    global spielfeld
    global buttons
    global playerListBar
    playerListBar.deletePlayerListBar()

    for indexVertikal, listeVertikal in enumerate(spielfeld):
        for indexHorizontal, viereck in enumerate(listeVertikal):
            background.delete(viereck.feld)
            viereck.deleteChip()

    for i, button in enumerate(buttons):
        button.destroy()

    spielfeld.clear()
    buttons.clear()
    menu.deleteAllButtons()


def createStartMenu():
    global tf_player1
    global tf_player2
    global chip1
    global chip2
    global startButton
    global spielfeld
    global vierGewinnt
    global player1
    global player2

    chip1 = createPlayerChip(background, 800, 310, 80, colorOfPlayer1)
    chip2 = createPlayerChip(background, 800, 410, 80, colorOfPlayer2)

    background.tag_bind(chip1, '<Button-1>', lambda a: chooseColorPlayer1())
    background.tag_bind(chip2, '<Button-1>', lambda a: chooseColorPlayer2())

    vierGewinnt = background.create_text(960, 200, text="Vier Gewinnt", fill="black", font=("Purisa", 100))

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

    settingsMenu.createButton()


# geht zum Startmenü zurück
def backToStartMenu():
    global spielerAnDerReihe
    global restarted
    global roundNumber

    createStartMenu()
    deleteInGameItems()

    spielerAnDerReihe = player1
    restarted = True
    roundNumber = 0


def restartGame():
    global playerListBar
    playerListBar.setSpielerAnDerReihe(1)

    global roundNumber
    roundNumber = 0

    for indexVertikal, vertikaleListe in enumerate(spielfeld):
        for indexHorizontal, viereck in enumerate(vertikaleListe):
            viereck: VierGewinntFeld
            if not viereck.isEmpty():
                viereck.deleteChip()
                viereck.placeChip('black', 0)


gui.mainloop()
