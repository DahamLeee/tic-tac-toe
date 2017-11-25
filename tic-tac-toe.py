from tkinter import *
import tkinter.messagebox

#무승부는 만들지 않았음
def whoWin() :

    j = 0
    while j < 3 :
       if list[j]["text"] == list[j+3]["text"] == list[j+6]["text"] != "     " :
           whoIsWinner()
       j += 1

    j = 0
    while j < 7 :
        if list[j]["text"] == list[j+1]["text"] == list[j+2]["text"] != "     " :
           whoIsWinner()
        j += 3

    if list[0]["text"] == list[4]["text"] == list[8]["text"] != "     ":
        whoIsWinner()
    if list[2]["text"] == list[4]["text"] == list[6]["text"] != "     ":
        whoIsWinner()

def whoIsWinner() :
    if player == "X":
        tkinter.messagebox.showinfo("Information", "O User win the game!");
    else :
        tkinter.messagebox.showinfo("Information", "X User win the game!");
        

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
            whoWin()
      else :
            player = "X"
            button["bg"] = "lightgreen"
            whoWin()

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


