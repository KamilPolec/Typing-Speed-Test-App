import tkinter as tk
from tkinter import ttk
from time import time


# sentence = "A quick brown fox jumps over the lazy dog."

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test")


class TypingSpeedApp(ttk.Frame):

    def __init__(self, parent):
        super().__init__()
        self.app = parent
        self.grid(pady=12, padx=12, column=0, row=0)

        self.start_time = float(0)

        self.sentence = tk.StringVar()
        self.sentence.set(
            "A quick brown fox jumps over the lazy dog.")
        ttk.Label(self, textvariable=self.sentence).grid(column=0, row=0)

        self.wpm_label = tk.StringVar()
        self.wpm_label.set("Please type in the above to calculate your wpm")
        ttk.Label(self, textvariable=self.wpm_label).grid(column=0, row=1)

        self.user_sentence = tk.StringVar()
        self.user_sentence.trace("w", self.track_wpm)
        self.entry = ttk.Entry(self, textvariable=self.user_sentence)
        self.entry.grid(column=0, row=2)
        self.entry.config(state="disabled")

        ttk.Button(self, text="Start", command=self.start_countdown).grid(column=0, row=3)
        self.milliseconds = 0
        self.seconds = 1
        self.minutes = self.seconds // 60
        self.seconds = self.seconds % 60
        self.countdown_running = False
        self.timer_running = False
        self.countdown = tk.StringVar()
        self.countdown.set(f"{self.minutes:02}:{self.seconds:02}")
        ttk.Label(self, textvariable=self.countdown).grid(column=0, row=4)

    def track_wpm(self, *args):
        self.entry.config(state="enabled")
        self.entry.focus()
        if self.start_time == 0:
            self.start_time = float(time())

        no_of_user_wrds = len(self.user_sentence.get().split())
        if self.seconds > 0:
            wpm = 60 / (float(time()) - self.start_time) * no_of_user_wrds
            self.wpm_label.set(f"Your WPM is: {wpm:.2f}")

        if len(self.user_sentence.get()) == len(self.sentence.get()):
            no_of_user_wrds = len(self.user_sentence.get().split())
            wpm = 60 / (float(time()) - self.start_time) * no_of_user_wrds
            self.wpm_label.set(f"Your final WPM is: {wpm:.2f}")
            self.start_time = float(0)
            self.entry.config(state="disabled")
            self.timer_running = False

    def start_countdown(self):
        if not self.countdown_running:
            self.countdown_running = True
            self.update_countdown()

    def start_timer(self):
        self.user_sentence.set("")
        self.countdown_running = False
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def update_countdown(self):
        if self.seconds > 0 and self.countdown_running:
            self.seconds -= 1
            time_str = f"{self.minutes:02}:{self.seconds:02}"
            self.countdown.set(time_str)
            self.app.after(1000, self.update_countdown)
        else:
            self.start_timer()

    def update_timer(self):
        if self.timer_running:
            self.track_wpm()
            self.seconds += 1
            time_str = f"{self.minutes:02}:{self.seconds:02}"
            self.countdown.set(time_str)
            self.app.after(1000, self.update_timer)


if __name__ == "__main__":
    app = App()
    TypingSpeedApp(app)
    app.mainloop()
