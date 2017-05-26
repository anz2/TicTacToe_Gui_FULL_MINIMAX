# -*- coding: utf-8 -*-
"""
Created on Mon May 22 12:53:53 2017

@author: Anzor
"""

from tkinter import (Button,N,S,W,E,Tk,messagebox)
from random import choice

root=Tk()
root.title("Tic Tac Toe")


bclick=choice([False,True])
def tictactoe(buttons):
    global bclick
    if buttons["text"]==" " and bclick == True:
        buttons["text"]="X"
        bclick=False
    elif buttons["text"]==" " and bclick == False:
        buttons["text"]="O"
        bclick=True
    if (  button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
          button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
          button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or
          button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or       
          button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
          button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X" or       
          button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
          button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        messagebox.showinfo("Winner X","Player X Won The Game!")
    elif (  button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
          button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
          button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
          button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or       
          button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
          button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O" or       
          button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
          button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        messagebox.showinfo("Winner O","Player O Won The Game!")
    elif (button1["text"]!=" " and button2["text"]!=" " and button3["text"]!=" " and
         button4["text"]!=" " and button5["text"]!=" " and button6["text"]!=" " and 
         button7["text"]!=" " and button8["text"]!=" " and button9["text"]!=" "):
        messagebox.showinfo("Game Over","It is Draw!")
        
button1=Button(root,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:tictactoe(button1))
button1.grid(row=1,column=1,sticky=S+N+E+W)
button2=Button(root,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:tictactoe(button2))
button2.grid(row=1,column=2,sticky=S+N+E+W)
button3=Button(root,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:tictactoe(button3))
button3.grid(row=1,column=3,sticky=S+N+E+W)
button4=Button(root,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:tictactoe(button4))
button4.grid(row=2,column=1,sticky=S+N+E+W)
button5=Button(root,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:tictactoe(button5))
button5.grid(row=2,column=2,sticky=S+N+E+W)
button6=Button(root,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:tictactoe(button6))
button6.grid(row=2,column=3,sticky=S+N+E+W)
button7=Button(root,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:tictactoe(button7))
button7.grid(row=3,column=1,sticky=S+N+E+W)
button8=Button(root,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:tictactoe(button8))
button8.grid(row=3,column=2,sticky=S+N+E+W)
button9=Button(root,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:tictactoe(button9))
button9.grid(row=3,column=3,sticky=S+N+E+W)

root.mainloop()





