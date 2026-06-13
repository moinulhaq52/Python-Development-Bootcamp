from tkinter import *
from token import STRING

from win32con import BOLD_FONTTYPE

window = Tk()
window.title("Mile To Kilometer Converter")
window.minsize(width="400",height="300")
window.config(padx=50,pady=50)

#1 Input
mile_Input = Entry(width=20)
mile_Input.focus()
mile_Input.grid(column=2,row=0)
#CONVERT FUNCTION
def CONVERT_MILES_TO_KM():
    miles = float(mile_Input.get())
    km = miles*1.609
    km_label.config(text= f"{km}km")

    pass

#4 Label
# Miles Label
mile_label = Label(text="Miles",font=("Arial",15,"bold"))
mile_label.grid(column=3,row=0)
#Equal Label
equal_label = Label(text="is Equal to",font=("Arial",15,"bold"))
equal_label.grid(column=1,row=1)
#Km Label changeable
km_label = Label(text="0",font=("Arial",15,"bold"))
km_label.grid(column=2,row=1)
#Km Simple Label
kilometer_label = Label(text="km",font=("Arial",15,"bold"))
kilometer_label.grid(column=3,row=1)

#1 Button
submit_button = Button(text="Convert",command=CONVERT_MILES_TO_KM)
submit_button.grid(column=2,row=2)

window.mainloop()
