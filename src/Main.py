from YTManager import Downloader
from tkinter import *

window = Tk()

#title config
window.title("YT Downloader")
for i in range(5):
    window.grid_columnconfigure(i)
for i in range(5):
    window.grid_rowconfigure(i)

#icon config
try:
    icon = PhotoImage(file = "src/icon.png")
    window.iconphoto(True, icon)
except:
    pass

#window confi
window.geometry("518x110")
window.configure(background="black")
window.resizable(False, False)

#labels
empty = Label(window, text="", bg="black")
empty.grid(row = 0,column = 0)

title = Label(window, text="YT Downloader", font=("Arial", 30), bg="black", fg="red")
title.grid(row = 0,column = 4)

subtitle = Label(window, text="by MarcMeRu11", font=("Arial", 7), bg="black", fg="white")
subtitle.grid(row = 1,column = 4)

link = Entry(x = 25, width=50)
link.grid(row = 5,column = 4)

downloadButton = Button(text="Download", width=10, height=1, bg="black", fg="red", command=lambda: Downloader(link.get()).download())
downloadButton.grid(row = 5,column = 5)


window.mainloop()