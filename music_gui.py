import os
import tkinter as tk
from tkinter.filedialog import askdirectory
import pygame as pg

#create a gui window
root = tk.Tk()

#create a title
root.title("Music gui")

#configure the size
screen_height = 350
screen_width = 450
root.minsize(width=screen_width, height=screen_height)

#create a ask directory box
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir() #gives you a list of all the songs

play_list = tk.Listbox(root,
                       font="Helventica",
                       bg="pink",
                       fg="blue",
                       selectmode=tk.SINGLE
                       )


play_list.pack(fill="both", expand="True")

pos = 0
for song in song_list:
    play_list.insert(pos, song)
    pos += 1

#initialize pygame lib
pg.init()

def play_music():
    pg.mixer.music.load(play_list.get(tk.ACTIVE)) #this loads the file that you selected in the listbox
    song_name.set(play_list.get(tk.AKTIVE()))

    pg.mixer.music.play()

def play_on_selection(event):
    play_music()
    pause_button.configure(text="Unpause",
                           command=unpause_music)

def stop_music():
    pg.mixer.music.stop()

def pause_music():
    pg.mixer.music.pause()
    pause_button.configure(text="Unpause",
                           command=unpause_music)

def unpause_music():
    pg.mixer.music.unpause()
    pause_button.configure(text="Pause",
                           command=pause_music)


#create a button

#start to play
play_button = tk.Button (root,
                        text="Play",
                        width=5,
                        height=3,
                        font="Helvetica 12 bold",
                        highlightbackground="blue",
                        highlightthickness=10,
                        command=play_music
                        )

stop_button = tk.Button (root,
                        text="Stop",
                        width=5,
                        height=3,
                        font="Helvetica 12 bold",
                        highlightbackground="blue",
                        highlightthickness=10
                        )

pause_button = tk.Button (root,
                        text="Pause",
                        width=5,
                        height=3,
                        font="Helvetica 12 bold",
                        highlightbackground="blue",
                        highlightthickness=10
                        )

#place the name
song_name =

#place button
play_button.pack(fill="x")
stop_button.pack(fill="x")
pause_button.pack(fill="x")
#unpause_button.pack(fill="x")

#play music by pressing selection
play_list.bind("<<ListboxSelect>>", play_on_selection)

root.mainloop()
unpause_button = tk.Button (root,
                        text="unpause",
                        width=5,
                        height=3,
                        font="Helvetica 12 bold",
                        highlightbackground="blue",
                        highlightthickness=10
                        )