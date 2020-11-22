import numpy as np
from numpy import linalg as la
import copy
import white_moves
import black_moves

class State:
   def __init__ (self):
      self.board = [[0 for ind in range (8)] for ind in range (8)]
      self.board[0] = ['R','N','B','Q','K','B','N','R']
      self.board[1] = ['P','P','P','P','P','P','P','P']
      self.board[6] = ['p','p','p','p','p','p','p','p']
      self.board[7] = ['r','n','b','q','k','b','n','r']
      self.wCastleAvailOO  = True
      self.wCastleAvailOOO = True
      self.bCastleAvailOO  = True
      self.bCastleAvailOOO = True
      self.en_passant = None

      # Weights assigned to [[PNBRQK], [pnbrqk]] respectively
      self.weights = np.array ([[ 0.1,  0.7,  0.4,  0.3,  0.9,  0.0],
                                [-0.1, -0.7, -0.4, -0.3, -0.9, -0.0]])

   def __str__ (self):
      display = "+---+---+---+---+---+---+---+---+\n"
      for row in self.board[::-1]:
         for col in row:
            if col == 0:
               display += "|   "
            else:
               display += "| " + str (col) + " "
         display += "|\n+---+---+---+---+---+---+---+---+\n"
      return display

   def assess (self):
      wpieces  = ('P','N','B','R','Q','K')
      bpieces  = ('p','n','b','r','q','k')
      on_board = np.zeros ((2, 6))

      for row in self.board:
         for element in row:
            for ind, piece in enumerate (wpieces):
               if piece == element: on_board[0][ind] += 1
            for ind, piece in enumerate (bpieces):
               if piece == element: on_board[1][ind] += 1

      value = 0.0
      value += np.dot (on_board[0], self.weights[0])
      value += np.dot (on_board[1], self.weights[1])

      if on_board[0, 5] == 0: value = -np.inf
      if on_board[1, 5] == 0: value =  np.inf
      
      return value

   def copy (self):
      return copy.deepcopy (self)
