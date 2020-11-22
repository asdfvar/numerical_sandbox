import white_moves

def black_moves (state, src):
   board = state.board
   moves = []
   row = src[0]
   col = src[1]
   piece = board[row][col]
   if piece == 'p':
      if row > 0 and board[row-1][col] == 0: moves += [(row-1, col)]
      if row == 6 and board[row-1][col] == 0 and board[row-2][col] == 0: moves += [(row-2, col)]
      if row > 0 and col < 7 and str (board[row-1][col+1]) in 'PRNBQK':
         moves += [(row-1, col+1)]
      if row > 0 and col > 0 and str (board[row-1][col-1]) in 'PRNBQK':
         moves += [(row-1, col-1)]
      if state.en_passant is not None:
         if row-1 == state.en_passant[0] and col+1 == state.en_passant[1]:
            moves += state.en_passant
         elif row-1 == state.en_passant[0] and col-1 == state.en_passant[1]:
            moves += state.en_passant
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
      if row > 0 and col > 0:
         step = 1
         while (row - step >= 0 and col - step >= 0 and board[row-step][col-step] == 0):
            moves += [(row-step, col-step)]
            step += 1
         if (row - step >= 0 and col - step >= 0 and str (board[row-step][col-step]) in '0PNBRQK'):
            moves += [(row-step, col-step)]
      if row < 7 and col > 0:
         step = 1
         while (row + step < 8 and col - step >= 0 and board[row+step][col-step] == 0):
            moves += [(row+step, col-step)]
            step += 1
         if (row + step < 8 and col - step >= 0 and str (board[row+step][col-step]) in '0PNBRQK'):
            moves += [(row+step, col-step)]
      if row > 0 and col < 7:
         step = 1
         while (row - step >= 0 and col + step < 8 and board[row-step][col+step] == 0):
            moves += [(row-step, col+step)]
            step += 1
         if (row - step >= 0 and col + step < 8 and str (board[row-step][col+step]) in '0PNBRQK'):
            moves += [(row-step, col+step)]
   elif piece == 'r':
      if row < 7:
         step = 1
         while (row + step < 8 and board[row+step][col] == 0):
            moves += [(row+step, col)]
            step += 1
         if (row + step < 8 and str (board[row+step][col]) in '0PNBRQK'):
            moves += [(row+step, col)]
      if row > 0:
         step = 1
         while (row - step >= 0 and board[row-step][col] == 0):
            moves += [(row-step, col)]
            step += 1
         if (row - step >= 0 and str (board[row-step][col]) in '0PNBRQK'):
            moves += [(row-step, col)]
      if col < 7:
         step = 1
         while (col + step < 8 and board[row][col+step] == 0):
            moves += [(row, col+step)]
            step += 1
         if (col + step < 8 and str (board[row][col+step]) in '0PNBRQK'):
            moves += [(row, col+step)]
      if col > 0:
         step = 1
         while (col - step >= 0 and board[row][col-step] == 0):
            moves += [(row, col-step)]
            step += 1
         if (col - step >= 0 and str (board[row][col-step]) in '0PNBRQK'):
            moves += [(row, col-step)]
   elif piece == 'q':
      if row < 7:
         step = 1
         while (row + step < 8 and board[row+step][col] == 0):
            moves += [(row+step, col)]
            step += 1
         if (row + step < 8 and str (board[row+step][col]) in '0PNBRQK'):
            moves += [(row+step, col)]
      if row > 0:
         step = 1
         while (row - step >= 0 and board[row-step][col] == 0):
            moves += [(row-step, col)]
            step += 1
         if (row - step >= 0 and str (board[row-step][col]) in '0PNBRQK'):
            moves += [(row-step, col)]
      if col < 7:
         step = 1
         while (col + step < 8 and board[row][col+step] == 0):
            moves += [(row, col+step)]
            step += 1
         if (col + step < 8 and str (board[row][col+step]) in '0PNBRQK'):
            moves += [(row, col+step)]
      if col > 0:
         step = 1
         while (col - step >= 0 and board[row][col-step] == 0):
            moves += [(row, col-step)]
            step += 1
         if (col - step >= 0 and str (board[row][col-step]) in '0PNBRQK'):
            moves += [(row, col-step)]
      if row < 7 and col < 7:
         step = 1
         while (row + step < 8 and col + step < 8 and board[row+step][col+step] == 0):
            moves += [(row+step, col+step)]
            step += 1
         if (row + step < 8 and col + step < 8 and str (board[row+step][col+step]) in '0PNBRQK'):
            moves += [(row+step, col+step)]
      if row > 0 and col > 0:
         step = 1
         while (row - step >= 0 and col - step >= 0 and board[row-step][col-step] == 0):
            moves += [(row-step, col-step)]
            step += 1
         if (row - step >= 0 and col - step >= 0 and str (board[row-step][col-step]) in '0PNBRQK'):
            moves += [(row-step, col-step)]
      if row < 7 and col > 0:
         step = 1
         while (row + step < 8 and col - step >= 0 and board[row+step][col-step] == 0):
            moves += [(row+step, col-step)]
            step += 1
         if (row + step < 8 and col - step >= 0 and str (board[row+step][col-step]) in '0PNBRQK'):
            moves += [(row+step, col-step)]
      if row > 0 and col < 7:
         step = 1
         while (row - step >= 0 and col + step < 8 and board[row-step][col+step] == 0):
            moves += [(row-step, col+step)]
            step += 1
         if (row - step >= 0 and col + step < 8 and str (board[row-step][col+step]) in '0PNBRQK'):
            moves += [(row-step, col+step)]
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
      if state.bCastleAvailOO:
         if board[7][5] == board[7][6] == 0:
            pos, allmoves = white_moves.all_white_moves (state)
            valid = True
            if (7,5) in allmoves: valid = False
            if (7,6) in allmoves: valid = False
            if valid: moves += [(7,6)]
      if state.bCastleAvailOOO:
         if board[7][2] == board[7][3] == 0:
            pos, allmoves = white_moves.all_white_moves (state)
            valid = True
            if (7,2) in allmoves: valid = False
            if (7,3) in allmoves: valid = False
            if valid: moves += [(7,2)]
   return moves

def all_black_moves (state):
   board = state.board
   moves     = []
   positions = []
   for row in range (8):
      for col in range (8):
         lmoves = black_moves (state, (row, col))
         if len (lmoves) > 0:
            moves.append (lmoves)
            positions.append ((row, col))
   return positions, moves

def move_black (state, src, dst, promote = 'q'):
   board = state.board
   legal_moves = black_moves (state, src)

   valid = False
   if len (legal_moves) > 0:
      for pos in legal_moves:
         if dst == pos: valid = True
   if not (valid):
      print ("illegal move " + str (src) + " -> " + str (dst))
      return

   # Perform castling
   if state.bCastleAvailOO or state.bCastleAvailOOO and board[src[0]][src[1]] == 'k':
      if dst == (7,6):
         board[7][5] = 'r'
         board[7][7] = 0
      elif dst == (7,2):
         board[7][3] = 'r'
         board[7][0] = 0

   # Disable castling if the king or either of the rooks have moved
   if src == (7, 0) and board[src[0]][src[1]] == 'r':
      state.wCastleAvailOOO = False
   elif src == (7, 7) and board[src[0]][src[1]] == 'r':
      state.wCastleAvailOO = False
   if board[src[0]][src[1]] == 'k':
      state.wCastleAvailOO  = False
      state.wCastleAvailOOO = False

   # Perform the move
   board[dst[0]][dst[1]] = board[src[0]][src[1]]
   board[src[0]][src[1]] = 0

   # Promote the pawn if the condition is met
   if board[0][dst[1]] == 'p': board[0][dst[1]] = promote

   # Set the en passant flag if the condition is met
   en_passant = None
   if board[dst[0]][dst[1]] == 'p' and src[0] == 6 and dst[0] == 4:
      if dst[1] < 7 and board[dst[0]][dst[1]+1] == 'P':
         en_passant = (5, src[1])
      if dst[1] > 0 and board[dst[0]][dst[1]-1] == 'P':
         en_passant = (5, src[1])
   state.en_passant = en_passant
