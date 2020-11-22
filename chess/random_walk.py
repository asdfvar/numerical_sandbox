#!/usr/bin/python3

import state
import white_moves
import black_moves
import random

random.seed (0)

state = state.State ()
print (state)

for itt in range (36):
   # White move
   positions, moves = white_moves.all_white_moves (state)
   ind = random.randrange (len (positions))
   position = positions[ind]
   dst = random.choice (moves[ind])
   white_moves.move_white (state, position, dst)
   print (state)
   print (state.assess ())

   # Black move
   positions, moves = black_moves.all_black_moves (state)
   ind = random.randrange (len (positions))
   position = positions[ind]
   dst = random.choice (moves[ind])
   black_moves.move_black (state, position, dst)
   print (state)
   print (state.assess ())
