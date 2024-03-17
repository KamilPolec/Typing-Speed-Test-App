import tkinter as tk
from tkinter import ttk
from time import time
from wonderwords import RandomWord


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

        self.target_text = tk.StringVar()
        self.generate_words(5)
        ttk.Label(self, textvariable=self.target_text).grid(column=0, row=0)

        self.wpm_label = tk.StringVar()
        ttk.Label(self, textvariable=self.wpm_label).grid(column=0, row=1)

        self.user_input = tk.StringVar()
        self.user_input.trace("w", self.track_wpm)
        self.entry = ttk.Entry(self, textvariable=self.user_input)
        self.entry.grid(column=0, row=2)

        ttk.Button(self, text="Reset", command=self.reset).grid(column=0, row=3)
        self.seconds = 0
        self.timer_running = False
        self.countdown = tk.StringVar()
        ttk.Label(self, textvariable=self.countdown).grid(column=0, row=4)
        self.accuracy = tk.StringVar()
        ttk.Label(self, textvariable=self.accuracy).grid(column=1, row=4)

        self.reset()

    def track_wpm(self, *args):
        user_input = self.user_input.get()
        user_wrd_lst = user_input.split()
        target_text = self.target_text.get()
        num_of_user_words = len(user_wrd_lst)

        if len(user_input) > 0:
            self.start_timer()
            wpm = 60 / (float(time()) - self.start_time) * num_of_user_words
            self.wpm_label.set(f"WPM: {wpm:.2f}")
            word_accuracy = []
            for index, word in enumerate(user_wrd_lst):
                total_word_len = len(word)
                matching_chars = [num for num, (e1, e2) in enumerate(zip([*word], [*target_text.split()[index]])) if
                                  e1 == e2]
                accuracy = (len(matching_chars) / total_word_len) * 100.0
                word_accuracy.append(accuracy)

            mean_accuracy = sum(word_accuracy) / len(word_accuracy)
            self.accuracy.set(f"Accuracy: {mean_accuracy:.2f}%")

        if self.start_time == 0:
            self.start_time = float(time())

        if len(user_input) >= len(target_text) and len(user_wrd_lst[-1]) >= len(target_text.split()[-1]) and len(
                user_wrd_lst) >= len(target_text.split()):
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
        self.user_input.set("")
        self.entry.config(state="enabled")
        self.entry.focus()
        self.wpm_label.set("Please type in the above to calculate your wpm")
        self.accuracy.set("Accuracy: 0.00%")

    def stop(self):
        self.start_time = float(0)
        self.timer_running = False
        self.entry.config(state="disabled")

    def generate_words(self, str_len):
        words = RandomWord().random_words(str_len, word_max_length=6)
        words = " ".join(words)
        self.target_text.set(words)


if __name__ == "__main__":
    app = App()
    TypingSpeedApp(app)
    app.mainloop()
