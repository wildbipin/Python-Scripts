import random
import tkinter as tk
from tkinter import messagebox

# Returns list of digits of a number 
def getDigits(num):
    return [int(i) for i in str(num)]

# Returns True if number has no duplicate digits, otherwise False
def noDuplicates(num):
    num_li = getDigits(num)
    return len(num_li) == len(set(num_li))

# Generates a 4 digit number with no repeated digits
def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num

# Returns common digits with exact matches (bulls) and the common digits in wrong position (cows)
def numOfBullsCows(num, guess):
    bull_cow = [0, 0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)

    for i, j in zip(num_li, guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1

    return bull_cow

# Main game class
class CowsAndBullsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Cows and Bulls Game")

        self.secret_num = generateNum()
        self.tries = 0

        self.label = tk.Label(master, text="Enter number of tries:")
        self.label.pack()

        self.tries_entry = tk.Entry(master)
        self.tries_entry.pack()

        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.guess_label = tk.Label(master, text="Enter your guess:")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        self.submit_button = tk.Button(master, text="Submit Guess", command=self.submit_guess)
        self.submit_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.pack()

        self.history_label = tk.Label(master, text="Guess History:")
        self.history_label.pack()

        self.history_text = tk.Text(master, height=10, width=50)
        self.history_text.pack()
        self.history_text.config(state=tk.DISABLED)

    def start_game(self):
        try:
            self.tries = int(self.tries_entry.get())
            if self.tries <= 0:
                raise ValueError
            self.tries_entry.config(state=tk.DISABLED)
            self.start_button.config(state=tk.DISABLED)
            self.result_label.config(text=f"Game started! You have {self.tries} tries.")
            self.history_text.config(state=tk.NORMAL)
            self.history_text.delete(1.0, tk.END)
            self.history_text.config(state=tk.DISABLED)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of tries.")

    def submit_guess(self):
        if self.tries <= 0:
            messagebox.showinfo("Game Over", "You have no more tries left.")
            return

        try:
            guess = int(self.guess_entry.get())
            if not noDuplicates(guess):
                raise ValueError("Number should not have repeated digits.")
            if guess < 1000 or guess > 9999:
                raise ValueError("Enter a 4 digit number only.")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
            return

        bull_cow = numOfBullsCows(self.secret_num, guess)
        self.tries -= 1
        self.result_label.config(text=f"{bull_cow[0]} bulls, {bull_cow[1]} cows\nTries left: {self.tries}")

        self.history_text.config(state=tk.NORMAL)
        self.history_text.insert(tk.END, f"Guess: {guess}, {bull_cow[0]} bulls, {bull_cow[1]} cows\n")
        self.history_text.config(state=tk.DISABLED)

        if bull_cow[0] == 4:
            messagebox.showinfo("Congratulations!", "You guessed right!")
            self.reset_game()
        elif self.tries == 0:
            messagebox.showinfo("Game Over", f"You ran out of tries. The number was {self.secret_num}")
            self.reset_game()

    def reset_game(self):
        self.secret_num = generateNum()
        self.tries = 0
        self.tries_entry.config(state=tk.NORMAL)
        self.tries_entry.delete(0, tk.END)
        self.start_button.config(state=tk.NORMAL)
        self.guess_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        self.history_text.config(state=tk.DISABLED)
        messagebox.showinfo("Game Reset", "The game has been reset.")

# Create the Tkinter window
root = tk.Tk()
game = CowsAndBullsGame(root)
root.mainloop()
