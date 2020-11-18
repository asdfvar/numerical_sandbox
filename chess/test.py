#!/usr/bin/python3

import engine

state = engine.Kernel ()

state.move ((1,4), (3,4))
print (state)

print (str (state.white_moves ((1, 5))))

keys, moves = state.all_white_moves ()
print (keys)
print (moves)
