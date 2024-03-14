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
        ttk.Label(self, textvariable=self.sentence).grid(column=0, row=0, columnspan=3)

        self.wpm_label = tk.StringVar()
        ttk.Label(self, textvariable=self.wpm_label).grid(column=0, row=1, columnspan=3)

        self.user_sentence = tk.StringVar()
        self.user_sentence.trace("w", self.track_wpm)
        self.entry = ttk.Entry(self, textvariable=self.user_sentence)
        self.entry.grid(column=0, row=2, columnspan=3)

        ttk.Button(self, text="Reset", command=self.reset).grid(column=1, row=3)
        self.seconds = 0
        self.timer_running = False
        self.countdown = tk.StringVar()
        ttk.Label(self, textvariable=self.countdown).grid(column=0, row=4, columnspan=3)
        self.reset()

    def track_wpm(self, *args):
        if self.start_time == 0:
            self.start_time = float(time())

        len_of_user_wrds = len(self.user_sentence.get().split())
        if len_of_user_wrds == 1:
            self.start_timer()

        if self.seconds > 0 and len_of_user_wrds > 0:
            wpm = 60 / (float(time()) - self.start_time) * len_of_user_wrds
            self.wpm_label.set(f"Your WPM is: {wpm:.2f}")

        if len(self.user_sentence.get()) == len(self.sentence.get()):
            len_of_user_wrds = len(self.user_sentence.get().split())
            wpm = 60 / (float(time()) - self.start_time) * len_of_user_wrds
            self.wpm_label.set(f"Your final WPM is: {wpm:.2f}")
            self.start_time = float(0)
            self.stop()

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def update_timer(self):
        if self.timer_running:
            self.seconds += 1
            minutes = self.seconds // 60
            seconds = self.seconds % 60
            time_str = f"{minutes:02}:{seconds:02}"
            self.countdown.set(time_str)
            self.app.after(1000, self.update_timer)

    def reset(self):
        self.seconds = 0
        self.timer_running = False
        self.start_time = float(0)
        self.countdown.set("00:00")
        self.user_sentence.set("")
        self.entry.config(state="enabled")
        self.entry.focus()
        self.wpm_label.set("Please type in the above to calculate your wpm")

    def stop(self):
        self.timer_running = False
        self.entry.config(state="disabled")


if __name__ == "__main__":
    app = App()
    TypingSpeedApp(app)
    app.mainloop()
