#!/usr/bin/python3

import fitter
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

class Sin (fitter.fitter):
   def call (self, x, param_set):
      result = 0;
      for param in param_set:
         result *= x
         result += param
      return result

x = np.arange (-3.5, 3.5, 0.1)
y = np.sin (x)

param_set = np.ones (9)

solution = np.array ([0.0, -1/5040.0, 0, 1/120.0, 0, -1/6.0, 0, 1.0, 0])

sin = Sin ()

fig, axs = plt.subplots (2)
step = 1.0

def animate (i):
   global param_set
   global step
   param_set_new, min_error_list, _ = sin.update_params (x, y, param_set, step, 100)
   if np.linalg.norm (param_set_new - param_set) == 0: step *= 0.9
   param_set = param_set_new
   axs[0].clear ()
   axs[1].clear ()
   axs[0].plot (x, y, color = 'b')
   axs[0].plot (x, sin.call (x, param_set), color = 'r')
   axs[1].plot (np.arange (len (solution)), solution, color = 'b')
   axs[1].plot (np.arange (len (param_set)), param_set, color = 'r')
   print (param_set)

ani = animation.FuncAnimation (fig, animate, interval=100)
plt.show ()
