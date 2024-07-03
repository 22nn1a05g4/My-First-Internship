from tkinter import *
import random, string
import pyperclip

password =Tk()
password.geometry("300x300")
password.resizable(0,0)
password.configure(background="grey")
password.title("Random - PASSWORD GENERATOR")

heading = Label(password, text='PASSWORD GENERATOR', font='arial 10 bold',bg='beige')
heading.pack(pady=30) 

Label(password, text ='Random', font ='arial 10 bold').pack(side = BOTTOM,pady=15)

pass_label = Label(password, text='PASSWORD LENGTH', font='arial 10 bold')
pass_label.pack()

pass_len = IntVar()
length = Spinbox(password, from_ = 4, to_ = 30 , textvariable = pass_len , width = 10).pack()

pass_str = StringVar()

def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(password, text = "GENERATE A PASSWORD" , command = Generator ).pack(pady= 5)

Entry(password , textvariable = pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(password, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)
password.mainloop()
