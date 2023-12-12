import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
import pandas as pd
from tkinter import messagebox

# create gui window
root = tk.Tk()
# give your gui a title
root.title("Online pet")
# set the size of the gui
screen_width=350
screen_height=350
root.minsize(width=screen_width, height=screen_height)
# change colour of background
#root.configure(background="white")

# place an image on the first screen
def add_image(root, file_path, width, height):
    """This definition will place the image on the gui window.
    You need to specify the variable name that creates your gui window and the image file path"""

    # for some reason this image will not appear without specifying global variables
    global pic, f1

    # Create the frame for the first windows of the game
    f1 = tk.Frame(root)
    # read the image you want to use for the first fra,e
    img = Image.open(file_path)
    # resize the image - make sure this is the same size as the gui window
    img = img.resize((width, height), Image.LANCZOS)
    # add this code to view the image as the frame
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    # code to just place the image
    Lab.pack()
    f1.pack()

def enter_user_data():

    #create a dictionary that stores the information of the user

    current_timestamp = datetime.now()
    user_data = {
    "name_of_user": name.get(),
    "user_id":username.get(),
    "created_at":current_timestamp
    }

    user_ids = list(pd.read_csv("data/user_data.csv").user_id)

    #reads list of existing user_ids and if username is given shows warning
    if username.get() in user_ids:
        tk.messagebox.showwarning("Warning! Username already exists :(")

    else:
        #coverts the dictionary into a data frame
        user_data_df = pd.DataFrame([user_data])
        #convert into csv file
        user_data_df.to_csv("data/user_data.csv", header=False, index=False, mode="a")

        #delete all the widgets
        #the for thing

        #the thanks label

        thank_you_label = tk.Label(root, text=f"Thank you, {name.get()}")
        thank_you_label.pack(side=tk.TOP)


def create_new_user_page():
    global homepage, new_label, name, name_box, username_label, username, username_box, favourite_pet, favourite_pet_box

    f1.destroy()
    welcome_label.destroy()
    new_user.destroy()
    returning_user.destroy()
    #for i in root.winfo.children():
        #i.destroy()

    #create button for homepage
    homepage = tk.Button(root, text="Homepage", command=create_homepage)

    homepage.pack(side=tk.BOTTOM)

    #create labels and entry boxes
    new_label = tk.Label(root, text="Welcome new user", font="Arial 12 bold")
    new_label.pack(side=tk.TOP, anchor=tk.CENTER)


    #get information about new user
    new_label = tk.Label(root, text="What is your name?")
    new_label.place(x=10, y=100)

    #create entry

    name = tk.StringVar()
    name_box = tk.Entry(root, textvar=name, fg="white", bg="black")
    name_box.place(x=10, y=125)

    #create username
    username_label = tk.Label(root, text="What is your username?")
    username_label.place(x=10, y=150)

    username = tk.StringVar()
    username_box = tk.Entry(root, textvar=username, fg="white", bg="black")
    username_box.place(x= 10, y=175)


    favourite_pet_label = tk.Label(root, text="What is your favourite pet?")
    favourite_pet_label.place(x=10, y=200)

    #enter for favourite pet
    favourite_pet = tk.StringVar()
    favourite_pet_box = tk.Entry(root, textvar=favourite_pet, fg="white", bg="black")
    favourite_pet_box.place(x=10, y=225)

    #create a button to store it all

    submit = tk.Button(root, text="Submit information", command=enter_user_data)
    submit.pack(side=tk.BOTTOM)

def create_homepage():
    global welcome_label
    add_image(root, "Images/hedgehog_graphic.png", screen_width, screen_height)

    global welcome_label, new_user, returning_user

    #use try and except to try execute some code if it errors
    try:
        homepage.destroy()
    except:
        pass

    #steps to create a homepage
    #create the label
    welcome_label = tk.Label(root, text="Welcome to the online pet page!", font="Arial 12 bold", fg="black", bg="white")
    welcome_label.place(x=20, y=10)

    #add the buttons
    new_user = tk.Button(root, text="New user", command=create_new_user_page)
    returning_user = tk.Button(root, text="Returning user")

    new_user.pack()
    returning_user.pack()

#call the definition
create_homepage()

#execute the code
root.mainloop()