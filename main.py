from tkinter import *
from tkinter import ttk
from time import time

# sentence = "A quick brown fox jumps over the lazy dog."

time_bef = float(0)


def calculate_wpm(*args):
    global time_bef
    if time_bef == 0:
        time_bef = float(time())
    no_of_wrds = (len(sentence.get().split()))
    if user_sentence.get() == sentence.get():
        time_aft = (float(time()))
        wpm = 60 / (time_aft - time_bef) * no_of_wrds
        wpm_label.set(f"Your WPM is: {wpm:.2f}")


root = Tk()
root.title("Typing speed test")

body = ttk.Frame(root, padding=12)
body.grid()

sentence = StringVar()
sentence.set(
    "A quick brown fox jumps over the lazy dog.")
ttk.Label(body, textvariable=sentence).grid(column=0, row=0)

wpm_label = StringVar()
wpm_label.set("Please type in the above to calculate your wpm")
ttk.Label(body, textvariable=wpm_label).grid(column=0, row=1)
user_sentence = StringVar()
user_sentence.trace("w", calculate_wpm)
ttk.Entry(body, textvariable=user_sentence).grid(column=0, row=2)
ttk.Button(body, text="Start", command=calculate_wpm).grid(column=0, row=3)

root.mainloop()
