from tkinter import *
from tkinter import ttk
import random

def aus1(a):
    if auswahll.get() == "Spieler":
        photo1.config(image=mensch_img)
    else:
        photo1.config(image=ki_img)
def aus2(a):
    if auswahl2.get() == "Spieler":
        photo2.config(image=mensch_img)
    else:
        photo2.config(image=ki_img)

def PvsP():
    PvP = Toplevel(root)
    PvP.title("Tic Tac Toe gegen den Computer!")
    global X_img
    global O_img
    global blank
    global a

    X_img = PhotoImage(file="Images/X.png")
    O_img = PhotoImage(file="Images/O.png")
    blank = PhotoImage(file="Images/blank.png")
    T = Label(PvP, text="TicTacToe gegen jemand anderes!", font='helvetica 12')
    neueRunde = Button(PvP, text="neue Runde", bg="lightgray", command=lambda: PvP.destroy(), font='helvetica 12')
    exit = Button(PvP, text="Exit", bg="lightgray", command=lambda: root.destroy(), font='helvetica 12')
    grid0 = Button(PvP, image=blank, cursor="X_cursor", command=lambda: buttoins(0))
    grid1 = Button(PvP, image=blank, cursor="X_cursor", command=lambda: buttoins(1))
    grid2 = Button(PvP, image=blank, cursor="X_cursor", command=lambda: buttoins(2))
    grid3 = Button(PvP, image=blank, cursor="X_cursor", command=lambda: buttoins(3))
    grid4 = Button(PvP, image=blank, cursor="X_cursor", command=lambda: buttoins(4))
    grid5 = Button(PvP, image=blank, cursor="X_cursor", command=lambda: buttoins(5))
    grid6 = Button(PvP, image=blank, cursor="X_cursor", command=lambda: buttoins(6))
    grid7 = Button(PvP, image=blank, cursor="X_cursor", command=lambda: buttoins(7))
    grid8 = Button(PvP, image=blank, cursor="X_cursor", command=lambda: buttoins(8))

    T.grid(row=0, column=1)
    neueRunde.grid(row=0, column=0)
    exit.grid(row=0, column=2)
    grid0.grid(row=1, column=0)
    grid1.grid(row=1, column=1)
    grid2.grid(row=1, column=2)
    grid3.grid(row=2, column=0)
    grid4.grid(row=2, column=1)
    grid5.grid(row=2, column=2)
    grid6.grid(row=3, column=0)
    grid7.grid(row=3, column=1)
    grid8.grid(row=3, column=2)
    takeBtn1 = []
    takeBtn2 = []
    a = 2

    def disable():
        btns = {0: grid0, 1: grid1, 2: grid2, 3: grid3, 4: grid4, 5: grid5, 6: grid6, 7: grid7, 8: grid8}
        for i in btns:
            for x in range(0, 10):
                x = btns[i]
                x.config(state=DISABLED)

    def buttoins(btn):
        global a
        # Player 1
        btns = {0: grid0, 1: grid1, 2: grid2, 3: grid3, 4: grid4, 5: grid5, 6: grid6, 7: grid7, 8: grid8}
        if a % 2 == 0:
            x = btns[btn]
            x.config(image=X_img)
            x.config(state=DISABLED)
            takeBtn1.append(btn)
            for integer in ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]):
                if integer[0] in takeBtn1 and integer[1] in takeBtn1 and integer[2] in takeBtn1:
                    T.config(text="Spieler 1, du hast Gewonnen!", fg="red", font='helvetica 14')
                    disable()
                    a += 1
        else:
            x = btns[btn]
            x.config(image=O_img)
            x.config(state=DISABLED)
            takeBtn2.append(btn)
            for integer in ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]):
                if integer[0] in takeBtn2 and integer[1] in takeBtn2 and integer[2] in takeBtn2:
                    T.config(text="Spieler 2, du hast Gewonnen!", fg="red", font='helvetica 14')
                    disable()
                    a += 1
        a += 1
        if a == 11:
            T.config(text="Das Spielfeld ist voll!", fg="red", font='helvetica 14')

def PvsC():
    PvC = Toplevel(root)
    PvC.title("Tic Tac Toe gegen den Computer!")
    global X_img
    global O_img
    global blank
    global a

    X_img = PhotoImage(file="Images/X.png")
    O_img = PhotoImage(file="Images/O.png")
    blank = PhotoImage(file="Images/blank.png")
    T = Label(PvC, text="TicTacToe gegen den Computer!", font='helvetica 12')
    neueRunde = Button(PvC, text="neue Runde", bg="lightgray", command=lambda: PvC.destroy(), font='helvetica 12')
    exit = Button(PvC, text="Exit", bg="lightgray", command=lambda: root.destroy(), font='helvetica 12')
    grid0 = Button(PvC, image=blank, cursor="X_cursor", command=lambda: button_click(0))
    grid1 = Button(PvC, image=blank, cursor="X_cursor", command=lambda: button_click(1))
    grid2 = Button(PvC, image=blank, cursor="X_cursor", command=lambda: button_click(2))
    grid3 = Button(PvC, image=blank, cursor="X_cursor", command=lambda: button_click(3))
    grid4 = Button(PvC, image=blank, cursor="X_cursor", command=lambda: button_click(4))
    grid5 = Button(PvC, image=blank, cursor="X_cursor", command=lambda: button_click(5))
    grid6 = Button(PvC, image=blank, cursor="X_cursor", command=lambda: button_click(6))
    grid7 = Button(PvC, image=blank, cursor="X_cursor", command=lambda: button_click(7))
    grid8 = Button(PvC, image=blank, cursor="X_cursor", command=lambda: button_click(8))

    T.grid(row=0, column=1)
    neueRunde.grid(row=0, column=0)
    exit.grid(row=0, column=2)
    grid0.grid(row=1, column=0)
    grid1.grid(row=1, column=1)
    grid2.grid(row=1, column=2)
    grid3.grid(row=2, column=0)
    grid4.grid(row=2, column=1)
    grid5.grid(row=2, column=2)
    grid6.grid(row=3, column=0)
    grid7.grid(row=3, column=1)
    grid8.grid(row=3, column=2)

    freeBtn = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    grid = ["", "", "", "", "", "", "", "", ""]
    takeBtn = []
    te = False

    def disable():
        btns = {0: grid0, 1: grid1, 2: grid2, 3: grid3, 4: grid4, 5: grid5, 6: grid6, 7: grid7, 8: grid8}
        for i in btns:
            for x in range(0, 10):
                x = btns[i]
                x.config(state=DISABLED)

    def button_click(btn):
        te = False
        # Player 1
        e = 0
        freeBtn.remove(btn)
        btns = {0: grid0, 1: grid1, 2: grid2, 3: grid3, 4: grid4, 5: grid5, 6: grid6, 7: grid7, 8: grid8}
        x = btns[btn]
        x.config(image=X_img)
        x.config(state=DISABLED)
        takeBtn.append(btn)
        grid[btn] = "X"
        for integer in ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]):
            if integer[0] in takeBtn and integer[1] in takeBtn and integer[2] in takeBtn:
                T.config(text="Du hast gegen den Computer gewonnen!", fg="red", font='helvetica 14')
                disable()
            else:
                e += 1
        if not "" in grid:
            T.config(text="Das Spielfeld ist voll und keiner hat gewonnen!", fg="red", font='helvetica 14')
        if e == 8:
            for p in range(1):
                for i in freeBtn:
                    gridCopy = grid[:]
                    gridCopy[i] = "O"
                    if gridCopy[0] == gridCopy[1] == gridCopy[2] == "O":
                        grid0.config(image=O_img)
                        grid1.config(image=O_img)
                        grid2.config(image=O_img)
                        disable()
                        T.config(text="Der Computer hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[3] == gridCopy[4] == gridCopy[5] == "O":
                        grid3.config(image=O_img)
                        grid4.config(image=O_img)
                        grid5.config(image=O_img)
                        disable()
                        T.config(text="Der Computer hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[6] == gridCopy[7] == gridCopy[8] == "O":
                        grid6.config(image=O_img)
                        grid7.config(image=O_img)
                        grid8.config(image=O_img)
                        disable()
                        T.config(text="Der Computer hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[0] == gridCopy[4] == gridCopy[8] == "O":
                        grid0.config(image=O_img)
                        grid4.config(image=O_img)
                        grid8.config(image=O_img)
                        disable()
                        T.config(text="Der Computer hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[2] == gridCopy[4] == gridCopy[6] == "O":
                        grid2.config(image=O_img)
                        grid4.config(image=O_img)
                        grid6.config(image=O_img)
                        disable()
                        T.config(text="Der Computer hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[0] == gridCopy[3] == gridCopy[6] == "O":
                        grid0.config(image=O_img)
                        grid3.config(image=O_img)
                        grid6.config(image=O_img)
                        disable()
                        T.config(text="Der Computer hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[1] == gridCopy[4] == gridCopy[7] == "O":
                        grid1.config(image=O_img)
                        grid4.config(image=O_img)
                        grid7.config(image=O_img)
                        disable()
                        T.config(text="Der Computer hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[2] == gridCopy[5] == gridCopy[8] == "O":
                        grid2.config(image=O_img)
                        grid5.config(image=O_img)
                        grid8.config(image=O_img)
                        disable()
                        T.config(text="Der Computer hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                for i in freeBtn:
                    gridCopy = grid[:]
                    gridCopy[i] = "X"
                    if gridCopy[0] == gridCopy[1] == gridCopy[2] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[3] == gridCopy[4] == gridCopy[5] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[6] == gridCopy[7] == gridCopy[8] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[0] == gridCopy[4] == gridCopy[8] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[2] == gridCopy[4] == gridCopy[6] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[0] == gridCopy[3] == gridCopy[6] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[1] == gridCopy[4] == gridCopy[7] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[2] == gridCopy[5] == gridCopy[8] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                if te:
                    te = False
                    break
                else:
                    freieEcken = []
                    freieFelder = []
                    for i in freeBtn:
                        if i in [0, 2, 6, 8]:
                            freieEcken.append(i)
                    if len(freieEcken) > 0:
                        a = random.choice(freieEcken)
                        x = btns[a]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        grid[a] = "O"
                        freeBtn.remove(a)
                        break
                    if 4 in freeBtn:
                        grid[4] = "O"
                        grid5.config(image=O_img)
                        grid5.config(state=DISABLED)
                        freeBtn.remove(4)
                        break
                    for i in freeBtn:
                        if i in [1, 3, 5, 7]:
                            freieFelder.append(i)
                    if len(freieFelder) > 0:
                        a = random.choice(freieFelder)
                        grid[a] = "O"
                        x = btns[a]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        freeBtn.remove(a)
def CvsC():
    CvC = Toplevel(root)
    CvC.title("Tic Tac Toe Computer gegen Computer!")
    global X_img
    global O_img
    global blank
    global a
    global freeBtn
    global grid
    global te
    global t

    X_img = PhotoImage(file="Images/X.png")
    O_img = PhotoImage(file="Images/O.png")
    blank = PhotoImage(file="Images/blank.png")
    T = Label(CvC, text="TicTacToe Computer gegen Computer!", font='helvetica 12')
    neueRunde = Button(CvC, text="neue Runde", bg="lightgray", command=lambda: CvC.destroy(), font='helvetica 12')
    exit = Button(CvC, text="Exit", bg="lightgray", command=lambda: root.destroy(), font='helvetica 12')
    grid0 = Button(CvC, image=blank, cursor="X_cursor")
    grid1 = Button(CvC, image=blank, cursor="X_cursor")
    grid2 = Button(CvC, image=blank, cursor="X_cursor")
    grid3 = Button(CvC, image=blank, cursor="X_cursor")
    grid4 = Button(CvC, image=blank, cursor="X_cursor")
    grid5 = Button(CvC, image=blank, cursor="X_cursor")
    grid6 = Button(CvC, image=blank, cursor="X_cursor")
    grid7 = Button(CvC, image=blank, cursor="X_cursor")
    grid8 = Button(CvC, image=blank, cursor="X_cursor")
    P = Button(CvC, text="Start", command=lambda: button_click(), font="helvetica 20", bg="grey")
    var = IntVar(value=1)
    Ü = Checkbutton(CvC, text="mit Delay", font="helvetica 18", bg="lightgrey", onvalue=1, offvalue=0, variable=var)

    T.grid(row=0, column=1)
    neueRunde.grid(row=0, column=0)
    exit.grid(row=0, column=2)
    grid0.grid(row=1, column=0)
    grid1.grid(row=1, column=1)
    grid2.grid(row=1, column=2)
    grid3.grid(row=2, column=0)
    grid4.grid(row=2, column=1)
    grid5.grid(row=2, column=2)
    grid6.grid(row=3, column=0)
    grid7.grid(row=3, column=1)
    grid8.grid(row=3, column=2)
    P.grid(row=4, column=1)
    Ü.grid(row=4, column=0)
    freeBtn = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    grid = ["", "", "", "", "", "", "", "", ""]
    te = False
    t = 0

    def button_click():
        global t
        btns = {0: grid0, 1: grid1, 2: grid2, 3: grid3, 4: grid4, 5: grid5, 6: grid6, 7: grid7, 8: grid8}
        for i in btns:
            for x in range(0, 10):
                x = btns[i]
                x.config(state=DISABLED)
        if var.get() == 1:
            t = 1500
        Computer_1()

    def Computer_1():
        global te
        btns = {0: grid0, 1: grid1, 2: grid2, 3: grid3, 4: grid4, 5: grid5, 6: grid6, 7: grid7, 8: grid8}
        if not "" in grid:
            T.config(text="Das Spielfeld ist voll!", fg="red", font='helvetica 14')
        else:
            for ü in range(1):
                for i in freeBtn:
                    gridCopy = grid[:]
                    gridCopy[i] = "X"
                    if gridCopy[0] == gridCopy[1] == gridCopy[2] == "X":
                        grid0.config(image=X_img)
                        grid1.config(image=X_img)
                        grid2.config(image=X_img)
                        T.config(text="Der Computer 1 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[3] == gridCopy[4] == gridCopy[5] == "X":
                        grid3.config(image=X_img)
                        grid4.config(image=X_img)
                        grid5.config(image=X_img)
                        T.config(text="Der Computer 1 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[6] == gridCopy[7] == gridCopy[8] == "X":
                        grid6.config(image=X_img)
                        grid7.config(image=X_img)
                        grid8.config(image=X_img)
                        T.config(text="Der Computer 1 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[0] == gridCopy[4] == gridCopy[8] == "X":
                        grid0.config(image=X_img)
                        grid4.config(image=X_img)
                        grid8.config(image=X_img)
                        T.config(text="Der Computer 1 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[2] == gridCopy[4] == gridCopy[6] == "X":
                        grid2.config(image=X_img)
                        grid4.config(image=X_img)
                        grid6.config(image=X_img)
                        T.config(text="Der Computer 1 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[0] == gridCopy[3] == gridCopy[6] == "X":
                        grid0.config(image=X_img)
                        grid3.config(image=X_img)
                        grid6.config(image=X_img)
                        T.config(text="Der Computer 1 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[1] == gridCopy[4] == gridCopy[7] == "X":
                        grid1.config(image=X_img)
                        grid4.config(image=X_img)
                        grid7.config(image=X_img)
                        T.config(text="Der Computer 1 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[2] == gridCopy[5] == gridCopy[8] == "X":
                        grid2.config(image=X_img)
                        grid5.config(image=X_img)
                        grid8.config(image=X_img)
                        T.config(text="Der Computer 1 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                for i in freeBtn:
                    gridCopy = grid[:]
                    gridCopy[i] = "O"
                    if gridCopy[0] == gridCopy[1] == gridCopy[2] == "O":
                        x = btns[i]
                        x.config(image=X_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "X"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[3] == gridCopy[4] == gridCopy[5] == "O":
                        x = btns[i]
                        x.config(image=X_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "X"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[6] == gridCopy[7] == gridCopy[8] == "O":
                        x = btns[i]
                        x.config(image=X_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "X"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[0] == gridCopy[4] == gridCopy[8] == "O":
                        x = btns[i]
                        x.config(image=X_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "X"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[2] == gridCopy[4] == gridCopy[6] == "O":
                        x = btns[i]
                        x.config(image=X_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "X"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[0] == gridCopy[3] == gridCopy[6] == "O":
                        x = btns[i]
                        x.config(image=X_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "X"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[1] == gridCopy[4] == gridCopy[7] == "O":
                        x = btns[i]
                        x.config(image=X_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "X"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[2] == gridCopy[5] == gridCopy[8] == "O":
                        x = btns[i]
                        x.config(image=X_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "X"
                        freeBtn.remove(i)
                        break
                if te:
                    te = False
                    Computer_2()
                    break
                else:
                    freieEcken = []
                    freieFelder = []
                    for i in freeBtn:
                        if i in [0, 2, 6, 8]:
                            freieEcken.append(i)
                    if len(freieEcken) > 0:
                        a = random.choice(freieEcken)
                        x = btns[a]
                        x.config(image=X_img)
                        x.config(state=DISABLED)
                        grid[a] = "X"
                        freeBtn.remove(a)
                        break
                    if 4 in freeBtn:
                        grid[4] = "X"
                        grid5.config(image=X_img)
                        grid5.config(state=DISABLED)
                        freeBtn.remove(4)
                        break
                    for i in freeBtn:
                        if i in [1, 3, 5, 7]:
                            freieFelder.append(i)
                            break
                    if len(freieFelder) > 0:
                        a = random.choice(freieFelder)
                        grid[a] = "X"
                        x = btns[a]
                        x.config(image=X_img)
                        x.config(state=DISABLED)
                        freeBtn.remove(a)
                        break
            root.after(t, Computer_2)

    def Computer_2():
        global te
        btns = {0: grid0, 1: grid1, 2: grid2, 3: grid3, 4: grid4, 5: grid5, 6: grid6, 7: grid7, 8: grid8}
        if not "" in grid:
            T.config(text="Das Spielfeld ist voll!", fg="red", font='helvetica 14')
        else:
            for int in range(1):
                for i in freeBtn:
                    gridCopy = grid[:]
                    gridCopy[i] = "O"
                    if gridCopy[0] == gridCopy[1] == gridCopy[2] == "O":
                        grid0.config(image=O_img)
                        grid1.config(image=O_img)
                        grid2.config(image=O_img)
                        T.config(text="Der Computer 2 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[3] == gridCopy[4] == gridCopy[5] == "O":
                        grid3.config(image=O_img)
                        grid4.config(image=O_img)
                        grid5.config(image=O_img)
                        T.config(text="Der Computer 2 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[6] == gridCopy[7] == gridCopy[8] == "O":
                        grid6.config(image=O_img)
                        grid7.config(image=O_img)
                        grid8.config(image=O_img)
                        T.config(text="Der Computer 2 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[0] == gridCopy[4] == gridCopy[8] == "O":
                        grid0.config(image=O_img)
                        grid4.config(image=O_img)
                        grid8.config(image=O_img)
                        T.config(text="Der Computer 2 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[2] == gridCopy[4] == gridCopy[6] == "O":
                        grid2.config(image=O_img)
                        grid4.config(image=O_img)
                        grid6.config(image=O_img)
                        T.config(text="Der Computer 2 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[0] == gridCopy[3] == gridCopy[6] == "O":
                        grid0.config(image=O_img)
                        grid3.config(image=O_img)
                        grid6.config(image=O_img)
                        T.config(text="Der Computer 2 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[1] == gridCopy[4] == gridCopy[7] == "O":
                        grid1.config(image=O_img)
                        grid4.config(image=O_img)
                        grid7.config(image=O_img)
                        T.config(text="Der Computer 2 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                    elif gridCopy[2] == gridCopy[5] == gridCopy[8] == "O":
                        grid2.config(image=O_img)
                        grid5.config(image=O_img)
                        grid8.config(image=O_img)
                        T.config(text="Der Computer 2 hat gewonnen!", fg="red", font='helvetica 14')
                        te = True
                        break
                for i in freeBtn:
                    gridCopy = grid[:]
                    gridCopy[i] = "X"
                    if gridCopy[0] == gridCopy[1] == gridCopy[2] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[3] == gridCopy[4] == gridCopy[5] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[6] == gridCopy[7] == gridCopy[8] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[0] == gridCopy[4] == gridCopy[8] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[2] == gridCopy[4] == gridCopy[6] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[0] == gridCopy[3] == gridCopy[6] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[1] == gridCopy[4] == gridCopy[7] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                    elif gridCopy[2] == gridCopy[5] == gridCopy[8] == "X":
                        x = btns[i]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        te = True
                        grid[i] = "O"
                        freeBtn.remove(i)
                        break
                if te:
                    te = False
                    Computer_1()
                    break
                else:
                    freieEcken = []
                    freieFelder = []
                    for i in freeBtn:
                        if i in [0, 2, 6, 8]:
                            freieEcken.append(i)
                    if len(freieEcken) > 0:
                        a = random.choice(freieEcken)
                        x = btns[a]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        grid[a] = "O"
                        freeBtn.remove(a)
                        break
                    if 4 in freeBtn:
                        grid[4] = "O"
                        grid5.config(image=O_img)
                        grid5.config(state=DISABLED)
                        freeBtn.remove(4)
                        break
                    for i in freeBtn:
                        if i in [1, 3, 5, 7]:
                            freieFelder.append(i)
                            break
                    if len(freieFelder) > 0:
                        a = random.choice(freieFelder)
                        grid[a] = "O"
                        x = btns[a]
                        x.config(image=O_img)
                        x.config(state=DISABLED)
                        freeBtn.remove(a)
                        break
            root.after(t, Computer_1)

def button_click():
    if auswahll.get() == "Spieler" and auswahl2.get() == "Spieler":
        PvsP()
    elif auswahll.get() == "Computer" and auswahl2.get() == "Computer":
        CvsC()
    else:
        PvsC()

root = Tk()
root.title("Tic Tac Toe Start")

labelTop = Label(root, text="Wähle die Spieler!", font="helvetica 14 underline")
labelTop.grid(column=2, row=0)

mensch_img = PhotoImage(file="Images/mensch.png")
ki_img = PhotoImage(file="Images/ki.png")

photo1 = Label(root, image=mensch_img)
photo2 = Label(root, image=mensch_img)
photo1.grid(column=0, row=1)
photo2.grid(column=4, row=1)

labelTop = Label(root, text="VS", fg="red", font="helvetica 14")
labelTop.grid(column=2, row=1)

auswahll = ttk.Combobox(root,values=["Spieler", "Computer"], font="helvetica 14 italic")
auswahll.grid(column=0, row=2)
auswahll.current(0)
auswahll.bind("<<ComboboxSelected>>", aus1)

auswahl2 = ttk.Combobox(root,values=["Spieler", "Computer"], font="helvetica 14 italic")
auswahl2.grid(column=4, row=2)
auswahl2.current(0)
auswahl2.bind("<<ComboboxSelected>>", aus2)

start = Button(root, text="Start", font="helvetica 14 bold", command=lambda: button_click())
start.grid(column=2, row=3)

root.mainloop()