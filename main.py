from tkinter import *

gui = Tk()
w, h = gui.winfo_screenwidth(), gui.winfo_screenheight()
gui.geometry("%dx%d+0+0" % (w, h))
gui.title('VierGewinnt')


class VierGewinntFeld:
    # ToDo: Add a Canvas for every Feld

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y




class Player:
    playerField = VierGewinntFeld(0, 0)
    playerColor = ""
    name = ""

    def __init__(self, playerColor, name):
        self.playerColor = playerColor
        self.name = name

    def move(self, x, y):
        self.playerField.move(x, y)



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
but1.place(x=275, y=300)

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


spielfeld = [[], [], [], [], [], [], []]


def setupPlayerListBar():
    # ToDo: füge die Spielerleiste hinzu für das Spiel
    print("This is work in progress")


def setupSpielFeld():
    # ToDo: implement this
    print("Setting Up Spielfeld!")


gui.mainloop()





#neues#########################################################################



from tkinter import *


gui = Tk()
gui.geometry('750x500')
gui.title('VierGewinnt')
endbildschirm='aus'


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



#Kreise im Startgame Bildschirm
canvas_width = 200
canvas_height = 40

myCanvas = Canvas(width=canvas_width, height=canvas_height, bg='grey')
myCanvas.pack(expand=YES, fill=BOTH)
oval1 = myCanvas.create_oval(100, 50, 160, 110, fill="yellow")
oval2 = myCanvas.create_oval(100, 150, 160, 210, fill="red")






#Button und Textfeld code(Startbildschirm)

but1 = Button(gui, width=20, height=6, bg='grey')
but1["text"] = "Start"
but1["command"] = lambda:startGame()
but1.place(x=275, y=300)



tf_player1 = Entry(gui, bg='grey')
tf_player1.place(x=175, y=70)

tf_player2 = Entry(gui, bg='grey')

tf_player2.place(x=175, y=170)

player1 = Player("yellow", tf_player1.get())
player2 = Player("red", tf_player2.get())



def startGame():

    myCanvas.delete(oval1)
    myCanvas.delete(oval2)
    tf_player1.destroy()
    tf_player2.destroy()
    but1.destroy()

#Button für neue Runde
while endbildschirm=='an':

    but2 = Button(gui, width=20, height=6, bg='grey')
    but2["text"] = "Start"
    but2["command"] = lambda:newGame()
    but2.place(x=275, y=300)
    endbildschirm='aus'

    def newGame():
        

        oval1 = myCanvas.create_oval(100, 50, 160, 110, fill="yellow")
        oval2 = myCanvas.create_oval(100, 150, 160, 210, fill="red")
        myCanvas.pack()

        but1 = Button(gui, width=20, height=6, bg='grey')
        but1["text"] = "Start"
        but1["command"] = lambda:startGame()
        but1.place(x=275, y=300)





#hallo








player1 = Player("yellow", tf_player1.get())
player2 = Player("red", tf_player2.get())








gui.mainloop()
