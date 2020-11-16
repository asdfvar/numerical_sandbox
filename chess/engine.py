#!/usr/bin/python3

class State:
   def __init__ (self):
      self.board = [[0 for ind in range (8)] for ind in range (8)]
      self.board[0] = ['R','N','B','Q','K','B','N','R']
      self.board[1] = ['P','P','P','P','P','P','P','P']
      self.board[6] = ['p','p','p','p','p','p','p','p']
      self.board[7] = ['r','n','b','q','k','b','n','r']
      self.Wcastle = False
      self.Bcastle = False

   def __str__ (self):
      display = ""
      for row in self.board[::-1]:
         display += str ((row))
         display += '\n'
      return display

   def white_moves (self, src):
      board = self.board
      moves = []
      row = src[0]
      col = src[1]
      piece = board[row][col]
      if piece == 'P':
         if row == 1 and board[row+2][col] == 0: moves += [(row+2, col)]
         if row < 7 and board[row+1][col] == 0: moves += [(row+1, col)]
         if row < 7 and col < 7 and str (board[row+1][col+1]) in 'prnbqk':
            moves += [(row+1, col+1)]
         if row < 7 and col > 0 and str (board[row+1][col-1]) in 'prnbqk':
            moves += [(row+1, col-1)]
      elif piece == 'N':
         if row + 2 < 8 and col + 1 < 8:
            if (str (board[row+2][col+1]) in '0pnbrqk'):
               moves += [(row+2, col+1)]
         if row + 2 < 8 and col - 1 >= 0:
            if (str (board[row+2][col-1]) in '0pnbrqk'):
               moves += [(row+2, col-1)]
         if row - 2 >= 0 and col + 1 < 8:
            if (str (board[row-2][col+1]) in '0pnbrqk'):
               moves += [(row-2, col+1)]
         if row - 2 >= 0 and col - 1 < 8:
            if (str (board[row-2][col-1]) in '0pnbrqk'):
               moves += [(row-2, col-1)]
         if row + 1 < 8 and col + 2 < 8:
            if (str (board[row+1][col+2]) in '0pnbrqk'):
               moves += [(row+1, col+2)]
         if row - 1 >= 0 and col + 2 < 8:
            if (str (board[row-1][col+2]) in '0pnbrqk'):
               moves += [(row-1, col+2)]
         if row + 1 < 8 and col - 2 >= 0:
            if (str (board[row+1][col-2]) in '0pnbrqk'):
               moves += [(row+1, col-2)]
         if row - 1 >= 0 and col - 2 >= 0:
            if (str (board[row-1][col-2]) in '0pnbrqk'):
               moves += [(row-1, col-2)]
      elif piece == 'B':
         if row < 7 and col < 7:
            step = 1
            while (row + step < 8 and col + step < 8 and str (board[row+step][col+step]) in '0pnbrqk'):
               moves += [(row+step, col+step)]
               step += 1
         if row > 0 and col > 0:
            step = 1
            while (row - step >= 0 and col - step >= 0 and str (board[row-step][col-step]) in '0pnbrqk'):
               moves += [(row-step, col-step)]
               step += 1
         if row < 7 and col > 0:
            step = 1
            while (row + step < 8 and col - step >= 0 and str (board[row+step][col-step]) in '0pnbrqk'):
               moves += [(row+step, col-step)]
               step += 1
         if row > 0 and col < 7:
            step = 1
            while (row - step >= 0 and col + step < 8 and str (board[row-step][col+step]) in '0pnbrqk'):
               moves += [(row-step, col+step)]
               step += 1
      elif piece == 'R':
         if row < 7:
            step = 1
            while (row + step < 8 and str (board[row+step][col]) in '0pnbrqk'):
               moves += [(row+step, col)]
               step += 1
         if row > 0:
            step = 1
            while (row - step >= 0 and str (board[row-step][col]) in '0pnbrqk'):
               moves += [(row-step, col)]
               step += 1
         if col < 7:
            step = 1
            while (col + step < 8 and str (board[row][col+step]) in '0pnbrqk'):
               moves += [(row, col+step)]
               step += 1
         if col > 0:
            step = 1
            while (col - step >= 0 and str (board[row][col-step]) in '0pnbrqk'):
               moves += [(row, col-step)]
               step += 1
      elif piece == 'Q':
         if row < 7:
            step = 1
            while (row + step < 8 and str (board[row+step][col]) in '0pnbrqk'):
               moves += [(row+step, col)]
               step += 1
         if row > 0:
            step = 1
            while (row - step >= 0 and str (board[row-step][col]) in '0pnbrqk'):
               moves += [(row-step, col)]
               step += 1
         if col < 7:
            step = 1
            while (col + step < 8 and str (board[row][col+step]) in '0pnbrqk'):
               moves += [(row, col+step)]
               step += 1
         if col > 0:
            step = 1
            while (col - step >= 0 and str (board[row][col-step]) in '0pnbrqk'):
               moves += [(row, col-step)]
               step += 1
         if row < 7 and col < 7:
            step = 1
            while (row + step < 8 and col + step < 8 and str (board[row+step][col+step]) in '0pnbrqk'):
               moves += [(row+step, col+step)]
               step += 1
         if row > 0 and col > 0:
            step = 1
            while (row - step >= 0 and col - step >= 0 and str (board[row-step][col-step]) in '0pnbrqk'):
               moves += [(row-step, col-step)]
               step += 1
         if row < 7 and col > 0:
            step = 1
            while (row + step < 8 and col - step >= 0 and str (board[row+step][col-step]) in '0pnbrqk'):
               moves += [(row+step, col-step)]
               step += 1
         if row > 0 and col < 7:
            step = 1
            while (row - step >= 0 and col + step < 8 and str (board[row-step][col+step]) in '0pnbrqk'):
               moves += [(row-step, col+step)]
               step += 1
      elif piece == 'K':
         if row + 1 < 8:
            if col + 1 < 8:
               if (str (board[row+1][col+1]) in '0pnbrqk'): moves += [(row+1, col+1)]
            if col - 1 >= 0:
               if (str (board[row+1][col-1]) in '0pnbrqk'): moves += [(row+1, col-1)]
            if (str (board[row+1][col]) in '0pnbrqk'): moves += [(row+1, col)]
         if col + 1 < 8:
            if (str (board[row][col+1]) in '0pnbrqk'): moves += [(row, col+1)]
         if col - 1 >= 0:
            if (str (board[row][col-1]) in '0pnbrqk'): moves += [(row, col-1)]
         if (str (board[row][col]) in '0pnbrqk'): moves += [(row, col)]
         if row - 1 >= 0:
            if col + 1 < 8:
               if (str (board[row-1][col+1]) in '0pnbrqk'): moves += [(row-1, col+1)]
            if col - 1 >= 0:
               if (str (board[row-1][col-1]) in '0pnbrqk'): moves += [(row-1, col-1)]
            if (str (board[row-1][col]) in '0pnbrqk'): moves += [(row-1, col)]
      return moves

   def black_moves (board, src):
      moves = []
      row = src[0]
      col = src[1]
      piece = board[row][col]
      if piece == 'p':
         if row == 6 and board[row-2][col] == 0: moves += [(row-2, col)]
         if row > 0 and board[row-1][col] == 0: moves += [(row-1, col)]
         if row > 0 and col < 7 and str (board[row-1][col+1]) in 'PRNBQK':
            moves += [(row-1, col+1)]
         if row > 0 and col > 0 and str (board[row-1][col-1]) in 'PRNBQK':
            moves += [(row-1, col-1)]
      elif piece == 'n':
         if row + 2 < 8 and col + 1 < 8:
            if (str (board[row+2][col+1]) in '0PNBRQK'):
               moves += [(row+2, col+1)]
         if row + 2 < 8 and col - 1 >= 0:
            if (str (board[row+2][col-1]) in '0PNBRQK'):
               moves += [(row+2, col-1)]
         if row - 2 >= 0 and col + 1 < 8:
            if (str (board[row-2][col+1]) in '0PNBRQK'):
               moves += [(row-2, col+1)]
         if row - 2 >= 0 and col - 1 < 8:
            if (str (board[row-2][col-1]) in '0PNBRQK'):
               moves += [(row-2, col-1)]
         if row + 1 < 8 and col + 2 < 8:
            if (str (board[row+1][col+2]) in '0PNBRQK'):
               moves += [(row+1, col+2)]
         if row - 1 >= 0 and col + 2 < 8:
            if (str (board[row-1][col+2]) in '0PNBRQK'):
               moves += [(row-1, col+2)]
         if row + 1 < 8 and col - 2 >= 0:
            if (str (board[row+1][col-2]) in '0PNBRQK'):
               moves += [(row+1, col-2)]
         if row - 1 >= 0 and col - 2 >= 0:
            if (str (board[row-1][col-2]) in '0PNBRQK'):
               moves += [(row-1, col-2)]
      elif piece == 'b':
         if row < 7 and col < 7:
            step = 1
            while (row + step < 8 and col + step < 8 and str (board[row+step][col+step]) in '0PNBRQK'):
               moves += [(row+step, col+step)]
               step += 1
         if row > 0 and col > 0:
            step = 1
            while (row - step >= 0 and col - step >= 0 and str (board[row-step][col-step]) in '0PNBRQK'):
               moves += [(row-step, col-step)]
               step += 1
         if row < 7 and col > 0:
            step = 1
            while (row + step < 8 and col - step >= 0 and str (board[row+step][col-step]) in '0PNBRQK'):
               moves += [(row+step, col-step)]
               step += 1
         if row > 0 and col < 7:
            step = 1
            while (row - step >= 0 and col + step < 8 and str (board[row-step][col+step]) in '0PNBRQK'):
               moves += [(row-step, col+step)]
               step += 1
      elif piece == 'r':
         if row < 7:
            step = 1
            while (row + step < 8 and str (board[row+step][col]) in '0PNBRQK'):
               moves += [(row+step, col)]
               step += 1
         if row > 0:
            step = 1
            while (row - step >= 0 and str (board[row-step][col]) in '0PNBRQK'):
               moves += [(row-step, col)]
               step += 1
         if col < 7:
            step = 1
            while (col + step < 8 and str (board[row][col+step]) in '0PNBRQK'):
               moves += [(row, col+step)]
               step += 1
         if col > 0:
            step = 1
            while (col - step >= 0 and str (board[row][col-step]) in '0PNBRQK'):
               moves += [(row, col-step)]
               step += 1
      elif piece == 'q':
         if row < 7:
            step = 1
            while (row + step < 8 and str (board[row+step][col]) in '0PNBRQK'):
               moves += [(row+step, col)]
               step += 1
         if row > 0:
            step = 1
            while (row - step >= 0 and str (board[row-step][col]) in '0PNBRQK'):
               moves += [(row-step, col)]
               step += 1
         if col < 7:
            step = 1
            while (col + step < 8 and str (board[row][col+step]) in '0PNBRQK'):
               moves += [(row, col+step)]
               step += 1
         if col > 0:
            step = 1
            while (col - step >= 0 and str (board[row][col-step]) in '0PNBRQK'):
               moves += [(row, col-step)]
               step += 1
         if row < 7 and col < 7:
            step = 1
            while (row + step < 8 and col + step < 8 and str (board[row+step][col+step]) in '0PNBRQK'):
               moves += [(row+step, col+step)]
               step += 1
         if row > 0 and col > 0:
            step = 1
            while (row - step >= 0 and col - step >= 0 and str (board[row-step][col-step]) in '0PNBRQK'):
               moves += [(row-step, col-step)]
               step += 1
         if row < 7 and col > 0:
            step = 1
            while (row + step < 8 and col - step >= 0 and str (board[row+step][col-step]) in '0PNBRQK'):
               moves += [(row+step, col-step)]
               step += 1
         if row > 0 and col < 7:
            step = 1
            while (row - step >= 0 and col + step < 8 and str (board[row-step][col+step]) in '0PNBRQK'):
               moves += [(row-step, col+step)]
               step += 1
      elif piece == 'k':
         if row + 1 < 8:
            if col + 1 < 8:
               if (str (board[row+1][col+1]) in '0PNBRQK'): moves += [(row+1, col+1)]
            if col - 1 >= 0:
               if (str (board[row+1][col-1]) in '0PNBRQK'): moves += [(row+1, col-1)]
            if (str (board[row+1][col]) in '0PNBRQK'): moves += [(row+1, col)]
         if col + 1 < 8:
            if (str (board[row][col+1]) in '0PNBRQK'): moves += [(row, col+1)]
         if col - 1 >= 0:
            if (str (board[row][col-1]) in '0PNBRQK'): moves += [(row, col-1)]
         if (str (board[row][col]) in '0PNBRQK'): moves += [(row, col)]
         if row - 1 >= 0:
            if col + 1 < 8:
               if (str (board[row-1][col+1]) in '0PNBRQK'): moves += [(row-1, col+1)]
            if col - 1 >= 0:
               if (str (board[row-1][col-1]) in '0PNBRQK'): moves += [(row-1, col-1)]
            if (str (board[row-1][col]) in '0PNBRQK'): moves += [(row-1, col)]
      return moves

   def all_white_moves (self):
      board = self.board
      moves = {}
      keys = []
      for row in range (8):
         for col in range (8):
            lmoves = self.white_moves ((row, col))
            if len (lmoves) > 0:
               moves[(row, col)] = lmoves
               keys.append ((row, col))
      return keys, moves

   def all_black_moves (self):
      board = self.board
      moves = {}
      keys = []
      for row in range (8):
         for col in range (8):
            lmoves = self.black_moves ((row, col))
            if len (lmoves) > 0:
               moves[(row, col)] = lmoves
               keys.append ((row, col))
      return keys, moves

   def move (self, src, dst):
      board = self.board
      board[dst[0]][dst[1]] = board[src[0]][src[1]]
      board[src[0]][src[1]] = 0

   def analyze (self):
      pass
