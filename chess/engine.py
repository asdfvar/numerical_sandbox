#!/usr/bin/python3

import sys
import numpy as np
import state
import white_moves
import black_moves
import convert_position
import assessment
import tree

def move (gameState, play, depth = 1):
   trunk = tree.Node (0, [gameState, 0, 0], assessment.assess (gameState))
   start_play = play
   add_level (trunk, play, depth)
   if play == 'w':
      trunk.pruneSetMax ()
   if play == 'b':
      trunk.pruneSetMin ()
   return trunk.nodes[0].contents

def add_level (node, play, level):
   if level <= 0: return

   gameState = node.contents[0]

   all_play_moves = {
      'w': white_moves.all_white_moves,
      'b': black_moves.all_black_moves}

   positions, moves = all_play_moves[play] (gameState)

   play_moves = {
      'w': white_moves.move_white,
      'b': black_moves.move_black}

   if   play == 'w': next_play = 'b'
   elif play == 'b': next_play = 'w'

   for ind in range (len (positions)):
      for piece_move in moves[ind]:

         new_state = gameState.copy ()

         play_moves[play] (new_state, positions[ind], piece_move)

         new_node = node.addNode ([new_state, positions[ind], piece_move],
               assessment.assess (new_state))

         add_level (new_node, next_play, level-1)

         # Prune the node
         if play == 'w':
            node.pruneSetMax ()
         elif play == 'b':
            node.pruneSetMin ()

# Example
if __name__ == "__main__":
   sys.setrecursionlimit (10000)
   gameState = state.State ()
   print (gameState)

   play = 'w'
   for ind in range (3):
      result = move (gameState, play, 3)
      gameState = result[0]
      position  = result[1]
      movement  = result[2]
      print (convert_position.coord2basic (position) + " --> " +
            convert_position.coord2basic (movement))
      print (gameState)
      if   play == 'w': play = 'b'
      elif play == 'b': play = 'w'
