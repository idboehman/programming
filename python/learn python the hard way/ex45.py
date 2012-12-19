# Exercise 45: You Make A Game
# Game: Battleship!
# Based on an exercise completed at CodeAcademy

from random import randint # used for random number generation


class Board(object):
    
    def initBoard(self):
        """Creates a 5x5 game board"""
        board = []
        for x in range(0,5):
            board.append(['O'] * 5)
        return board

    def printBoard(self, board):
        """Prints the board in a more visually appealing manner"""
        for row in board:
            print ' '.join(row)
        print "\n"

    def inRange(self, board, guess_row, guess_col):
        if (guess_row < 1 or guess_col < 1 or
            guess_row > len(board) or 
            guess_col > len(board[0])):
           return False
        else:
            return True
 
    def sameGuess(self, board, guess_row, guess_col):
        if board[guess_row - 1][guess_col - 1] == "X":
           return True 
        

class Ship(object):
#row =
    ''' 
    def __init__(self, row=None, col=None, board):
        """Generates a random spot on the board to place the ship"""
        self.row = row if row is not None else self.randomRow(board)
        self.col = col if col is not None else self.randomCol(board)
        #self.row = self.random_row(Board.board())
        #self.col = self.random_col(Board.board())
    ''' 

    def randomRow(self, board):
        """Returns a random row on the board"""
        # Number between 0 and len of board - 1 (b/c arrays start at 0)
        return randint(0, len(board) - 1)
    def randomCol(self, board):
        """Returns a random column on the board"""
        # since a board is a list of rows, generating a random num
        # between 0 and the len of board[0] - 1 generates a number
        # associated w/ an element of the top row, or a col num
        return randint(0, len(board[0]) - 1)

class Game(object):
    board = Board().initBoard()
    ship = Ship()
    ship.row = ship.randomRow(board)
    ship.col = ship.randomCol(board)

    def __init__(self, turns=None):
        # game board to play on, a Game has-a board
        #self.board = board
        #self.ship = ship    # ship to place on board, a Game has-a ship
        self.turns = turns if turns is not None else 5 # a game lasts 5 turns

    def play(self):
        print "Let's play Battleship!"
        print "Here's the board:\n"
        #print self.ship.row
        #print self.ship.col
        #print "\n"
        Board().printBoard(self.board)
        print "You have " + str(self.turns) + " guesses"
        print self.ship.row, self.ship.col

        for turn in range(self.turns):
            print "Guess number", turn+1
            left = str(self.turns - (turn + 1))
            guess_row = int(raw_input("Guess Row: "))
            guess_col = int(raw_input("Guess Column: "))

            if (guess_row == self.ship.row and
                guess_col == self.ship.col):
                print 'Congratulations! You sunk my battleship!'
                print 'You win!'
                self.board[guess_row - 1][guess_col - 1] = "&"
                Board().printBoard(self.board)
                break
            elif not (Board().inRange(self.board, guess_row, guess_col)):
                print "Oops, that's not even in the ocean!",
                print "\nPlease try again, this time guessing",
                print "between 1 and 5"
                print "You have " + left + " turns remaining\n"
            elif Board().sameGuess(self.board, guess_row, guess_col):
                print "You've guessed that already silly!"
                print "You have " + left + " turns remaining\n"
            else:
                print 'You missed my battleship!'
                self.board[guess_row - 1][guess_col - 1] = "X"
                print "You have " + left + " turns remaining\n"
            Board().printBoard(self.board)

a_game = Game()
a_game.play()
