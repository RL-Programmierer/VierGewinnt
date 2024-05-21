from tkinter import *
from tkinter import colorchooser
import random

gui = Tk()
width, height = gui.winfo_screenwidth(), gui.winfo_screenheight()
gui.geometry("%dx%d+0+0" % (width, height))
gui.state('zoomed')
gui.title('Vier Gewinnt')

print('max. Länge:', width)
print('max. Höhe:', height)


# Repräsentiert einen Spieler
class Player:

    # Initialisierung des Spielers
    def __init__(self, playerColor, name, playerNumber):
        self.playerNumber = playerNumber
        self.playerColor = playerColor
        self.name = name
        self.computerGegner = False

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

    def setComputerGegner(self, computerGegner: bool):
        self.computerGegner = computerGegner


# Screen System, um schnell vom einem zu einem andern Screen zu wechseln
# → kann beispielsweise das Startmenü repräsentieren
class Screen:
    def __init__(self, name: str):
        self.name = name
        self.overlays: list = []

    def create(self):
        pass

    def delete(self):
        pass

    def onSwitch(self):
        pass

    def clearOverlay(self, name: str):
        for index, screen in enumerate(self.overlays):
            if screen.name == name:
                screen.delete()
                self.overlays.remove(screen)

    def clearOverlays(self):
        for index, screen in enumerate(self.overlays):
            screen.delete()
        self.overlays.clear()

    def getOverlay(self, name: str):
        for index, screen in enumerate(self.overlays):
            if screen.name == name:
                return screen
        return None

    def addOverlayScreen(self, overlay):
        overlay: Screen

        if not self.containsOverlay(overlay.name):
            overlay.create()
            self.overlays.append(overlay)

    def containsOverlay(self, name: str):
        for index, screen in enumerate(self.overlays):
            if screen.name == name:
                return True
        return False

    def switchTo(self, toScreen):
        global currentScreen

        self.onSwitch()
        self.delete()
        self.clearOverlays()

        if isinstance(toScreen, Screen):
            toScreen: Screen
            toScreen.create()
            print("switched to:", toScreen.name)
        else:
            print("Die toScreen Variabel ist kein Screen! Derzeitiger Type der Variabel:", type(toScreen))

        currentScreen = toScreen


class StartScreen(Screen):

    def __init__(self):
        super().__init__("StartScreen")
        self.chip1 = None
        self.chip2 = None
        self.vierGewinntText = None
        self.startButton = None
        self.tf_player1 = None
        self.tf_player2 = None
        self.settingsButton = None

    def create(self):
        global spielfeld
        global player1
        global player2
        global shouldPlaceChip
        global textFeldColor
        global buttonColor

        self.chip1 = createPlayerChip(background, 800, 310, 80, colorOfPlayer1)
        self.chip2 = createPlayerChip(background, 800, 410, 80, colorOfPlayer2)

        background.tag_bind(self.chip1, '<Button-1>', lambda a: self.chooseColorPlayer1())
        background.tag_bind(self.chip2, '<Button-1>', lambda a: self.chooseColorPlayer2())

        self.vierGewinntText = background.create_text(960, 200, text="Vier Gewinnt", fill="black", font=("Purisa", 100))

        # Button und Textfeld code(Startbildschirm)

        if self.startButton is None:
            # Start Button wird gesetzt
            self.startButton = Button(gui, width=30, height=6, bg=buttonColor)
            self.startButton["text"] = "Start"
            self.startButton["command"] = lambda: currentScreen.switchTo(SpielfeldScreen())
            self.startButton.place(x=890, y=540)
        else:
            self.startButton.place(x=890, y=540)

        if self.tf_player1 is None:
            # Textfeld für Spieler 1
            self.tf_player1 = Entry(gui, bg=textFeldColor, width=25, font=("Purisa", 14))
            self.tf_player1.place(x=900, y=340)
            self.tf_player1.insert(0, playerName1)
        else:
            self.tf_player1.place(x=900, y=340)

        if self.tf_player2 is None:
            # Textfeld für Spieler 2
            self.tf_player2 = Entry(gui, bg=textFeldColor, width=25, font=("Purisa", 14))
            self.tf_player2.place(x=900, y=440)
            self.tf_player2.insert(0, playerName2)
        else:
            self.tf_player2.place(x=900, y=440)

        shouldPlaceChip = True

        if self.settingsButton is None:
            self.settingsButton = Button(gui, width=30, height=6, bg=buttonColor)
            self.settingsButton["text"] = "Einstellungen"
            self.settingsButton["command"] = lambda: self.switchTo(Settings())
            self.settingsButton.place(x=890, y=650)
        else:
            self.settingsButton.place(x=890, y=650)

        return self

    def onSwitch(self):
        global player1
        global player2
        global playerName1
        global playerName2
        global colorOfPlayer1
        global colorOfPlayer2

        playerName1 = self.tf_player1.get()
        playerName2 = self.tf_player2.get()
        player1.setName(self.tf_player1.get())
        player2.setName(self.tf_player2.get())
        player1.setPlayerColor(colorOfPlayer1)
        player2.setPlayerColor(colorOfPlayer2)

    def delete(self):
        global player1
        global player2
        global background

        background.delete(self.chip1)
        background.delete(self.chip2)
        background.delete(self.vierGewinntText)
        self.startButton.place_forget()
        self.tf_player1.place_forget()
        self.tf_player2.place_forget()
        self.settingsButton.place_forget()
        return self

    # öffnet das Color Chooser Menu für Spieler 1 und setzt die Farbe, wenn sie verändert wurde
    def chooseColorPlayer1(self):
        global colorOfPlayer1
        global defaultColorOfPlayer1
        color = colorchooser.askcolor(title="Choose color", initialcolor=defaultColorOfPlayer1)[1]
        if color is not None:
            colorOfPlayer1 = color
        background.itemconfig(self.chip1, fill=colorOfPlayer1)

    # öffnet das Color Chooser Menu für Spieler 2 und setzt die Farbe, wenn sie verändert wurde
    def chooseColorPlayer2(self):
        global colorOfPlayer2
        global defaultColorOfPlayer2
        color = colorchooser.askcolor(title="Choose color", initialcolor=defaultColorOfPlayer2)[1]
        if color is not None:
            colorOfPlayer2 = color
        background.itemconfig(self.chip2, fill=colorOfPlayer2)


class ErrorScreen(Screen):

    def __init__(self, errorMessage: str):
        super().__init__("ErrorScreen")
        self.errorMessage = errorMessage
        self.errorText = None

    def create(self):
        self.errorText = background.create_text(960, 200, text=self.errorMessage, fill="red", font=("Purisa", 100))

    def delete(self):
        background.delete(self.errorText)


class SpielfeldScreen(Screen):

    def __init__(self):
        super().__init__("SpielfeldScreen")
        self.active = False

    def create(self):
        if player1.name != "" and player2.name != "":
            self.active = True

            # alle Vierecke werden in einer Reihe zu einem Spielfeld zusammen gesetzt
            # x Koordinate Berechnung
            for v in range(1, int(getTextfieldOption(5, defaultVerticalFeldNumber))):
                # y Koordinate Berechnung
                horizontalLineList = []
                for h in range(1, int(getTextfieldOption(4, defaultHorizontalFeldNumber))):
                    feld = VierGewinntFeld(h, v)
                    horizontalLineList.append(feld)
                spielfeld.append(horizontalLineList)

            # erstellt die Spieler Leiste und setzt die Variable
            self.addOverlayScreen(PlayerListBar())
            self.addOverlayScreen(InGameMenu())

            createControlButtons()

            # Nur zum Testen da
            startButton2 = Button(gui, width=20, height=5, bg=buttonColor)
            startButton2["text"] = "CPU"
            startButton2["command"] = lambda: compGegner()
            startButton2.place(x=100, y=150)
        else:
            currentScreen.switchTo(StartScreen())
            print("Keine Namen sind gesetzt")

    def delete(self):
        global spielerAnDerReihe
        global win
        global roundNumber
        global background
        global spielfeld
        global buttons

        self.active = True

        for indexVertikal, listeVertikal in enumerate(spielfeld):
            for indexHorizontal, viereck in enumerate(listeVertikal):
                background.delete(viereck.feld)
                viereck.deleteChip()

        for i, button in enumerate(buttons):
            button.destroy()

        spielfeld.clear()
        buttons.clear()
        self.clearOverlays()

        spielerAnDerReihe = player1

        win = False
        roundNumber = 0


class SyncedTextField:
    def __init__(self, maxCharForEntry: int, x: int, y: int, w: int, font, defaultOption, desc: str, maxChar: int):
        self.maxCharForEntry = maxCharForEntry
        self.x = x
        self.y = y
        self.w = w
        self.font = font
        # self.defaultOption = defaultOption
        self.currentOption = defaultOption
        self.desc = desc
        self.maxChar = maxChar
        self.textField = None
        self.descItem = None

    def on_validate(self, P):
        if len(P) <= self.maxCharForEntry:
            return True
        else:
            return False

    def getCurrentOption(self):
        if self.textField is not None:
            self.currentOption = self.textField.get()
            return self.textField.get()
        else:
            return self.currentOption

    def create(self):
        self.textField: Entry = Entry(gui, bg=textFeldColor, width=self.w, font=self.font,
                                      validate='key', validatecommand=(gui.register(self.on_validate), '%P'))
        self.textField.place(x=self.x, y=self.y)
        self.textField.insert(0, self.currentOption)

        descList: list[str] = [self.desc[i:i + self.maxChar] for i in range(0, len(self.desc), self.maxChar)]
        self.descItem = MultilineDescription(self.desc, self.maxChar, self.font, self.x + (self.w * 5.6),
                                             self.y - (len(descList) * 20))
        return self

    def destroy(self):
        self.textField.place_forget()
        self.descItem.destroy()

    def show(self):
        self.textField.place(x=self.x, y=self.y)

        descList: list[str] = [self.desc[i:i + self.maxChar] for i in range(0, len(self.desc), self.maxChar)]
        self.descItem = MultilineDescription(self.desc, self.maxChar, self.font, self.x + (self.w * 5.6),
                                             self.y - (len(descList) * 20))


class MultilineDescription:
    def __init__(self, description: str, maxChar, font, x, y):
        global background
        descList: list[str] = [description[i:i + maxChar] for i in range(0, len(description), maxChar)]

        abstand = 20
        self.textList = []

        for index, desc in enumerate(descList):
            self.textList.append(background.create_text(x, y + (abstand * index), text=desc, font=font))

    def destroy(self):
        global background
        for index, text in enumerate(self.textList):
            background.delete(text)


class SwitchStateButton:
    def __init__(self, desc: str, textSize: int, maxChar: int, x, y, w, h, color, stateList: list, defaultState):
        global buttonColor
        correctColor = color
        if correctColor is None:
            correctColor = buttonColor

        self.desc = desc
        self.color = correctColor

        self.button = None

        self.states: list = stateList
        self.defaultState: int = self.states.index(defaultState)
        self.currentState: int = self.states.index(defaultState)

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.descText = None
        self.textSize = textSize
        self.maxChar = maxChar

    def create(self):
        if self.button is None:
            self.button: Button = Button(gui, width=self.w, height=self.h, bg=self.color)
            self.button["text"] = str(self.states[self.currentState])
            self.button["command"] = lambda: self.switchState()
            self.button.place(x=self.x, y=self.y)
        else:
            self.button.place(x=self.x, y=self.y)

        descList: list[str] = [self.desc[i:i + self.maxChar] for i in range(0, len(self.desc), self.maxChar)]

        self.descText = MultilineDescription(self.desc, self.maxChar, ('Purisa', self.textSize),
                                             self.x + (self.w * 3.6),
                                             self.y - (len(descList) * 20))

        return self

    def destroy(self):
        self.button.place_forget()
        self.descText.destroy()

    def getButton(self):
        return self.button

    def getCurrentState(self):
        return self.states.index(self.currentState)

    def switchState(self):
        newState = self.currentState + 1
        if newState == len(self.states):
            newState = self.currentState - 1
        self.switchStateTo(newState)
        self.currentState = newState

    def switchStateTo(self, state: int):
        if state != self.currentState:
            self.button.configure(text=str(self.states[state]))


# Repräsentiert das Settings Menu im Startmenü
class Settings(Screen):

    def __init__(self):
        super().__init__("SettingsScreen")

    # erstellt die Buttons für das Einstellungs Menu
    def create(self):
        global options

        if buttonDontExist(0):
            backButton = Button(gui, width=30, height=6, bg=buttonColor)
            backButton["text"] = "Zurück zum Startmenü"
            backButton["command"] = lambda: self.switchTo(StartScreen())
            backButton.place(x=890, y=650)
            options.append(backButton)
        else:
            backButton = Button(gui, width=30, height=6, bg=buttonColor)
            backButton["text"] = "Zurück zum Startmenü"
            backButton["command"] = lambda: self.switchTo(StartScreen())
            backButton.place(x=890, y=650)
            options[0] = backButton

        if buttonDontExist(1):
            controlOption: SwitchStateButton = SwitchStateButton("Control Buttons", 15, 15, 600, 650, 30, 6, None,
                                                                 [False, True],
                                                                 False).create()
            options.append(controlOption)
        else:
            options[1].create()

        if buttonDontExist(2):
            controlOption: SwitchStateButton = SwitchStateButton(
                "Spielfeldrand", 15, 20, 890 + 190 + (30 * 3.6), 650, 30, 6,
                None, [True, False], True).create()
            options.append(controlOption)
        else:
            options[2].create()

        if buttonDontExist(3):
            textField: SyncedTextField = SyncedTextField(7, 890, 200, 20, ('Purisa', 15), defaultSpielfeldFarbe,
                                                         "Ändere die Farbe des Spielfelds", 50).create()

            options.append(textField)
        else:
            options[3].show()

        if buttonDontExist(4):
            textField: SyncedTextField = SyncedTextField(2, 890, 300, 20, ('Purisa', 15), defaultHorizontalFeldNumber,
                                                         "Horizontal Spielfeldgröße", 50).create()

            options.append(textField)
        else:
            options[4].show()

        if buttonDontExist(5):
            textField: SyncedTextField = SyncedTextField(2, 890, 400, 20, ('Purisa', 15), defaultVerticalFeldNumber,
                                                         "Vertikale Spielfeldgröße", 50).create()

            options.append(textField)
        else:
            options[5].show()

        if buttonDontExist(6):
            textField: SyncedTextField = SyncedTextField(2, 890, 500, 20, ('Purisa', 15), connect,
                                                         "Gewinnüberprüfungsgröße", 50).create()

            options.append(textField)
        else:
            options[6].show()

    # löscht die Buttons vom Einstellungs Menu
    def delete(self):
        print("Deleted:", self.name)
        for index, button in enumerate(options):
            button.destroy()


class WinScreen(Screen):
    def __init__(self, winner: Player):
        super().__init__("WinOverlay")
        self.winner = winner
        self.rectangle = None
        self.text = None
        self.text2 = None
        self.text3 = None
        self.restartButton = None
        self.backButton = None

    def create(self):
        global shouldPlaceChip

        if self.winner.playerNumber == 0:
            print("Patt - Das Spielfeld ist voll!")

            shouldPlaceChip = False

            self.rectangle = background.create_rectangle(840, 450, 1080, 800, fill="#3A3A3A", outline='#6F6F6F')
            # self.text = background.create_text(960, 500, text="Der Spieler", fill="black", font=("Purisa", 20))
            self.text2 = background.create_text(960, 535, text="Patt", fill="black",
                                                font=("Purisa", 20, "bold"))
            # self.text3 = background.create_text(960, 565, text="hat gewonnen", fill="black", font=("Purisa", 20))

            self.clearOverlay("InGameOverlay")

            self.restartButton = Button(gui, width=25, height=4, bg=buttonColor)
            self.restartButton["text"] = "Neustart"
            self.restartButton["command"] = lambda: self.restart()
            self.restartButton.place(x=867, y=610)

            self.backButton = Button(gui, width=25, height=4, bg=buttonColor)
            self.backButton["text"] = "Zurück zum Startmenü"
            self.backButton["command"] = lambda: currentScreen.switchTo(StartScreen())
            self.backButton.place(x=867, y=690)
        else:
            print("Der Spieler: " + self.winner.getName() + " hat gewonnen")

            shouldPlaceChip = False

            self.rectangle = background.create_rectangle(840, 450, 1080, 800, fill="#3A3A3A", outline='#6F6F6F')
            self.text = background.create_text(960, 500, text="Der Spieler", fill="black", font=("Purisa", 20))
            self.text2 = background.create_text(960, 535, text=self.winner.getName(), fill=self.winner.getPlayerColor(),
                                                font=("Purisa", 20, "bold"))
            self.text3 = background.create_text(960, 565, text="hat gewonnen", fill="black", font=("Purisa", 20))

            self.clearOverlay("InGameOverlay")

            self.restartButton = Button(gui, width=25, height=4, bg=buttonColor)
            self.restartButton["text"] = "Neustart"
            self.restartButton["command"] = lambda: self.restart()
            self.restartButton.place(x=867, y=610)

            self.backButton = Button(gui, width=25, height=4, bg=buttonColor)
            self.backButton["text"] = "Zurück zum Startmenü"
            self.backButton["command"] = lambda: currentScreen.switchTo(StartScreen())
            self.backButton.place(x=867, y=690)

    def restart(self):
        global shouldPlaceChip
        self.delete()
        shouldPlaceChip = True
        self.addOverlayScreen(InGameMenu())
        self.clearOverlay("WinScreen")
        restartGame()

    def delete(self):
        global background

        background.delete(self.rectangle)
        background.delete(self.text)
        background.delete(self.text2)
        background.delete(self.text3)
        self.restartButton.destroy()
        self.backButton.destroy()
        currentScreen.overlays.remove(self)


# Repräsentiert das in Game Menu
class InGameMenu(Screen):
    def __init__(self):
        super().__init__("InGameOverlay")
        # Button Variablen, um einzelne Buttons zu haben
        self.menuButton = None
        self.backToSMButton = None
        self.restartButton = None
        # Liste zum Speichern aller Buttons
        self.buttonList = []
        # Überprüfung, ob das Menu offen ist
        self.statusOpen = False

    # erstellt nur den Menu Button
    def create(self):
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
            self.backToSMButton["command"] = lambda: currentScreen.switchTo(StartScreen())
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
    def delete(self):
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
class PlayerListBar(Screen):

    # erstellt die obere Leiste mit Spielernamen
    def __init__(self):
        super().__init__("PlayerListBarOverlay")
        self.Bindestrich = None
        self.Rechteck = None
        self.Spieler1 = None
        self.Spieler2 = None

    def create(self):
        global background
        global spielerAnDerReihe
        global otherPlayerColor

        self.Rechteck = background.create_rectangle(0, 0, 1920, 60, fill=playerListBarColor,
                                                    outline=playerListBarOutlineColor)
        self.Bindestrich = background.create_text(960, 30, text='-', fill='#000000', font=('Purisa', 22))

        if spielerAnDerReihe.getPlayerNumber() == 1:
            self.Spieler1 = background.create_text(820, 30, text=player1.name, fill=player1.getPlayerColor(),
                                                   font=('Purisa', 18, 'bold'))
        else:
            self.Spieler1 = background.create_text(820, 30, text=player1.name, fill=otherPlayerColor,
                                                   font=('Purisa', 18))

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

        checkComp()

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
                spielerAnDerReihe = player1
            elif playerNumber == 2:
                spielerAnDerReihe = player2
            else:
                print('Error!!! SpielerAnDerReihe:', spielerAnDerReihe)

            if playerNumber == 1:
                background.itemconfig(self.Spieler1, fill=player1.getPlayerColor(), font=('Purisa', 18, 'bold'))
                background.itemconfig(self.Spieler2, fill=otherPlayerColor, font=('Purisa', 18))
            elif playerNumber == 2:
                background.itemconfig(self.Spieler1, fill=otherPlayerColor, font=('Purisa', 18))
                background.itemconfig(self.Spieler2, fill=player2.getPlayerColor(), font=('Purisa', 18, 'bold'))

    def delete(self):
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
        self.farbe = getTextfieldOption(3, defaultSpielfeldFarbe)

        feld_y = 100 + size * self.horizontal
        feld_x = 375 + size * self.vertikal

        if getButtonState(2, True):
            self.feld = background.create_rectangle(feld_x, feld_y, feld_x + size,
                                                    feld_y + size, fill=self.farbe, outline=self.farbe)
        else:
            self.feld = background.create_rectangle(feld_x, feld_y, feld_x + size,
                                                    feld_y + size, fill=self.farbe)

        if not getButtonState(1, False):
            # gibt dem Feld die Funktion bei einem Linksklick, den Chip mit Physics hinzusetzten
            background.tag_bind(self.feld, '<Button-1>', lambda a: handlePlayerChip(self.vertikal))

        self.placeChip(backgroundColor, 0)

    def setColor(self, color):
        global background
        self.farbe = color
        if getButtonState(2, True):
            background.itemconfig(self.feld, fill=color, outline=color)
        else:
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

        if not getButtonState(1, False):
            # gibt dem Chip die Funktion bei einem Linksklick, den Chip mit Physics hinzusetzten
            background.tag_bind(self.playerChip, '<Button-1>', lambda a: handlePlayerChip(self.vertikal))

    # löscht Spieler Chip, wenn es nicht ein leeres Feld
    def deleteChip(self):
        global background
        if self.playerChip is not None:
            background.delete(self.playerChip)


# Feld Größe Einstellung
size = 130

# Überprüfungsgröße
connect = 4

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
defaultHorizontalFeldNumber = 7
defaultVerticalFeldNumber = 8

# default Spieler Name
playerName1 = 'Spieler 1'
playerName2 = 'Spieler 2'

# Spielerkreise im Startbildschirm
canvas_width = 200
canvas_height = 40

# default Spieler Farben
defaultColorOfPlayer1 = 'red'
defaultColorOfPlayer2 = 'yellow'

colorOfPlayer1 = 'red'
colorOfPlayer2 = 'yellow'

# Spieler Variablen
player1 = Player(colorOfPlayer1, playerName1, 1)
player2 = Player(colorOfPlayer2, playerName2, 2)

# Spieler an der Reihe
spielerAnDerReihe = player1

# Runden Nummer
roundNumber = 0

# kann das Setzen von Chips verhindern
shouldPlaceChip = True

# Cancels the next Round
win = False

# Erstellung des haupt Canvas
background = Canvas(width=gui.winfo_screenwidth(), height=gui.winfo_screenheight(), bg=backgroundColor)
background.pack(expand=YES, fill=BOTH)


# Hilfsfunktion um einen Spieler Chip auf dem Bildschirm darzustellen
def createPlayerChip(canvas, x, y, chipSize, color):
    chip = canvas.create_oval(x, y, x + chipSize, y + chipSize, fill=color)
    return chip


currentScreen = StartScreen().create()

# Liste aller interaktiven Schaltfläschen im Settings Menu
options: list = []

# Liste enthält weitere Listen → diese Listen repräsentieren eine vertikale Linie von den Vierecken
spielfeld: list = []

# Control Button Liste, um die Buttons später zu löschen
buttons = []


def buttonDontExist(number: int):
    for index, button in enumerate(options):
        if index == number:
            return False
    return True


def getButtonState(number: int, defaultReturn):
    for index, button in enumerate(options):
        button: SwitchStateButton
        if index == number:
            return button.getCurrentState()
    return defaultReturn


def getTextfieldOption(number: int, defaultReturn):
    for index, button in enumerate(options):
        button: SyncedTextField
        if index == number:
            return button.getCurrentOption()
    return defaultReturn


def playerNumberToPlayer(playerNumber: int):
    if playerNumber == 1:
        return player1
    elif playerNumber == 2:
        return player2
    else:
        return None


# startet eine neue Runde
def nextRound():
    global roundNumber
    global spielerAnDerReihe
    global win
    if not win:
        roundNumber = roundNumber + 1
        print('Round Number:', roundNumber)
        overlay = currentScreen.getOverlay("PlayerListBarOverlay")
        if overlay is not None:
            overlay: PlayerListBar
            overlay.tauscheSpielerAnDerReihe()
            if isSpielfeldVoll():
                currentScreen.addOverlayScreen(WinScreen(Player("", "", 0)))


# ToDo: einen loop machen
def checkComp():
    if spielerAnDerReihe.computerGegner:
        gui.after(1000, lambda: handleComp())


def handleComp():
    row = random.randint(0, int(getTextfieldOption(5, defaultVerticalFeldNumber)) - 1)
    feld: VierGewinntFeld = getPositionForChip(row)
    if feld is not None:
        if shouldPlaceChip:
            feld.placeChip(spielerAnDerReihe.getPlayerColor(), spielerAnDerReihe.getPlayerNumber())
            winCheck(spielerAnDerReihe.getPlayerNumber())
            nextRound()


# erstellt die Buttons, die in der Reihe einen neuen Chip hineinsetzten können
def createControlButtons():
    if getButtonState(1, False):
        for y in range(1, int(getTextfieldOption(5, defaultVerticalFeldNumber))):
            createControlButton(y)


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
    feld: VierGewinntFeld = getPositionForChip(row)
    if feld is not None:
        if shouldPlaceChip:
            feld.placeChip(spielerAnDerReihe.getPlayerColor(), spielerAnDerReihe.getPlayerNumber())
            winCheck(spielerAnDerReihe.getPlayerNumber())
            nextRound()


# berechnet die richtige Stelle im Spielfeld für den Spielerchip
def getPositionForChip(row):
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


def isSpielfeldVoll():
    fullRows = []

    for h, listOfObjects in enumerate(spielfeld):
        row = []
        for v, feld in enumerate(listOfObjects):
            if not feld.isEmpty():
                row.append(feld)

        if len(row) == int(getTextfieldOption(4, defaultHorizontalFeldNumber)) - 1:
            fullRows.append(row)

    if len(fullRows) == int(getTextfieldOption(5, defaultVerticalFeldNumber)) - 1:
        return True
    else:
        return False


def restartGame():
    global spielerAnDerReihe
    global win

    overlay = currentScreen.getOverlay("PlayerListBarOverlay")
    if overlay is not None:
        overlay: PlayerListBar
        overlay.setSpielerAnDerReihe(1)

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
                viereck.setColor(getTextfieldOption(3, defaultSpielfeldFarbe))
                viereck.placeChip(backgroundColor, 0)


# allgemeine Gewinn Überprüfung
def winCheck(playerNumber: int):
    global win
    for h in range(int(getTextfieldOption(5, defaultVerticalFeldNumber))):
        for v in range(int(getTextfieldOption(4, defaultHorizontalFeldNumber))):
            if (checkSingleLineClear(h, v, 1, playerNumber) == True
                    or checkSingleLineClear(h, v, 2, playerNumber) == True
                    or checkSingleLineClear(h, v, 3, playerNumber) == True
                    or checkSingleLineClear(h, v, 4, playerNumber)):
                win = True


# Überprüft, ob jemand in einer Linie gewonnen hat
def checkSingleLineClear(horizontaleNummer: int, vertikaleNummer: int, operationType: int, playerNumber: int):
    # speichert mehrere Status, der jeweiligen Felder des operationTypes
    firstCheckList: list[VierGewinntFeld] = []
    # speichert die Felder ein, die von einem bestimmten Spieler besetzt wurden
    feldWinList: list[VierGewinntFeld] = []

    if operationType == 1:
        for index in range(int(getTextfieldOption(6, connect))):
            firstCheckList.append(checkSingleFieldWin(horizontaleNummer, vertikaleNummer + index, playerNumber))
    elif operationType == 2:
        for index in range(int(getTextfieldOption(6, connect))):
            firstCheckList.append(checkSingleFieldWin(horizontaleNummer + index, vertikaleNummer, playerNumber))
    elif operationType == 3:
        for index in range(int(getTextfieldOption(6, connect))):
            firstCheckList.append(
                checkSingleFieldWin(horizontaleNummer + index, vertikaleNummer + index, playerNumber))
    elif operationType == 4:
        for index in range(int(getTextfieldOption(6, connect))):
            firstCheckList.append(
                checkSingleFieldWin(horizontaleNummer - index, vertikaleNummer + index, playerNumber))

    # alle Felder die vom jeweiligem Spieler besetzt sind, in die erste Liste hinzufügen
    for index, feld in enumerate(firstCheckList):
        if feld is not None:
            feldWinList.append(feld)

    # Überprüfung, ob die größe der ersten Checkliste genau der finalen Checkliste entspricht
    if len(feldWinList) == len(firstCheckList):
        currentScreen.addOverlayScreen(WinScreen(playerNumberToPlayer(playerNumber)))
        for index, feld in enumerate(feldWinList):
            feld.setColor('green')
        return True
    else:
        return False


# Wenn der Spieler dieses Feld besetzt hat, return diese Funktion das Feld - andererseits wird None returned
def checkSingleFieldWin(horizontaleNummer: int, vertikaleNummer: int, playerNumber: int):
    feld = getFeld(horizontaleNummer, vertikaleNummer)

    if feld is not None:
        if feld.getPlayerNumber() == playerNumber:
            return feld
        else:
            return None
    else:
        return None


def compGegner():
    spielerAnDerReihe.computerGegner = True
    checkComp()


gui.mainloop()
