#!/usr/bin/python3

import engine

state = engine.State ()

state.move ((0,0), (2,2))
print (state)

print (str (state.white_moves ((1, 5))))

keys, moves = state.all_white_moves ()
print (keys)
print (moves)
