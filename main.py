from tkinter import *


gui = Tk()
gui.geometry('750x500')
gui.title('VierGewinnt')



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














player1 = Player("yellow", tf_player1.get())
player2 = Player("red", tf_player2.get())








gui.mainloop()
