#!/usr/bin/python3

import numpy as np
import state
import white_moves
import black_moves
import convert_position
import assessment
import tree

def move (state, play, depth = 1):
   trunk = tree.Node (0, state, assessment.assess (state))
   node = trunk
   trunk.addNode (state, assessment.assess (state))
   add_level (trunk, play, depth)
   if play == 'w':
      trunk.pruneKeepMax ()
   if play == 'b':
      trunk.pruneKeepMin ()

def add_level (node, play, level):
   if level <= 0: return

   state = node.contents

   if play == 'w':
      positions, moves = white_moves.all_white_moves (state)
   elif play == 'b':
      positions, moves = black_moves.all_black_moves (state)

   for ind in range (len (positions)):
      for piece_move in moves[ind]:

         new_state = state.copy ()

         if play == 'w':
            print ("White moves " + convert_position.coord2basic (positions[ind]) +
                  " --> " + convert_position.coord2basic (piece_move))
            white_moves.move_white (new_state, positions[ind], piece_move)
         elif play == 'b':
            print ("Black moves " + convert_position.coord2basic (positions[ind]) +
                  " --> " + convert_position.coord2basic (piece_move))
            black_moves.move_black (new_state, positions[ind], piece_move)
         print (new_state)

         new_node = node.addNode (new_state, assessment.assess (new_state))

         if play == 'w':
            add_level (new_node, 'b', level-1)
         elif play == 'b':
            add_level (new_node, 'w', level-1)

         # Prune the node
         if play == 'w':
            node.pruneKeepMax ()
         elif play == 'b':
            node.pruneKeepMin ()

# Example
if __name__ == "__main__":
   state = state.State ()
   print (state)
   move (state, 'w', 5)
