import tkinter as tk
from tkinter import messagebox
from tkinter import *

root = tk.Tk()
root.title("TIC TAC TOE")


playerX, playerO = IntVar(),IntVar()
playerX.set(0)
playerO.set(0)

frame = tk.Frame(root,height = 500,width = 280,bg="lightblue",relief="ridge")
frame.pack()


frame_1 = tk.Frame(frame,height=300,width=280,bg = "gray")
frame_1.place(height=290,width=290)


frame_2 = tk.Frame(frame,height=50,width=280,bg="gray")
frame_2.place(height =50,width=285,relx=0,rely=0.58)
label_1 = tk.Label(frame_2,bg="lightblue",font=('arial',12,'bold'))
label_1.place(relx=0,rely=0,relwidth=1.6,relheight=1)


frame_3 = tk.Frame(frame,height=50,width=280,bg="lightgreen")
frame_3.place(height =80,width=285,relx=0,rely=0.68)
label_2 = tk.Label(frame_3,text="For\nPlayer X: ",font=('arial',15,'bold'),bg="cadet Blue")
label_2.place(relx=0,rely=0,relwidth=0.5,relheight=1)


frame_4 = tk.Frame(frame,height=50,width=280,bg="lightgreen")
frame_4.place(height =80,width=285,relx=0,rely=0.84)
label_3 = tk.Label(frame_4,text="For\nPlayer O: ",font=('arial',15,'bold'),bg="cadet Blue")
label_3.place(relx=0,rely=0,relwidth=0.5,relheight=1)



textplayerX = tk.Entry(frame_3,font=30,bd=2,width=30,fg="black",textvariable = playerX)
textplayerX.place(relx=0.45,rely=0,relheight=1)

textplayerO = tk.Entry(frame_4,bd=2,width=30,font=30,fg="black",textvariable=playerO)
textplayerO.place(relx=0.45,rely=0,relheight=1)


click =True
label_1['text'] = "X's turn"
def position(button):

    global click
    label_1['text'] ="X's turn"
    if button['text'] == "" and click == True:
        button['text'] = "X"
        label_1['text'] = "O's turn"
        click = False
        check_if_win()
        Xscore()
    elif button['text'] == "" and click == False:
        button['text'] = "O"
        click = True
        check_if_win()
        Oscore()

def restart():
    reset()
    playerO.set(0)
    playerX.set(0)

def reset():
    button_1['text'] = ""
    button_2['text'] = ""
    button_3['text'] = ""
    button_4['text'] = ""
    button_5['text'] = ""
    button_6['text'] = ""
    button_7['text'] = ""
    button_8['text'] = ""
    button_9['text'] = ""



def check_if_win():
    check_rows()
    check_columns()
    check_diagonals()

def check_rows():
    row_1 = button_1["text"] == button_2["text"] == button_3["text"] != ""
    row_2 = button_4["text"] == button_5["text"] == button_6["text"] != ""
    row_3 = button_7["text"] == button_8["text"] == button_9["text"] != ""
    if row_1 :
        return tk.messagebox.showinfo("Winner"," %s you have just won a game"%button_1['text'])
    elif row_2:
        return  tk.messagebox.showinfo("Winner"," %s you have just won a game"%button_4['text'])
    elif row_3:
        return tk.messagebox.showinfo("Winner"," %s you have just won a game"%button_7['text'])
    return


# check colmuns
def check_columns():
    column_1 = button_1["text"] == button_4["text"] == button_7["text"] != ""
    column_2 = button_2["text"] == button_5["text"] == button_8["text"] != ""
    column_3 = button_3["text"] == button_6["text"] == button_9["text"] != ""
    if column_1:
        return tk.messagebox.showinfo("Winner"," %s you have just won a game"%button_1['text'])
    elif column_2:
        return  tk.messagebox.showinfo("Winner"," %s you have just won a game"%button_2['text'])
    elif column_3:
        return tk.messagebox.showinfo("Winner"," %s you have just won a game"%button_3['text'])
    return


# check diagonals
def check_diagonals():
    diagonal_1 = button_1['text'] == button_5['text'] == button_9['text'] != ""
    diagonal_2 = button_7['text'] == button_5['text'] == button_3['text'] != ""
    if diagonal_1:
        return  tk.messagebox.showinfo("Winner"," %s you have just won a game"%button_1['text'])
    elif diagonal_2:
        return tk.messagebox.showinfo("Winner"," %s you have just won a game"%button_7['text'])
    return


def Xscore():
    row_1 = button_1["text"] == button_2["text"] == button_3["text"] == "X"
    row_2 = button_4["text"] == button_5["text"] == button_6["text"] == "X"
    row_3 = button_7["text"] == button_8["text"] == button_9["text"] == "X"
    column_1 = button_1["text"] == button_4["text"] == button_7["text"] == "X"
    column_2 = button_2["text"] == button_5["text"] == button_8["text"] == "X"
    column_3 = button_3["text"] == button_6["text"] == button_9["text"] == "X"
    diagonal_1 = button_1['text'] == button_5['text'] == button_9['text'] == "X"
    diagonal_2 = button_7['text'] == button_5['text'] == button_3['text'] == "X"
    if row_1 or row_2 or row_3 or column_1 or column_2 or column_3 or diagonal_1 or diagonal_2 == "X":
        n = int(playerX.get())
        score = (n + 1)
        textplayerX['textvariable'] = playerX.set(score)


def Oscore():

    row_1 = button_1["text"] == button_2["text"] == button_3["text"] == "O"
    row_2 = button_4["text"] == button_5["text"] == button_6["text"] == "O"
    row_3 = button_7["text"] == button_8["text"] == button_9["text"] == "O"
    column_1 = button_1["text"] == button_4["text"] == button_7["text"] == "O"
    column_2 = button_2["text"] == button_5["text"] == button_8["text"] == "O"
    column_3 = button_3["text"] == button_6["text"] == button_9["text"] == "O"
    diagonal_1 = button_1['text'] == button_5['text'] == button_9['text'] == "O"
    diagonal_2 = button_7['text'] == button_5['text'] == button_3['text'] == "O"
    if row_1 or row_2 or row_3 or column_1 or column_2 or column_3 or diagonal_1 or diagonal_2 == "X":
        n = int(playerO.get())
        score = (n + 1)
        textplayerO['textvariable'] = playerO.set(score)



resetbutton = tk.Button(frame_2,height = 2,font = 20,width=8,text="Reset",command=reset)
resetbutton.grid(row = 0,column =1)


restartbutton = tk.Button(frame_2,height = 2,font = 20,width=8,text="Restart",command=restart)
restartbutton.grid(row=0,column=3)


button_1 = tk.Button(frame_1,height = 5,width=12,text="",command = lambda:position(button_1))
button_1.grid(row = 1,column =1)

button_2 = tk.Button(frame_1,height = 5,width=12,text="",command = lambda:position(button_2))
button_2.grid(row = 1,column =2)

button_3 = tk.Button(frame_1,height = 5,width=12,text="",command = lambda:position(button_3))
button_3.grid(row = 1,column =3)

button_4 = tk.Button(frame_1,height = 5,width=12,text="",command = lambda:position(button_4))
button_4.grid(row = 2,column =1)

button_5 = tk.Button(frame_1,height = 5,width=12,text="",command = lambda:position(button_5))
button_5.grid(row = 2,column =2)

button_6 = tk.Button(frame_1,height = 5,width=12,text="",command = lambda:position(button_6))
button_6.grid(row = 2,column =3)

button_7 = tk.Button(frame_1,height = 5,width=12,text="",command = lambda:position(button_7))
button_7.grid(row = 3,column =1)

button_8 = tk.Button(frame_1,height = 5,width=12,text="",command = lambda:position(button_8))
button_8.grid(row = 3,column =2)

button_9 = tk.Button(frame_1,height = 5,width=12,text="",command = lambda:position(button_9))
button_9.grid(row = 3,column =3)





root.mainloop()
