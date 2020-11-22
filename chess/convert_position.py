def coord2basic (coord):
   row = coord[0] + 1
   col = coord[1] + ord ('a')
   return str (chr (col) + str (row))
