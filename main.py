from tkinter import *
from tkinter import colorchooser

gui = Tk()
width, height = gui.winfo_screenwidth(), gui.winfo_screenheight()
gui.geometry("%dx%d+0+0" % (width, height))
gui.state('zoomed')
gui.title('Vier Gewinnt')

print('max. Länge:', width)
print('max. Höhe:', height)


# Repräsentiert das Settings Menu im Startmenü
class Settings:
    def __init__(self):
        self.settingsButton = None
        self.controlButtons = False
        # Liste aller interaktiven Schaltfläschen, die Beteiligt sind
        self.options = []

    # Erstellt den Button, um auf das Menu zugreifen zu können
    def createButton(self):
        self.settingsButton = Button(gui, width=30, height=6, bg=buttonColor)
        self.settingsButton["text"] = "Einstellungen"
        self.settingsButton["command"] = lambda: self.createOptions()
        self.settingsButton.place(x=890, y=650)

    # löscht nur den Einstellungs Menu Button
    def deleteMenuButton(self):
        if self.settingsButton is not None:
            self.settingsButton: Button
            self.settingsButton.destroy()
            self.settingsButton = None

    # erstellt die Buttons für das Einstellungs Menu
    def createOptions(self):
        # löschen des Menu Buttons
        self.deleteMenuButton()

        # löschen des Startmenüs
        deleteStartMenu()

        backButton = Button(gui, width=30, height=6, bg=buttonColor)
        backButton["text"] = "Zurück zum Startmenü"
        backButton["command"] = lambda: self.backToStartMenu()
        backButton.place(x=890, y=650)
        self.options.append(backButton)

        controlOption = Button(gui, width=30, height=6, bg=buttonColor)
        controlOption["text"] = str(self.controlButtons)
        controlOption["command"] = lambda: self.switchControlButtonState()
        controlOption.place(x=890, y=540)
        self.options.append(controlOption)

    # löscht die Buttons vom Einstellungs Menu
    def deleteOptions(self):
        for index, button in enumerate(self.options):
            button: Button
            button.destroy()

        self.options.clear()

    # geht wieder zurück zum Startbildschirm
    def backToStartMenu(self):
        self.deleteMenuButton()
        self.deleteOptions()
        createStartMenu()

    # ändert den Button Text zwischen True und False, wenn die Einstellung geändert wird
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
            self.menuButton = Button(gui, width=20, height=5, bg=buttonColor)
            self.menuButton["text"] = "Menü"
            self.menuButton["command"] = lambda: self.toggleMenu()
            self.menuButton.place(x=1710, y=100)
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
            self.backToSMButton = Button(gui, width=20, height=5, bg=buttonColor)
            self.backToSMButton["text"] = "Zurück zum Startmenü"
            self.backToSMButton["command"] = lambda: backToStartMenu()
            self.backToSMButton.place(x=1710, y=190)

            self.restartButton = Button(gui, width=20, height=5, bg=buttonColor)
            self.restartButton["text"] = "Neustart"
            self.restartButton["command"] = lambda: restartGame()
            self.restartButton.place(x=1710, y=280)

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
        global otherPlayerColor

        self.Rechteck = background.create_rectangle(0, 0, 1920, 60, fill=playerListBarColor, outline=playerListBarOutlineColor)
        self.Bindestrich = background.create_text(960, 30, text='-', fill='#000000', font=('Purisa', 22))

        if spielerAnDerReihe.getPlayerNumber() == 1:
            self.Spieler1 = background.create_text(820, 30, text=player1.name, fill=player1.getPlayerColor(),
                                                   font=('Purisa', 18, 'bold'))
        else:
            self.Spieler1 = background.create_text(820, 30, text=player1.name, fill=otherPlayerColor, font=('Purisa', 18))

        if spielerAnDerReihe.getPlayerNumber() == 2:
            self.Spieler2 = background.create_text(1100, 30, text=player2.name, fill=player2.getPlayerColor(),
                                                   font=('Purisa', 18, 'bold'))
        else:
            self.Spieler2 = background.create_text(1100, 30, text=player2.name, fill=otherPlayerColor,
                                                   font=('Purisa', 18))

    # tauscht den Spieler, der an der Reihe ist
    def tauscheSpielerAnDerReihe(self):
        global background
        global spielerAnDerReihe
        global otherPlayerColor

        if spielerAnDerReihe.getPlayerNumber() == 1:
            spielerAnDerReihe = player2
        elif spielerAnDerReihe.getPlayerNumber() == 2:
            spielerAnDerReihe = player1
        else:
            print('Error!!! SpielerAnDerReihe:', spielerAnDerReihe)

        if spielerAnDerReihe.getPlayerNumber() == 1:
            background.itemconfig(self.Spieler1, fill=player1.getPlayerColor(), font=('Purisa', 18, 'bold'))
            background.itemconfig(self.Spieler2, fill=otherPlayerColor, font=('Purisa', 18))
        elif spielerAnDerReihe.getPlayerNumber() == 2:
            background.itemconfig(self.Spieler1, fill=otherPlayerColor, font=('Purisa', 18))
            background.itemconfig(self.Spieler2, fill=player2.getPlayerColor(), font=('Purisa', 18, 'bold'))

    def setSpielerAnDerReihe(self, playerNumber):
        global background
        global spielerAnDerReihe
        global otherPlayerColor

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
                background.itemconfig(self.Spieler2, fill=otherPlayerColor, font=('Purisa', 18))
            elif playerNumber == 2:
                background.itemconfig(self.Spieler1, fill=otherPlayerColor, font=('Purisa', 18))
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

        self.placeChip(backgroundColor, 0)

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
    def placeChip(self, color, playerNumber: int):
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

# Überprüfungsgröße
connect = 5

# Farben
defaultSpielfeldFarbe = '#2000FF'
backgroundColor = '#8D9495'
playerListBarColor = '#788688'
playerListBarOutlineColor = '#C0C0C0'
buttonColor = '#95A9AD'
textFeldColor = '#A4A4A4'
# Farbe des Spielers, der nicht an der Reihe ist
otherPlayerColor = '#5A5A5A'

# Spielfeldgröße
horizontalFeldNumber = 7
verticalFeldNumber = 8

# default Spieler Name
playerName1 = 'Spieler 1'
playerName2 = 'Spieler 2'

# Spielerkreise im Startbildschirm
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
# wird gebraucht um in startGame() die Buttons und usw vom Startmenü zu löschen
restarted = False

# kann das Setzen von Chips verhindern
shouldPlaceChip = True

win = False

# Erstellung des haupt Canvas
background = Canvas(width=gui.winfo_screenwidth(), height=gui.winfo_screenheight(), bg=backgroundColor)
background.pack(expand=YES, fill=BOTH)


# Hilfsfunktion um einen Spieler Chip auf dem Bildschirm darzustellen
def createPlayerChip(canvas, x, y, chipSize, color):
    chip = canvas.create_oval(x, y, x + chipSize, y + chipSize, fill=color)
    return chip


# setzen der Chip Variablen für die Spieler im Startmenü
chip1 = createPlayerChip(background, 800, 310, 80, colorOfPlayer1)
chip2 = createPlayerChip(background, 800, 410, 80, colorOfPlayer2)

# Wenn der <Button-1> gedrückt wird (links Klick) →
# wird die Farbe abgefragt über chooseColorPlayer1() / chooseColorPlayer2()
background.tag_bind(chip1, '<Button-1>', lambda a: chooseColorPlayer1())
background.tag_bind(chip2, '<Button-1>', lambda a: chooseColorPlayer2())

vierGewinnt = background.create_text(960, 200, text="Vier Gewinnt", fill="black", font=("Purisa", 100))

# Start Button wird gesetzt
startButton = Button(gui, width=30, height=6, bg=buttonColor)
startButton["text"] = "Start"
startButton["command"] = lambda: startGame()
startButton.place(x=890, y=540)

# Textfeld für Spieler 1
tf_player1 = Entry(gui, bg=textFeldColor, width=25, font=("Purisa", 14))
tf_player1.place(x=900, y=340)
tf_player1.insert(0, 'Spieler 1')

# Textfeld für Spieler 2
tf_player2 = Entry(gui, bg=textFeldColor, width=25, font=("Purisa", 14))
tf_player2.place(x=900, y=440)
tf_player2.insert(0, 'Spieler 2')

# Settings Menu im Startmenü
settingsMenu = Settings()
settingsMenu.createButton()

# erstellen der InGameMenu Klasse
menu = InGameMenu()

# Liste enthält weitere Listen → diese Listen repräsentieren eine vertikale Linie von den Vierecken
spielfeld = []

# Spielerleisten Variable
playerListBar = PlayerListBar()


def playerNumberToPlayer(playerNumber: int):
    if playerNumber == 1:
        return player1
    elif playerNumber == 2:
        return player2
    else:
        return None


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


def deleteStartMenu():
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

        deleteStartMenu()

        checkRestart()

    else:
        print("Keine Namen sind gesetzt")


# Überprüft, ob das Spiel restarted wurde → im Fall, das es restartet werden muss, werden die Startmenüelemente gelöscht
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
    global spielerAnDerReihe
    global win
    if not win:
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
    controlButton = Button(gui, width=17, height=3, bg=buttonColor)
    controlButton["text"] = "↓"
    controlButton["command"] = lambda: handlePlayerChip(row)
    controlButton.place(x=button_x, y=172)
    buttons.append(controlButton)


# setzt den Chip an der richtigen stelle, damit die Physics funktionieren
def handlePlayerChip(row):
    feld: VierGewinntFeld = getPositonForChip(row)
    if feld is not None:
        if shouldPlaceChip:
            feld.placeChip(spielerAnDerReihe.getPlayerColor(), spielerAnDerReihe.getPlayerNumber())
            winCheck(spielerAnDerReihe.getPlayerNumber())
            nextRound()


# berechnet die richtige Stelle im Spielfeld für den Spielerchip
def getPositonForChip(row):
    felderReihe = getFelderReihe(row - 1)
    for feld in reversed(felderReihe):
        if feld.isEmpty():
            return feld


# Helferfunktion, mit der man eine vertikale Reihe bekommt
def getFelderReihe(vertikaleReihenNummer):
    return spielfeld[vertikaleReihenNummer]


# Bekommt das Feld, mit den angegebenen Koordinaten
def getFeld(horizontaleNummer: int, vertikaleNummer: int):
    #    return spielfeld[horizontaleNummer][vertikaleNummer]
    for indexVertikal, vertikaleListe in enumerate(spielfeld):
        if indexVertikal == horizontaleNummer:
            for indexHorizontal, viereck in enumerate(vertikaleListe):
                viereck: VierGewinntFeld
                if indexHorizontal == vertikaleNummer:
                    return viereck
    return None


def getPlayerNumberOfFeld(horizontaleNummer: int, vertikaleNummer: int):
    feld = getFeld(horizontaleNummer, vertikaleNummer)
    if feld is not None:
        return feld.getPlayerNumber()
    else:
        return 0


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


# erstellt nur das Start Menu
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
    global shouldPlaceChip

    chip1 = createPlayerChip(background, 800, 310, 80, colorOfPlayer1)
    chip2 = createPlayerChip(background, 800, 410, 80, colorOfPlayer2)

    background.tag_bind(chip1, '<Button-1>', lambda a: chooseColorPlayer1())
    background.tag_bind(chip2, '<Button-1>', lambda a: chooseColorPlayer2())

    vierGewinnt = background.create_text(960, 200, text="Vier Gewinnt", fill="black", font=("Purisa", 100))

    # Button und Textfeld code(Startbildschirm)

    startButton = Button(gui, width=30, height=6, bg=buttonColor)
    startButton["text"] = "Start"
    startButton["command"] = lambda: startGame()
    startButton.place(x=890, y=540)

    tf_player1 = Entry(gui, bg=textFeldColor, width=25, font=("Purisa", 14))
    tf_player1.place(x=900, y=340)
    tf_player1.insert(0, 'Spieler 1')

    tf_player2 = Entry(gui, bg=textFeldColor, width=25, font=("Purisa", 14))
    tf_player2.place(x=900, y=440)
    tf_player2.insert(0, 'Spieler 2')

    shouldPlaceChip = True

    settingsMenu.createButton()


# geht zum Startmenü zurück
def backToStartMenu():
    global spielerAnDerReihe
    global restarted
    global roundNumber
    global win

    createStartMenu()
    deleteInGameItems()

    spielerAnDerReihe = player1
    restarted = True
    win = False
    roundNumber = 0


def restartGame():
    global playerListBar
    global spielerAnDerReihe
    global win

    playerListBar.setSpielerAnDerReihe(1)
    spielerAnDerReihe = player1

    global roundNumber
    global shouldPlaceChip
    roundNumber = 0
    win = False

    for indexVertikal, vertikaleListe in enumerate(spielfeld):
        for indexHorizontal, viereck in enumerate(vertikaleListe):
            viereck: VierGewinntFeld
            if not viereck.isEmpty():
                viereck.deleteChip()
                viereck.setColor(defaultSpielfeldFarbe)
                viereck.placeChip(backgroundColor, 0)


# allgemeine Gewinn Überprüfung
def winCheck(playerNumber: int):
    global win
    for h in range(horizontalFeldNumber):
        for v in range(verticalFeldNumber):
            if (checkSingleLineClear(h, v, 1, playerNumber) == True
                    or checkSingleLineClear(h, v, 2, playerNumber) == True
                    or checkSingleLineClear(h, v, 3, playerNumber) == True
                    or checkSingleLineClear(h, v, 4, playerNumber)):
                win = True


# Überprüft, ob jemand in einer Linie gewonnen hat
def checkSingleLineClear(horizontaleNummer: int, vertikaleNummer: int, operationType: int, playerNumber: int):
    feldWinListCheckOne: list[VierGewinntFeld] = []
    feldWinList: list[VierGewinntFeld] = []
    if operationType == 1:
        for index in range(connect):
            feldWinListCheckOne.append(checkSingleFieldWin(horizontaleNummer, vertikaleNummer + index, playerNumber))
    elif operationType == 2:
        for index in range(connect):
            feldWinListCheckOne.append(checkSingleFieldWin(horizontaleNummer + index, vertikaleNummer, playerNumber))
    elif operationType == 3:
        for index in range(connect):
            feldWinListCheckOne.append(checkSingleFieldWin(horizontaleNummer + index, vertikaleNummer + index, playerNumber))
    elif operationType == 4:
        for index in range(connect):
            feldWinListCheckOne.append(checkSingleFieldWin(horizontaleNummer - index, vertikaleNummer + index, playerNumber))

    for index, feld in enumerate(feldWinListCheckOne):
        if feld is not None:
            feldWinList.append(feld)

    if len(feldWinList) == len(feldWinListCheckOne):
        winScreen(playerNumberToPlayer(playerNumber))
        for index, feld in enumerate(feldWinList):
            feld.setColor('green')
        return True
    else:
        return False


def checkSingleFieldWin(horizontaleNummer: int, vertikaleNummer: int, playerNumber: int):
    feld = getFeld(horizontaleNummer, vertikaleNummer)

    if feld is not None:
        if feld.getPlayerNumber() == playerNumber:
            return feld
        else:
            return None
    else:
        return None


def winScreen(player: Player):
    global shouldPlaceChip
    global menu

    print("Der Spieler: " + player.getName() + " hat gewonnen")

    shouldPlaceChip = False

    rectangle = background.create_rectangle(840, 450, 1080, 800, fill="#3A3A3A", outline='#6F6F6F')
    text = background.create_text(960, 500, text="Der Spieler", fill="black", font=("Purisa", 20))
    text2 = background.create_text(960, 535, text=player.getName(), fill=player.getPlayerColor(), font=("Purisa", 20, "bold"))
    text3 = background.create_text(960, 565, text="hat gewonnen", fill="black", font=("Purisa", 20))

    menu.deleteAllButtons()

    restartButton = Button(gui, width=25, height=4, bg=buttonColor)
    restartButton["text"] = "Neustart"
    restartButton["command"] = lambda: restartFromWinScreen(backButton, restartButton, rectangle, text, text2, text3)
    restartButton.place(x=867, y=610)

    backButton = Button(gui, width=25, height=4, bg=buttonColor)
    backButton["text"] = "Zurück zum Startmenü"
    backButton["command"] = lambda: backToStartMenuFromWinScreen(backButton, restartButton, rectangle, text, text2, text3)
    backButton.place(x=867, y=690)


def backToStartMenuFromWinScreen(backButton: Button, restartButton: Button, rectangle, text, text2, text3):
    backButton.destroy()
    restartButton.destroy()
    background.delete(rectangle)
    background.delete(text)
    background.delete(text2)
    background.delete(text3)
    backToStartMenu()


def restartFromWinScreen(backButton: Button, restartButton: Button, rectangle, text, text2, text3):
    global shouldPlaceChip
    global menu

    shouldPlaceChip = True
    backButton.destroy()
    restartButton.destroy()
    background.delete(rectangle)
    background.delete(text)
    background.delete(text2)
    background.delete(text3)
    menu.createMenuButton()
    restartGame()


gui.mainloop()
