# -*- coding: utf-8 -*-
"""
Created on Mon May 22 04:04:07 2017

@author: Anzor
"""
from tkinter import (Button,N,S,W,E,Tk,messagebox)
from random import choice
from random import shuffle
from copy import deepcopy  

class TicTacToe:
    def __init__(self,Root):
        self.main=Root
        self.main.title("იქსიკი-ნოლიკი..... დაუმარცხებელი!") #ინტერფეისის სათაური
        
        '''ღილაკების ჩამონათვალი, რომელზეც შეგვიძლია დაჭერა და შესაბამისი უჯრის მონიშვნა'''
        self.button1=Button(self.main,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:self.Play(self.button1))     
        self.button2=Button(self.main,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:self.Play(self.button2))        
        self.button3=Button(self.main,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:self.Play(self.button3))
        self.button4=Button(self.main,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:self.Play(self.button4))        
        self.button5=Button(self.main,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:self.Play(self.button5))       
        self.button6=Button(self.main,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:self.Play(self.button6))        
        self.button7=Button(self.main,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:self.Play(self.button7))        
        self.button8=Button(self.main,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:self.Play(self.button8))
        self.button9=Button(self.main,text=" ",font='Arial 30 bold',height=4,width=8,command=lambda:self.Play(self.button9))
        self.button1.grid(row=1,column=1,sticky=S+N+E+W)
        self.button2.grid(row=1,column=2,sticky=S+N+E+W)
        self.button3.grid(row=1,column=3,sticky=S+N+E+W)
        self.button4.grid(row=2,column=1,sticky=S+N+E+W)
        self.button5.grid(row=2,column=2,sticky=S+N+E+W)
        self.button6.grid(row=2,column=3,sticky=S+N+E+W)
        self.button7.grid(row=3,column=1,sticky=S+N+E+W)
        self.button8.grid(row=3,column=2,sticky=S+N+E+W)
        self.button9.grid(row=3,column=3,sticky=S+N+E+W)
        '''გლობალური ცვლადების ჩამონათვალი'''
        self.PlayerStartsFirst=choice([False,True]) #შემთხვევითად ვირჩევთ რომელი იწყებს მოთამაშე თუ კომპიუტერი
        self.GameOver=False # თამაში დასრულდა თუ არა
        self.infinity=1000000 #უსასრულობის მნიშვნელობა, რომელიც ალფა-ბეტა პროცედურაში გვჭირდება
        self.ComputerValue='O' #კომპიუტერის სათამაშო ცვლადი
        self.PlayerValue='X' #მოთამაშის სათამაშო ცვლადი X ან O
        
        if not self.PlayerStartsFirst:
            self.PlayerValue='O'
            self.ComputerValue='X'
            '''კომპიუტერის თამაში'''
            value,computerMove=self.alfa_beta(self.read(),-self.infinity,self.infinity,True,self.ComputerValue,self.PlayerValue)
            #computerMove=randomChoiceMove(read(),'O')
            self.write(computerMove)
        
    '''შვილი კვანძების გენერატორი, რომელიც აბრუნებს არეულ სიას'''
    def children(self,node,value):
        childrenList=[]
        for row in range(3):
            for column in range(3):
                if node[row][column]==" ":
                    childrenList.append(deepcopy(node))
                    childrenList[-1][row][column]=value
        shuffle(childrenList)
        return childrenList
    '''მიმდინარე კვანძის სიღრმის დამთვლელი მინიმაქსისთვის'''
    def depth(self,node):
        counter=0
        for row in range(3):
            for column in range(3):
                if node[row][column]!=' ':
                    counter+=1
        return counter  
    '''ეკრანზე ვბეჭდავთ სიიდან ამოღებულ ცხრილს'''
    def write(self,node):
        self.button1["text"]=node[0][0]
        self.button2["text"]=node[0][1]
        self.button3["text"]=node[0][2]
        self.button4["text"]=node[1][0]
        self.button5["text"]=node[1][1]
        self.button6["text"]=node[1][2]
        self.button7["text"]=node[2][0]
        self.button8["text"]=node[2][1]
        self.button9["text"]=node[2][2]
    '''ვკითხულობთ ინტერფეისიდან ცხრილს და ვინახავთ სიაში'''
    def read(self):
        node=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        node[0][0]=self.button1["text"]
        node[0][1]=self.button2["text"]
        node[0][2]=self.button3["text"]
        node[1][0]=self.button4["text"]
        node[1][1]=self.button5["text"]
        node[1][2]=self.button6["text"]
        node[2][0]=self.button7["text"]
        node[2][1]=self.button8["text"]
        node[2][2]=self.button9["text"]
        return node
    """ფუნქცია ამოწმებს დასრულდა თამაში თუ არა და აბრუნებს შედეგებს {1,-1,0}""" 
    def checkResult(self,node):
        t=node[0]+node[1]+node[2]
        if (t[0]=='X' and t[1]=='X' and t[2]=='X'or 
            t[3]=='X' and t[4]=='X' and t[5]=='X'or
            t[6]=='X' and t[7]=='X' and t[8]=='X'or
            t[0]=='X' and t[3]=='X' and t[6]=='X'or
            t[1]=='X' and t[4]=='X' and t[7]=='X'or
            t[2]=='X' and t[5]=='X' and t[8]=='X'or
            t[0]=='X' and t[4]=='X' and t[8]=='X'or
            t[2]=='X' and t[4]=='X' and t[6]=='X'):
            return 1
        if (t[0]=='O' and t[1]=='O' and t[2]=='O'or 
            t[3]=='O' and t[4]=='O' and t[5]=='O'or
            t[6]=='O' and t[7]=='O' and t[8]=='O'or
            t[0]=='O' and t[3]=='O' and t[6]=='O'or
            t[1]=='O' and t[4]=='O' and t[7]=='O'or
            t[2]=='O' and t[5]=='O' and t[8]=='O'or
            t[0]=='O' and t[4]=='O' and t[8]=='O'or
            t[2]=='O' and t[4]=='O' and t[6]=='O'):
                return -1
        return 0
    '''ვამოწმებთ შედეგებს და ვნახულობთ თამაში დასრულდა თუ არა.
       დასრულების შემთხვევაში გამოგვაქვს ფანჯარა თუ ვინ გაიმარჯვა'''
    def checkResultGui(self):
        if (  self.button1["text"]=="X" and self.button2["text"]=="X" and self.button3["text"]=="X" or
              self.button1["text"]=="X" and self.button5["text"]=="X" and self.button9["text"]=="X" or
              self.button1["text"]=="X" and self.button4["text"]=="X" and self.button7["text"]=="X" or
              self.button4["text"]=="X" and self.button5["text"]=="X" and self.button6["text"]=="X" or       
              self.button7["text"]=="X" and self.button8["text"]=="X" and self.button9["text"]=="X" or
              self.button3["text"]=="X" and self.button5["text"]=="X" and self.button7["text"]=="X" or       
              self.button2["text"]=="X" and self.button5["text"]=="X" and self.button8["text"]=="X" or
              self.button3["text"]=="X" and self.button6["text"]=="X" and self.button9["text"]=="X"):
            if self.PlayerValue=='X':
                messagebox.showinfo("შენ გაიმარჯვე!")
            else:
                messagebox.showinfo("შენ დამარცხდი")
            return True
        elif (self.button1["text"]=="O" and self.button2["text"]=="O" and self.button3["text"]=="O" or
              self.button1["text"]=="O" and self.button5["text"]=="O" and self.button9["text"]=="O" or
              self.button1["text"]=="O" and self.button4["text"]=="O" and self.button7["text"]=="O" or
              self.button4["text"]=="O" and self.button5["text"]=="O" and self.button6["text"]=="O" or       
              self.button7["text"]=="O" and self.button8["text"]=="O" and self.button9["text"]=="O" or
              self.button3["text"]=="O" and self.button5["text"]=="O" and self.button7["text"]=="O" or       
              self.button2["text"]=="O" and self.button5["text"]=="O" and self.button8["text"]=="O" or
              self.button3["text"]=="O" and self.button6["text"]=="O" and self.button9["text"]=="O"):
            if self.PlayerValue=='O':
                messagebox.showinfo("შენ გაიმარჯვე!")
            else:
                messagebox.showinfo("შენ დამარცხდი")
            return True
        elif (self.button1["text"]!=" " and self.button2["text"]!=" " and self.button3["text"]!=" " and
              self.button4["text"]!=" " and self.button5["text"]!=" " and self.button6["text"]!=" " and 
              self.button7["text"]!=" " and self.button8["text"]!=" " and self.button9["text"]!=" "):
            messagebox.showinfo("ყაიმი")
            return True
        
    '''კომპიუტერი აკეთებს შემთხვევით (შესაძლო) სვლას'''
    def randomChoiceMove(self,node,value):
        return choice(self.children(node,value))
    
    '''სრული მინიმაქსი ალფა-ბეტა პროცედურით'''                         
    def alfa_beta(self,node,alfa,beta, maximizingPlayer,value,rvalue):
        result=self.checkResult(node)
        if result!=0 or self.depth(node)==9:
            '''ვამოწმებთ მიაღწია თუ არა ალგორითმმა გაჩერების მდგომარეობას'''
            return result,node
        if maximizingPlayer:
            '''მაქსიმიზაციის სვლა'''
            bestChoice=[-self.infinity,[]]
            for child in self.children(node,value):
                current=self.alfa_beta(child,alfa,beta,False,rvalue,value)
                if int(bestChoice[0])<current[0]:
                    bestChoice[0]=current[0]
                    bestChoice[1]=child
                alfa=max(alfa,bestChoice[0])
                if beta<=alfa:
                    break #beta cut-off
            return bestChoice
        else:
            '''მინიმიზაციის სვლა'''
            bestChoice=[self.infinity,[]]
            for child in self.children(node,value):
                current=self.alfa_beta(child,alfa,beta,True,rvalue,value)
                if int(bestChoice[0])>current[0]:
                    bestChoice[0]=current[0]
                    bestChoice[1]=child
                beta=min(beta,bestChoice[0])
                if beta<=alfa:
                    break #alfa cut-off
            return bestChoice
        
    '''ღილაკის დაჭერისას გამოიძახება ფუნქცია, რომელიც ასრულებს შესაბამის აქტივობას'''
    def Play(self,buttons):
        if self.GameOver:
            return
        
        '''მოთამაშის თამაში'''
        if buttons["text"]==" ":
            buttons["text"]=self.PlayerValue
            if self.checkResultGui():
                self.GameOver=True
                return
            '''კომპიუტერის თამაში'''
            value,computerMove=self.alfa_beta(self.read(),-self.infinity,self.infinity,self.ComputerValue=='X',self.ComputerValue,self.PlayerValue)
            #computerMove=randomChoiceMove(read(),'O')
            self.write(computerMove)
            if self.checkResultGui():
                self.GameOver=True
                return
def main():
    '''ინტერფეისის შექმნა  და ამუშავება'''
    root=Tk() #ცვლადი ინტერფეისისთვის
    TicTacToeGui=TicTacToe(root)
    root.mainloop()
if __name__ == '__main__':
    main()
