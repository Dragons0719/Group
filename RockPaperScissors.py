# Coded by James Woolbright and Blake Richardson
# Designed by Elijah Rotenberger
# Journal Writer - Lucas Deckard
# Researcher - Bernie Jobel-Diaz
# Debugger - Luke Atkins
# Last Updated: 9/20/2022

import random
import tkinter as tk
from tkinter.font import BOLD
 
window = tk.Tk()
window.withdraw()
window.attributes("-fullscreen", True)
window.title('Rock Paper Scissors')
window.config(bg='#09CCF7')
 
message = tk.Label(window,text='Welcome to Rock Paper Scissors!\nChoose one of the options to start.')
message.place(x=525, y=20)
message.config(bg='#09CCF7', font=('Poor Richard', 50, 'bold'))
 
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""
 
 
 
 
def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissor':2}
    return rps[choice]
def number_to_choice(number):
    rps={0:'rock',1:'paper',2:'scissor'}
    return rps[number]
 
def random_computer_choice():
    return random.choice(['rock','paper','scissor'])
tielabel = tk.Label(window, text="",bg="#09CCF7",fg="black")
tielabel.place(x=910, y=200)
def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        tielabel.config(text="You have tied", font=('Poor Richard', 15))
    elif((user-comp)%3==1):
        tielabel.config(text="")
        USER_SCORE+=1
    else:
        tielabel.config(text="")
        COMP_SCORE+=1
    text_area = tk.Text(window,height=20,width=60,bg="#FFFF99")
    text_area.place(x=670,y=250)
    answer = "                                                                           Your Choice: {uc} \n \n                                                                    Computer's Choice : {cc} \n \n                                                                                 Your Score : {u} \n \n                                                                            Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)    
    text_area.config(font=('Poor Richard', 15), bg='#1CB0D1')
    text_area.insert(tk.END,answer)
 
def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='scissor'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
 
button1 = tk.Button(window,text="       Rock       ",bg="skyblue",command=rock, font=('Arial', 50, BOLD), relief=tk.SOLID, borderwidth=5)
button1.place(x=100, y=900)
button2 = tk.Button(window,text="       Paper      ",bg="pink",command=paper, font=('Arial', 50, BOLD), relief=tk.SOLID, borderwidth=5)
button2.place(x=700, y=900)
button3 = tk.Button(window,text="      Scissors     ",bg="lightgreen",command=scissor, font=('Arial', 50, BOLD), relief=tk.SOLID, borderwidth=5)
button3.place(x=1300, y=900)

 
t1 = False
def Start():
    global t1
    t1 = True
    window.deiconify()
def Stop():
    global t1
    t1 = False
    window.withdraw()
exitbutton = tk.Button(window,bg="white",text="exit", command=Stop)
exitbutton.place(x=100, y=500)
def main():
    while t1 == True:
        window.update()
