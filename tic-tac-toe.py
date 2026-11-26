# Question
# Implement a Tic-Tac-Toe game for an n x n board that can determine the winner after each move.

# You need to create a TicTacToe class with two methods:

# TicTacToe(int n): Initializes a game board of size n x n

# int move(int row, int col, int player): Places a mark for the given player (1 or 2)
# at position (row, col) and returns:
# 0 if there's no winner yet
# 1 if player 1 wins
# 2 if player 2 wins

# A player wins when they successfully place n of their marks in:
# Any complete row
# Any complete column
# The main diagonal (from top-left to bottom-right)
# The anti-diagonal (from top-right to bottom-left)

class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0

    def move(self, row, col, player):
        d = 1 if player == 1 else -1
        n = self.n
        self.rows[row] += d
        self.cols[col] += d
        if row == col:      self.diag += d
        if row + col == n-1: self.anti += d
        if (abs(self.rows[row]) == n or abs(self.cols[col]) == n
                or abs(self.diag) == n or abs(self.anti) == n):
            return player
        return 0