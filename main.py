import tkinter as tk
from tkinter import ttk
from time import time


# sentence = "A quick brown fox jumps over the lazy dog."

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test")


class Body(ttk.Frame):

    def __init__(self, container):
        super().__init__()
        self.grid(pady=12, padx=12, column=0, row=0)

        self.time_bef = float(0)

        self.sentence = tk.StringVar()
        self.sentence.set(
            "A quick brown fox jumps over the lazy dog.")
        ttk.Label(self, textvariable=self.sentence).grid(column=0, row=0)

        self.wpm_label = tk.StringVar()
        self.wpm_label.set("Please type in the above to calculate your wpm")
        ttk.Label(self, textvariable=self.wpm_label).grid(column=0, row=1)
        self.user_sentence = tk.StringVar()
        self.user_sentence.trace("w", self.calculate_wpm)
        ttk.Entry(self, textvariable=self.user_sentence).grid(column=0, row=2)
        ttk.Button(self, text="Start", command=self.calculate_wpm).grid(column=0, row=3)

    def calculate_wpm(self, *args):
        if self.time_bef == 0:
            self.time_bef = float(time())
        no_of_wrds = (len(self.sentence.get().split()))
        if self.user_sentence.get() == self.sentence.get():
            time_aft = (float(time()))
            wpm = 60 / (time_aft - self.time_bef) * no_of_wrds
            self.wpm_label.set(f"Your WPM is: {wpm:.2f}")


if __name__ == "__main__":
    app = App()
    Body(app)
    app.mainloop()
