import math
from pickle import GLOBAL
from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
HEADING = "POTATO TIMER"
CHECK = "✔"
START = "Start"
END = "RESET"
REPS = 0
TIMER_WINDOW = NONE
TIME_COUNT = NONE
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    global REPS,TIMER_WINDOW , TIME_COUNT
    REPS = 0
    Heading_Label.config(text=HEADING , bg=PINK , font=(FONT_NAME,36,"bold"), fg="green")
    canvas.itemconfig(TIME_COUNT, text="00:00")
    Check_Label.config(text="")
    window.after_cancel(TIMER_WINDOW)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
#Start Timer
def start_time():
    global REPS
    REPS += 1

    WORK_IN_SEC = WORK_MIN * 60
    SHORT_BREAK_IN_SEC = SHORT_BREAK_MIN * 60
    LONG_BREAK_IN_SEC = LONG_BREAK_MIN * 60

    if(REPS % 8 == 0):
        Heading_Label.config(text="LONG BREAK" ,fg=YELLOW)
        count_timer(LONG_BREAK_IN_SEC)
    elif(REPS % 2 == 0):
        Heading_Label.config(text="SHORT BREAK" ,fg="red")
        count_timer(SHORT_BREAK_IN_SEC)
    else:
        Heading_Label.config(text="WORK TIME" , fg="blue")
        count_timer(WORK_IN_SEC)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

#Count Time
def count_timer(time):
    global TIMER_WINDOW
    #Min
    Count_Min = floor( time / 60 )
    if Count_Min < 10:
        Count_Min = "0"+f"{Count_Min}"
    #Sec
    Count_Sec = time % 60
    if Count_Sec < 10:
        Count_Sec = "0"+f"{Count_Sec}"


    canvas.itemconfig(TIME_COUNT,text=f"{Count_Min}:{Count_Sec}")
    if(time)>0:
        TIMER_WINDOW = window.after(1000,count_timer,time-1)
    else:
        start_time()
        mark = ""
        for n in range(math.floor(REPS/2)):
            mark += CHECK
        Check_Label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
#Window | Tkinter
window = Tk()
window.title("POMODORO(TOMOTA) TIMER")
window.config(padx=90,pady=90 , bg=PINK ,width=1200,height=300)

#By Tkinter Use Photo
TOMATO_IMAGE = PhotoImage(file="tomato.png")

#Heading
Heading_Label = Label(text=HEADING , bg=PINK , font=(FONT_NAME,36,"bold"), fg="green")
Heading_Label.grid(column=2,row=1)

#Tomato Time With Tomato Image
canvas = Canvas(width=210,height=230,bg=PINK , highlightthickness=0)
canvas.create_image(103,115,image = TOMATO_IMAGE)
TIME_COUNT = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,36,"bold"))
canvas.grid(column=2,row=2)

#Start Button & Start Counting
Start_Button = Button(text=START , bg=YELLOW , highlightthickness=0 , borderwidth=1, command= start_time)
Start_Button.grid(column=1,row=3)

#CheckMark
Check_Label = Label(text="" ,font=("Arial",20,"bold"),fg="green" , bg=PINK)
Check_Label.grid(column=2,row=4)

#End Button
End_Button = Button(text=END,bg=YELLOW ,highlightthickness=0 ,borderwidth=1 , command= reset_time)
End_Button.grid(column=3,row=3)




window.mainloop()
