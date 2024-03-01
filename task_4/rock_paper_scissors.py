'''
   Mpho Aphane                           0 0
   mpho4phane@gmail.com                  ._.       rock_paper_scissors.
'''

import random
import tkinter
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")

        self.user_score = 0
        self.computer_score = 0
        self.root.geometry("250x200")
        
        self.user_label = tkinter.Label(root, text="Your Choice:", font=('Arial', 10))
        self.user_label.pack()

        self.user_choice_label = tkinter.Label(root, text="", font=('Arial', 10))
        self.user_choice_label.pack()

        self.computer_label = tkinter.Label(root, text="Computer's Choice:", font=('Arial', 10))
        self.computer_label.pack()

        self.computer_choice_label = tkinter.Label(root, text="", font=('Arial', 10))
        self.computer_choice_label.pack()

        self.result_label = tkinter.Label(root, text="", font=('Arial', 10, 'bold'))
        self.result_label.pack()

        self.score_label = tkinter.Label(root, text="", font=('Arial', 10))
        self.score_label.pack()
        
        self.rock_button = ttk.Button(root, text="Rock", bootstyle="warning-outline", command=lambda: self.play_round("rock"))
        self.rock_button.pack(side=LEFT, fill=X, anchor=CENTER)
        ToolTip(self.rock_button, text="Wins against Scissors")

        self.rock_button = ttk.Button(root, text="Paper", bootstyle="secondary-outline", command=lambda: self.play_round("paper"))
        self.rock_button.pack(side=LEFT, fill=X, anchor=CENTER)
        ToolTip(self.rock_button, text="Wins against Rock")

        self.rock_button = ttk.Button(root, text="Scissors", bootstyle="dark-outline", command=lambda: self.play_round("scissors"))
        self.rock_button.pack(side=LEFT, fill=X, anchor=CENTER)
        ToolTip(self.rock_button, text="Wins against Paper")

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'It\'s a tie!'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_score += 1
            return 'You win!'
        else:
            self.computer_score += 1
            return 'You lose!'

    def update_labels(self, user_choice, computer_choice, result):
        self.user_choice_label.config(text=user_choice.capitalize())
        self.computer_choice_label.config(text=computer_choice.capitalize())
        color = 'black'
        if result == 'You win!': color = 'green'
        elif result == 'You lose!': color = 'red'
        self.result_label.config(text=result, fg=color)
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

    def play_round(self, user_choice):
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        self.update_labels(user_choice, computer_choice, result)


if __name__ == "__main__":
   root = tkinter.Tk()
   game = RockPaperScissors(root)
   root.mainloop()
