#!/usr/bin/python3

import state
import white_moves
import black_moves
import random

random.seed (0)

state = state.State ()
print (state)

for itt in range (80):
   # White move
   positions, moves = white_moves.all_white_moves (state)
   ind = random.randrange (len (positions))
   position = positions[ind]
   dst = random.choice (moves[ind])
   white_moves.move_white (state, position, dst)
   num_moves = 0
   for move in moves:
      num_moves += len (move)
   print ("num moves = " + str (num_moves))
   print (state)

   # Black move
   positions, moves = black_moves.all_black_moves (state)
   ind = random.randrange (len (positions))
   position = positions[ind]
   dst = random.choice (moves[ind])
   black_moves.move_black (state, position, dst)
   num_moves = 0
   for move in moves:
      num_moves += len (move)
   print ("num moves = " + str (num_moves))
   print (state)
