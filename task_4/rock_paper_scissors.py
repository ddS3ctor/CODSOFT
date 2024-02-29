'''
   Mpho Aphane                           0 0
   mpho4phane@gmail.com                  ._.       rock_paper_scissors.
'''

import tkinter
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")

        self.user_score = 0
        self.computer_score = 0

        self.user_label = tkinter.Label(root, text="Your Choice:", font=('Arial', 14))
        self.user_label.grid(row=0, column=0)

        self.user_choice_label = tkinter.Label(root, text="", font=('Arial', 14))
        self.user_choice_label.grid(row=0, column=1)

        self.computer_label = tkinter.Label(root, text="Computer's Choice:", font=('Arial', 14))
        self.computer_label.grid(row=1, column=0)

        self.computer_choice_label = tkinter.Label(root, text="", font=('Arial', 14))
        self.computer_choice_label.grid(row=1, column=1)

        self.result_label = tkinter.Label(root, text="", font=('Arial', 14))
        self.result_label.grid(row=2, columnspan=2)

        self.score_label = tkinter.Label(root, text="", font=('Arial', 14))
        self.score_label.grid(row=3, columnspan=2)

        self.rock_button = tkinter.Button(root, text="Rock", font=('Arial', 14), command=lambda: self.play_round("rock"))
        self.rock_button.grid(row=4, column=0)

        self.paper_button = tkinter.Button(root, text="Paper", font=('Arial', 14), command=lambda: self.play_round("paper"))
        self.paper_button.grid(row=4, column=1)

        self.scissors_button = tkinter.Button(root, text="Scissors", font=('Arial', 14), command=lambda: self.play_round("scissors"))
        self.scissors_button.grid(row=5, column=0, columnspan=2)

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
        self.result_label.config(text=result)
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

    def play_round(self, user_choice):
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        self.update_labels(user_choice, computer_choice, result)


if __name__ == "__main__":
   root = tkinter.Tk()
   game = RockPaperScissors(root)
   root.mainloop()
