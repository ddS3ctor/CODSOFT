'''
   Mpho Aphane                          -0~0-
   mpho4phane@gmail.com                  ._.       unittests/rock_paper_scissors.
'''

import unittest
import tkinter
from io import StringIO
from unittest.mock import patch
import task_4.rock_paper_scissors as rps

class TestTask4(unittest.TestCase):
    def test_win(self):
        root = tkinter.Tk()
        game = rps.RockPaperScissors(root)

        expected = 'You win!'
        computer_choice = 'scissors'
        user_choice = 'rock'
        return_value = game.determine_winner(user_choice, computer_choice)
        self.assertEqual(expected, return_value)

        computer_choice = 'paper'
        user_choice = 'scissors'
        return_value = game.determine_winner(user_choice, computer_choice)
        self.assertEqual(expected, return_value)

        computer_choice = 'rock'
        user_choice = 'paper'
        return_value = game.determine_winner(user_choice, computer_choice)
        self.assertEqual(expected, return_value)


    def test_lose(self):
        root = tkinter.Tk()
        game = rps.RockPaperScissors(root)

        expected = 'You lose!'
        computer_choice = 'scissors'
        user_choice = 'paper'
        return_value = game.determine_winner(user_choice, computer_choice)
        self.assertEqual(expected, return_value)

        root = tkinter.Tk()
        game = rps.RockPaperScissors(root)

        expected = 'You lose!'
        computer_choice = 'paper'
        user_choice = 'rock'
        return_value = game.determine_winner(user_choice, computer_choice)
        self.assertEqual(expected, return_value)

        root = tkinter.Tk()
        game = rps.RockPaperScissors(root)

        expected = 'You lose!'
        computer_choice = 'rock'
        user_choice = 'scissors'
        return_value = game.determine_winner(user_choice, computer_choice)
        self.assertEqual(expected, return_value)

    def test_tie(self):
        root = tkinter.Tk()
        game = rps.RockPaperScissors(root)

        expected = 'It\'s a tie!'
        computer_choice = 'rock'
        user_choice = 'rock'
        return_value = game.determine_winner(user_choice, computer_choice)
        self.assertEqual(expected, return_value)

        expected = 'It\'s a tie!'
        computer_choice = 'paper'
        user_choice = 'paper'
        return_value = game.determine_winner(user_choice, computer_choice)
        self.assertEqual(expected, return_value)

        expected = 'It\'s a tie!'
        computer_choice = 'scissors'
        user_choice = 'scissors'
        return_value = game.determine_winner(user_choice, computer_choice)
        self.assertEqual(expected, return_value)


    def test_user_score(self):
        root = tkinter.Tk()
        game = rps.RockPaperScissors(root)
        expected = 0
        user_score = game.user_score
        self.assertEqual(expected, user_score)

        expected = 1
        computer_choice = 'scissors'
        user_choice = 'rock'
        game.determine_winner(user_choice, computer_choice)
        user_score = game.user_score
        self.assertEqual(expected, user_score)


    def test_computer_score(self):
        root = tkinter.Tk()
        game = rps.RockPaperScissors(root)
        expected = 0
        computer_score = game.computer_score
        self.assertEqual(expected, computer_score)

        expected = 1
        computer_choice = 'paper'
        user_choice = 'rock'
        game.determine_winner(user_choice, computer_choice)
        computer_score = game.computer_score
        self.assertEqual(expected, computer_score)


if __name__ == '__main__':
    unittest.main()