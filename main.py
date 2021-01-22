import tkinter as tk
import pygame
import os
import glob

"""Pygame Init"""
pygame.init()
pygame.mixer.init()

"""Create a window"""
player = tk.Tk()


"""Edit window"""
player.title("Audio Player")
player.geometry("410x680")


"""Playlist Register"""
# os.chdir("Playlist/")
# playlist = os.listdir()

song_list = glob.glob("Playlist\\*.mp3")

# prefix, newplaylist = zip(*[[y[0], y[-1]] for y in [x.split("\\") for x in song_list]])
new_songlist = [y[-1] for y in [x.split("\\") for x in song_list]]


"""Playlist Input"""
playlist = tk.Listbox(player, highlightcolor="red", selectmode=tk.SINGLE)
for song in song_list:
    playlist.insert(0, song)



"""Action event"""
def play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    song_name_var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()


def stop_play():
    pygame.mixer.music.stop()


"""Song name"""
# label = tk.LabelFrame(player, text="Song name")
# contents1 = tk.Label(label, text=file[:-4])
song_name_var = tk.StringVar()
song_title = tk.Label(player, textvariable=song_name_var)

"""Register buttons"""
play_button = tk.Button(player, width=5, height=3, text="Play", command=play)
stop_button = tk.Button(player, width=5, height=3, text="Stop", command=stop_play)


"""Place widgets"""
song_title.pack(fill="x")
playlist.pack(fill="both", expand="yes")
play_button.pack(fill="x")
stop_button.pack(fill="x")

# contents1.pack()
# label.pack(fill="both", expand="yes")



"""Activate"""
player.mainloop()
