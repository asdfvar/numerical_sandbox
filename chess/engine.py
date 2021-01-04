#!/usr/bin/python3

import sys
import numpy as np
import state
import white_moves
import black_moves
import convert_position
import assessment
import tree
import time

def move (gameState, play, depth = 1):
   trunk = tree.Node (0, gameState, assessment.assess (gameState))
   start_play = play
   add_level (trunk, play, depth)
   if play == 'w':
      trunk.pruneSetMax ()
   if play == 'b':
      trunk.pruneSetMin ()
   return trunk.nodes[0].contents

def add_level (node, play, level):
   if level <= 0: return

   gameState = node.contents

   if play == 'w':
      positions, moves = white_moves.all_white_moves (gameState)
   elif play == 'b':
      positions, moves = black_moves.all_black_moves (gameState)

   for ind in range (len (positions)):
      for piece_move in moves[ind]:

         new_state = gameState.copy ()

         if play == 'w':
            #print ("White moves " + convert_position.coord2basic (positions[ind]) +
            #      " --> " + convert_position.coord2basic (piece_move))
            white_moves.move_white (new_state, positions[ind], piece_move)
         elif play == 'b':
            #print ("Black moves " + convert_position.coord2basic (positions[ind]) +
            #      " --> " + convert_position.coord2basic (piece_move))
            black_moves.move_black (new_state, positions[ind], piece_move)
         #print (new_state)
         #time.sleep (0.1)

         new_node = node.addNode (new_state, assessment.assess (new_state))

         if play == 'w':
            add_level (new_node, 'b', level-1)
         elif play == 'b':
            add_level (new_node, 'w', level-1)

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
   for ind in range (20):
      gameState = move (gameState, play, 3)
      print (ind)
      print (gameState)
      if   play == 'w': play = 'b'
      elif play == 'b': play = 'w'
