#!/usr/bin/python3

import state
import white_moves
import black_moves

state = state.State ()

white_moves.move_white (state, (1,4), (3,4))
print (state)

#print (str (white_moves ((1, 5))))

#keys, moves = state.all_white_moves ()
#print (keys)
#print (moves)
