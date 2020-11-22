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

   def copy (self):
      return copy.deepcopy (self)
