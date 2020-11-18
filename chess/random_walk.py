#!/usr/bin/python3

import random
import engine

state = engine.Kernel ()
print (state)

for itt in range (20):
   # White move
   positions, moves = state.all_white_moves ()
   ind = random.randrange (len (positions))
   position = positions[ind]
   dst = random.choice (moves[ind])
   state.move_white (position, dst)
   print (state)

   # Black move
   positions, moves = state.all_black_moves ()
   ind = random.randrange (len (positions))
   position = positions[ind]
   dst = random.choice (moves[ind])
   state.move_black (position, dst)
   print (state)
