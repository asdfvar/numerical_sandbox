import black_moves

def white_moves (state, src):
   board = state.board
   moves = []
   row = src[0]
   col = src[1]
   piece = board[row][col]
   if piece == 'P':
      if row < 7 and board[row+1][col] == 0: moves += [(row+1, col)]
      if row == 1 and board[row+1][col] == 0 and board[row+2][col] == 0: moves += [(row+2, col)]
      if row < 7 and col < 7 and str (board[row+1][col+1]) in 'prnbqk':
         moves += [(row+1, col+1)]
      if row < 7 and col > 0 and str (board[row+1][col-1]) in 'prnbqk':
         moves += [(row+1, col-1)]
      if state.en_passant is not None:
         if row+1 == state.en_passant[0] and col+1 == state.en_passant[1]:
            moves += state.en_passant
         elif row+1 == state.en_passant[0] and col-1 == state.en_passant[1]:
            moves += state.en_passant
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
      if state.wCastleAvailOO:
         if board[0][5] == board[0][6] == 0:
            pos, allmoves = black_moves.all_black_moves (state)
            valid = True
            if (0,5) in allmoves: valid = False
            if (0,6) in allmoves: valid = False
            if valid: moves += [(0,6)]
      if state.wCastleAvailOOO:
         if board[0][2] == board[0][3] == 0:
            pos, allmoves = black_moves.all_black_moves (state)
            valid = True
            if (0,2) in allmoves: valid = False
            if (0,3) in allmoves: valid = False
            if valid: moves += [(0,2)]
   return moves

def all_white_moves (state):
   board = state.board
   moves     = []
   positions = []
   for row in range (8):
      for col in range (8):
         lmoves = white_moves (state, (row, col))
         if len (lmoves) > 0:
            moves.append (lmoves)
            positions.append ((row, col))
   return positions, moves

def move_white (state, src, dst, promote = 'Q'):
   board = state.board
   legal_moves = white_moves (state, src)

   valid = False
   if len (legal_moves) > 0:
      for pos in legal_moves:
         if dst == pos: valid = True
   if not (valid):
      print ("illegal move " + str (src) + " -> " + str (dst))
      return

   # Perform castling
   if state.wCastleAvailOO or state.wCastleAvailOOO and board[src[0]][src[1]] == 'K':
      if dst == (0,6):
         board[0][5] = 'R'
         board[0][7] = 0
      elif dst == (0,2):
         board[0][3] = 'R'
         board[0][0] = 0

   # Disable castling if the king or either of the rooks have moved
   if src == (0, 0) and board[src[0]][src[1]] == 'R':
      state.wCastleAvailOOO = False
   elif src == (0, 7) and board[src[0]][src[1]] == 'R':
      state.wCastleAvailOO = False
   if board[src[0]][src[1]] == 'K':
      state.wCastleAvailOO  = False
      state.wCastleAvailOOO = False

   # Perform the move
   board[dst[0]][dst[1]] = board[src[0]][src[1]]
   board[src[0]][src[1]] = 0

   # Promote the pawn if the condition is met
   if board[7][dst[1]] == 'P': board[7][dst[1]] = promote

   # Set the en passant flag if the condition is met
   en_passant = None
   if board[dst[0]][dst[1]] == 'P' and src[0] == 1 and dst[0] == 3:
      if dst[1] < 7 and board[dst[0]][dst[1]+1] == 'p':
         en_passant = (2, src[1])
      if dst[1] > 0 and board[dst[0]][dst[1]-1] == 'p':
         en_passant = (2, src[1])
   state.en_passant = en_passant
