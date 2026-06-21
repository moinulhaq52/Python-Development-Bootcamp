from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

#1 Issue that I notice
# if we save 2 password of same website, and then we search website it shows only first one


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letter = [random.choice(letters)
    for _ in range(random.randint(8,10))]
    pass_number = [random.choice(numbers)
    for _ in range(random.randint(2,4))]
    pass_symbols = [random.choice(symbols)
    for _ in range(random.randint(2,4))]

    password = pass_symbols + pass_number + pass_letter
    # print(password)
    random.shuffle(password)

#old
    # for value in password:
    #     final_password += value

#new
    final_password = "".join(password)
    Password_Input.delete(0,END)
    Password_Input.insert(0,final_password)
    pyperclip.copy(final_password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def saving_data():
    website = Website_Input.get()
    email = Email_Input.get()
    password = Password_Input.get()

    data_dict = {
        website: {
        "Email" : email,
        "Password" : password,
    }
    }

    if len(email) == 0 or len(website)==0 or len(password) == 0:
        messagebox.showinfo(title="Error While Checking",message="Please insert all values!!")
    else:
        try:
            with open("file.json","r") as f:
                data = json.load(f)
                data.update(data_dict)
        except:
            with open("file.json", "w", encoding="utf-8") as f:
                json.dump(data_dict,f,indent=4)
        else:
            with open("file.json","w",encoding="utf-8") as f:
                json.dump(data,f,indent=4)
        finally:
            Website_Input.delete(0,END)
            Password_Input.delete(0,END)

# ---------------------------- Search Data ------------------------------- #
def search_data():
    website = Website_Input.get()
    try:
        with open("file.json", "r") as f:
            all_data = json.load(f)
    except:
        messagebox.showinfo(title="Account Info..",message="No Text in File Or File Not Exist")
    else:
        for data in all_data:
            if data == website:
                # print(f"{all_data[data]["Email"]}  {all_data[data]["Password"]}")
                messagebox.showinfo(title="Account Info...",
                                    message=f"Your Email : {all_data[data]["Email"]}\nYour Password : {all_data[data]["Password"]} \nWebsite : {data} ")
            else:
                messagebox.showinfo(title="Account Info..", message="Record Not Found")


# ---------------------------- UI SETUP ------------------------------- #
Window = Tk()
Window.config(padx=50,pady=50)
Window.title("PASSWORD GENERATOR")


#IMAGE SETUP
my_canvas = Canvas(width=200,height=200,highlightthickness=0)
LOCK_IMAGE = PhotoImage(file="logo.png")
my_canvas.create_image(100,100,image=LOCK_IMAGE)
my_canvas.grid(column=1,row=0)


#3 Label ,font=("Arial",10,"bold")

#Website_Label
Website_Label = Label(text="Website:")
Website_Label.grid(column=0,row=1)

#User/Email_Label
Email_Label = Label(text="Email/Username:")
Email_Label.grid(column=0,row=2)

#Password_Label
Password_Label = Label(text="Password:")
Password_Label.grid(column=0,row=3)


#3 Inputs

#Webiste Input
Website_Input = Entry(width=34)
Website_Input.grid(column=1,row=1)
Website_Input.focus()

#User/Email Input
Email_Input = Entry(width=45)
Email_Input.grid(column=1,row=2,columnspan=2)
Email_Input.insert(0,"moin@gmail.com")


#Password Input
Password_Input = Entry(width=34)
Password_Input.grid(column=1,row=3)

#3 Button

#Generate
Generate_Button = Button(text="GENERATE",highlightthickness=0 ,borderwidth=1,width=9,border=0,bg="yellow", command=generate_pass)
Generate_Button.grid(column=2,row=3)

#Add
Add_Button = Button(text="SAVE/ADD", highlightthickness=0 ,borderwidth=1,width=39,border=0,bg="green",command=saving_data)
Add_Button.grid(column=1,row=4,columnspan=2)

#Search
Search_Button = Button(text="SEARCH",highlightthickness=0, borderwidth=1, width=9,border=0,bg="blue" , command=search_data)
Search_Button.grid(column=2,row=1)







Window.mainloop()