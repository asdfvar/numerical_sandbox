#!/usr/bin/python3

class Kernel:
   def __init__ (self):
      self.board = [[0 for ind in range (8)] for ind in range (8)]
      self.board[0] = ['R','N','B','Q','K','B','N','R']
      self.board[1] = ['P','P','P','P','P','P','P','P']
      self.board[6] = ['p','p','p','p','p','p','p','p']
      self.board[7] = ['r','n','b','q','k','b','n','r']
      self.White_has_castle_OO  = True
      self.White_has_castle_OOO = True
      self.Black_has_castle_OO  = True
      self.Black_has_castle_OOO = True
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
         if self.White_has_castle_OO:
            if board[0][5] == board[0][6] == 0:
               keys, allmoves = self.all_black_moves ()
               valid = True
               for piece_moves in allmoves:
                  for lmove in piece_moves:
                     if lmove == (0, 5): valid = False
                     if lmove == (0, 6): valid = False
               if valid: moves += ['O-O']
         if self.White_has_castle_OOO:
            if board[0][2] == board[0][3] == 0:
               keys, allmoves = self.all_black_moves ()
               valid = True
               for piece_moves in allmoves:
                  for lmove in piece_moves:
                     if lmove == (0, 2): valid = False
                     if lmove == (0, 3): valid = False
               if valid: moves += ['O-O-O']
      return moves

   def black_moves (self, src):
      board = self.board
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
         if self.Black_has_castle_OO:
            if board[7][5] == board[7][6] == 0:
               keys, allmoves = self.all_white_moves ()
               valid = True
               for piece_moves in allmoves:
                  for lmove in piece_moves:
                     if lmove == (7, 5): valid = False
                     if lmove == (7, 6): valid = False
               if valid: moves += ['O-O']
         if self.Black_has_castle_OOO:
            if board[7][2] == board[7][3] == 0:
               keys, allmoves = self.all_white_moves ()
               valid = True
               for piece_moves in allmoves:
                  for lmove in piece_moves:
                     if lmove == (7, 2): valid = False
                     if lmove == (7, 3): valid = False
               if valid: moves += ['O-O-O']
      return moves

   def all_white_moves (self):
      moves = []
      keys  = []
      for row in range (8):
         for col in range (8):
            lmoves = self.white_moves ((row, col))
            if len (lmoves) > 0:
               moves.append (lmoves)
               keys.append ((row, col))
      return keys, moves

   def all_black_moves (self):
      moves = []
      keys  = []
      for row in range (8):
         for col in range (8):
            lmoves = self.black_moves ((row, col))
            if len (lmoves) > 0:
               moves.append (lmoves)
               keys.append ((row, col))
      return keys, moves

   def move_white (self, src, dst):
      board = self.board
      legal_moves = self.white_moves (src)

      valid = False
      if len (legal_moves) > 0:
         for key in legal_moves:
            if dst == key: valid = True
      if not (valid):
         print ("illegal move " + str (src) + " -> " + str (dst))
         return

      # Perform castling
      if dst == 'O-O':
         board[0][6] = 'K'
         board[0][5] = 'R'
         board[0][4] = 0
         board[0][7] = 0
         return
      elif dst == 'O-O-O':
         board[0][2] = 'K'
         board[0][3] = 'R'
         board[0][4] = 0
         board[0][0] = 0
         return

      # Disable castling if the condition is met
      if (src[0], src[1]) == (0, 0) and board[src[0]][src[1]] == 'R':
         self.White_has_castle_OOO = False
      elif (src[0], src[1]) == (0, 7) and board[src[0]][src[1]] == 'R':
         self.White_has_castle_OO = False
      if board[src[0]][src[1]] == 'K':
         self.White_has_castle_OO  = False
         self.White_has_castle_OOO = False

      # Perform a generic move
      board[dst[0]][dst[1]] = board[src[0]][src[1]]
      board[src[0]][src[1]] = 0

      # Set the en passant flag if the condition is met
      self.en_passant = None
      if board[dst[0]][dst[1]] == 'P' and src[0] == 1 and dst[0] == 3:
         if dst[1] < 7 and board[dst[0]][dst[1]+1] == 'p':
            self.en_passant = (2, src[1])
         if dst[1] > 0 and board[dst[0]][dst[1]-1] == 'p':
            self.en_passant = (2, src[1])

   def move_black (self, src, dst):
      board = self.board
      legal_moves = self.black_moves (src)

      valid = False
      if len (legal_moves) > 0:
         for key in legal_moves:
            if dst == key: valid = True
      if not (valid):
         print ("illegal move " + str (src) + " -> " + str (dst))
         return

      # Perform castling
      if dst == 'O-O':
         board[7][6] = 'k'
         board[7][5] = 'r'
         board[7][4] = 0
         board[7][7] = 0
         return
      elif dst == 'O-O-O':
         board[7][2] = 'k'
         board[7][3] = 'r'
         board[7][4] = 0
         board[7][0] = 0
         return

      # Disable castling if the condition is met
      if (src[0], src[1]) == (7, 0) and board[src[0]][src[1]] == 'r':
         self.White_has_castle_OOO = False
      elif (src[0], src[1]) == (7, 7) and board[src[0]][src[1]] == 'r':
         self.White_has_castle_OO = False
      if board[src[0]][src[1]] == 'k':
         self.White_has_castle_OO  = False
         self.White_has_castle_OOO = False

      # Perform a generic move
      board[dst[0]][dst[1]] = board[src[0]][src[1]]
      board[src[0]][src[1]] = 0

      # Set the en passant flag if the condition is met
      self.en_passant = None
      if board[dst[0]][dst[1]] == 'p' and src[0] == 6 and dst[0] == 4:
         if dst[1] < 7 and board[dst[0]][dst[1]+1] == 'P':
            self.en_passant = (5, src[1])
         if dst[1] > 0 and board[dst[0]][dst[1]-1] == 'P':
            self.en_passant = (5, src[1])

   def white_king_under_threat (position):
      pass
