#!/usr/bin/python3

import numpy as np
import state
import white_moves
import black_moves
import convert_position
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
   print (str (itt) + ": White moves " + convert_position.coord2basic (position) +
         " --> " + convert_position.coord2basic (dst))
   print (state)
   print ("Assessment: " + str (state.assess ()))
   if state.isEnd (): break
   print ()

   # Black move
   positions, moves = black_moves.all_black_moves (state)
   ind = random.randrange (len (positions))
   position = positions[ind]
   dst = random.choice (moves[ind])
   black_moves.move_black (state, position, dst)
   print (str (itt) + ": Black moves " + convert_position.coord2basic (position) +
         " --> " + convert_position.coord2basic (dst))
   print (state)
   print ("Assessment: " + str (state.assess ()))
   if state.isEnd (): break
   print ()
