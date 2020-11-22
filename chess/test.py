#!/usr/bin/python3

import state
import white_moves
import black_moves

state = state.State ()

white_moves.move_white (state, (1,4), (3,4))
print (state)

new_state = state.copy ()
white_moves.move_white (state, (1,2), (3,2))

print (state)
print (new_state)
