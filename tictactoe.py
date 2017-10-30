# Simple Tic-Tac-Toe example
# File: weaktictactoe2.py
# Base on code from http://www.summet.com/dmsi/html/guiProgramming.html
# Python 3.2
# www.ocf.berkeley.edu/~yosenl/extras/alphabeta/alphabeta.html

from tkinter import *
from tkinter.messagebox import showwarning

#We define a TTT class here:
class TTT():
    # It has an object variable called "board" that remembers
    # who has made what moves. We use a 9 element long 1D data structure
    # to make calculations easier. On-Screen, it's represented with a 3x3
    # grid.
    # "Postion of board: "
    # "0 | 1 | 2"
    # "3 | 4 | 5"
    # "6 | 7 | 8"
    board = [ "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]


    #This is the constructor. It draws the window with the 9 buttons.
    def __init__(self, tkMainWin):
        frame = Frame(tkMainWin)
        frame.pack()

        self.B00 = Button(frame)
        self.B00.bind("<ButtonRelease-1>", self.clicked)
        self.B00.grid(row=0,column=0)

        self.B01 = Button(frame)
        self.B01.bind("<ButtonRelease-1>", self.clicked)
        self.B01.grid(row=0, column=1)

        self.B02 = Button(frame)
        self.B02.bind("<ButtonRelease-1>", self.clicked)
        self.B02.grid(row=0, column=2)

        self.B10 = Button(frame)
        self.B10.bind("<ButtonRelease-1>", self.clicked)
        self.B10.grid(row=1,column=0)
        
        self.B11 = Button(frame)
        self.B11.bind("<ButtonRelease-1>", self.clicked)
        self.B11.grid(row=1, column=1)

        self.B12 = Button(frame)
        self.B12.bind("<ButtonRelease-1>", self.clicked)
        self.B12.grid(row=1, column=2)

        self.B20 = Button(frame)
        self.B20.bind("<ButtonRelease-1>", self.clicked)
        self.B20.grid(row=2,column=0)

        self.B21 = Button(frame)
        self.B21.bind("<ButtonRelease-1>", self.clicked)
        self.B21.grid(row=2,column=1)
        
        self.B22 = Button(frame)
        self.B22.bind("<ButtonRelease-1>", self.clicked)
        self.B22.grid(row=2,column=2)
        self.message = Button(frame)
        self.message.grid(row=0,column=3)
        self.label="Click a Square to Begin"
        
        # Set the text for each of the 9 buttons. 
        # Initially, to all Blanks!
        self.clear = Button(frame)
        self.clear.bind("<ButtonRelease-1>", self.clicked)
        self.clear.grid(row=2,column=3)
        self.redrawBoard()

    #This event handler (callback) will figure out which of the 9 buttons
    #were clicked, and call the "userMove" method with that move position.
    def clicked(self, event):
        if event.widget == self.B00:
            self.userMove(0)
        if event.widget == self.B01 :
            self.userMove(1)
        if event.widget == self.B02 :
            self.userMove(2)
        if event.widget == self.B10 :
            self.userMove(3)
        if event.widget == self.B11:
            self.userMove(4)
        if event.widget == self.B12 :
            self.userMove(5)
        if event.widget == self.B20 :
            self.userMove(6)
        if event.widget == self.B21 :
            self.userMove(7)
        if event.widget == self.B22 :
            self.userMove(8)
        if event.widget == self.clear :
            self.board = [ "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
            self.label="Click a Square to Begin"
            self.redrawBoard()

    def userWon(self, board=None):
        if board is None:
            board = self.board
        #see computerWon if this does not make sense
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for i,j,k in wins:
            if board[i] == board[j] == board[k] =="X": 
                return True
        return False
    
    def computerWon(self, board=None):
        if board is None:
            board = self.board
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for i,j,k in wins:
            if board[i] == board[j] == board[k] =="O": 
                return True
        return False
            
            
    #When a button signals that the user has tried to make a move by
    # clicking, we check to see if that move is valid. If it is, we
    # need to check to see if the user has won. If they have not, we
    # need to make our move, and check to see if the computer has won.
    # We also redraw the board after each move.
    def userMove(self, pos):
        #Is this a valid move?
        if self.board[pos] == "  ":
            #Record the players move...
            self.board[pos] = "X"
            #Then redraw the board!
            self.redrawBoard()
            
            #Check to see if the user won!
            if self.userWon():
                self.label= "Human Won"
            
            #Make computer move!
            self.computerMove()

            #Check to see if the computer won!
            if self.computerWon():
                self.label= "Computer Won"

            #Then redraw the board!
            self.redrawBoard()
            
        else:   #Move is NOT valid! Don't do anything!
            
            showwarning("Invalid Move", "I'm sorry, that move is not valid!")
            

    # TODO: Make computer move smarter!
    # This method will make a move for the computer.
    # It is VERY simplistic, as it just picks the first
    # valid move from an ordered list of preferred moves.
    def computerMove(self):
        #for move in [4, 0, 2, 6, 8, 1, 3, 5, 7]:
            #if self.board[move] == "  ":
                #self.board[move] = "O"
                #return
        self._bestMove = -1
        self._minimax("O", list(self.board))
        print (self._bestMove, self.board)
        if self._bestMove > -1:
            self.board[self._bestMove] = "O"
        else:
            for i,val in enumerate(self.board):
                if val == "  ":
                    self.board[i] = "O"
                    break

    def _minimax(self, player, board):
        if self.userWon(board):
            return "X"
        elif self.computerWon(board):
            return "O"
        elif self._isTie(board):
            return "  "

        # collect the possible moves
        moves = []
        for i,val in enumerate(board):
            if val == "  ":
                moves.append(i)
	
        # for each possible move
        for move in moves:
            # duplicate the board and make the move
            newBoard = list(board)
            newBoard[move] = player

            if player == "O":
                if self._minimax("X", newBoard) == "O":
                    self._bestMove = move
            else:
                if self._minimax("O", newBoard) == "X":
                    self._bestMove = move
    '''

    def _max(self, player, board):
        bestScore = None
        bestMove = None
        moves = self._possibleMoves(board)

        for m in moves:
            # duplicate the board and make the move
            newBoard = list(board)
            newBoard[m] = player
            
            if self._gameOver(newBoard):
                score = self._scoreBoard(newBoard)
            else:
                move,score = self._min(player, newBoard)

            if bestScore == None or score > bestScore:
                bestScore = score
                bestMove = m
        return (bestMove, bestScore)

    def _min(self, player, board):
        bestScore = None
        bestMove = None
        moves = self._possibleMoves(board)

        for m in moves:
            # duplicate the board and make the move
            newBoard = list(board)
            newBoard[m] = player
            
            if self._gameOver(newBoard):
                score = self._scoreBoard(newBoard)
            else:
                move,score = self._max(player, newBoard)

            if bestScore == None or score < bestScore:
                bestScore = score
                bestMove = m
        return (bestMove, bestScore)

    def _possibleMoves(self, board):
        moves = []
        for i,val in enumerate(board):
            if val == "  ":
                moves.append(i)
        return moves
        
    def _gameOver(self, board):
        if self.userWon(board) or self.computerWon(board) or self._isTie(board):
            return True
        return False

    def _scoreBoard(self, board):
        if self.userWon(board):
            return -1
        elif self.computerWon(board):
            return 1
        return 0
    '''

    def _isTie(self, board):
        for i in board:
            if i == "  ":
                return False
        return True


    #This method will update the text displayed by
    # each of the 9 buttons to reflect the "board"
    # object variable.
    def redrawBoard(self):
        self.B00.config( text = self.board[0])
        self.B01.config( text = self.board[1])
        self.B02.config( text = self.board[2])
        self.B10.config( text = self.board[3])
        self.B11.config( text = self.board[4])
        self.B12.config( text = self.board[5])
        self.B20.config( text = self.board[6])
        self.B21.config( text = self.board[7])
        self.B22.config( text = self.board[8])
        self.message.config( text = self.label)
        self.clear.config( text = "Clear Board")

#This code starts up TK and creates a main window.
mainWin = Tk()

#This code creates an instance of the TTT object.
ttt = TTT( mainWin)

#This line starts the main event handling loop and sets us on our way...
mainWin.mainloop()
