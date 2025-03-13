import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("350x250")
        
        self.secret_number = random.randint(1, 100)
        self.total_chances = 5
        self.chances_left = self.total_chances
        
        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)
        
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)
        
        self.chances_label = tk.Label(master, text=f"Chances left: {self.chances_left}")
        self.chances_label.pack(pady=5)
        
        self.reset_button = tk.Button(master, text="Restart Game", command=self.reset_game)
        self.reset_button.pack(pady=5)
    
    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            
            if user_guess < 1 or user_guess > 100:
                messagebox.showwarning("Warning", "Please enter a number between 1 and 100.")
                return
            
            self.chances_left -= 1
            self.chances_label.config(text=f"Chances left: {self.chances_left}")
            
            if user_guess == self.secret_number:
                messagebox.showinfo("Result", f"Congratulations! You guessed the correct number: {self.secret_number}\nYou won with {self.chances_left} chances remaining!")
                self.reset_game()
            elif self.chances_left == 0:
                messagebox.showinfo("Game Over", f"Game over! The number was {self.secret_number}.")
                self.reset_game()
            elif user_guess < self.secret_number:
                messagebox.showinfo("Result", "Too low! Try a higher number.")
            else:
                messagebox.showinfo("Result", "Too high! Try a lower number.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number between 1 and 100.")
    
    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.chances_left = self.total_chances
        self.chances_label.config(text=f"Chances left: {self.chances_left}")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
