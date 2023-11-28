import tkinter as tk
from datetime import date
from PIL import Image, ImageTk

# create gui window
root = tk.Tk()
# give your gui a title
root.title("age and calculator")
# set the size of the gui
root.minsize(width=450, height=450)
# change of background
f1 = tk.Frame(root)
img = Image.open("images/pic.png")
img = img.resize((350,350), Image.LANCZOS)
pic = ImageTk.PhotoImage(img)
Lab = tk.Label(f1,image=pic)
Lab.pack()
f1.pack()

def calculate_age():
    global age, dob

    print ("age")
    today = date.today()
    #what age is the user
    dob = cal.get.date()

    age = int((today - dob).days / 365.25)

    title = tk.Label(root,
                     text="This is your age:",
                     fg="black",
                     font="Geneva 12 bold"
                     )
    title.place(x=30, y=25)

    age = tk.Label(root,
                   text=age,
                   fg="black",
                   font="Geneva 12 bold"
                   )
    title.place(x=30, y=65)

# create label that welcomes the user
title = tk.Label(root,
         text="What is your date of birth? Please write in this format: YYYY/MM/DD",
         fg="black",
         font="Geneva 12 bold"
         )
title.place(x=30, y=25)

# create a box where user can enter the letter
user_date = tk.StringVar()
user_entry = tk.Entry(root,
                        textvariable=user_date,
                        fg="black",
                        font="Geneva 25 bold",
                        )
user_entry.place(x=50, y=350)

calculate = tk.Button(text="Calculate age",
                                 fg="black",
                                 font="Geneva 25 bold",
                                 command=calculate_age
                                 )
calculate.place(x=50, y=400)


root.mainloop()