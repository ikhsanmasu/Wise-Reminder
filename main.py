from tkinter import *
import requests

import os
import sys

# use this directory when generating exe file
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

background_dir = application_path + "/background.png"
button_logo_dir = application_path + "/wise-man.png"


def get_quote():
    respons = requests.get(url="https://zenquotes.io/api/random")
    respons.raise_for_status()
    data = respons.json()
    quote = data[0]['q']
    said_by = data[0]['a']
    canvas.itemconfig(quote_text, text=f"{quote}\n~{said_by}~")

window = Tk()
window.title("Wise reminder..")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=background_dir)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="You don't gave to be great to start, but you have to start to be great", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=button_logo_dir)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()