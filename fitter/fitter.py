#!/usr/bin/python3

import numpy as np
from numpy import linalg as la
from matplotlib import pyplot as plt
from matplotlib import animation

def gaussian (x, param_set):
   a = 1.0 / (param_set[0] * np.sqrt (2.0 * np.pi))
   b = np.exp (-0.5 * ((x - param_set[1]) / param_set[0])**2.0)
   c = 1

   return a * b * c

def weibull (x, param_set):
   a = param_set[1] / param_set[0]
   b = (x / param_set[0])**(param_set[1] - 1)
   c = np.exp (-(x / param_set[0])**param_set[1])

   return a * b * c

class fitter:
   # return a list of parameter sets that are randomized on the sphere of radius "eps"
   # about the starting "param_set" point
   def perturb_params (self, param_set, eps):

      # list of lists containing the candidate parameters epsilon step away
      # from the starting param_set
      candidate_params_list = []

      for itt in range (0, 4):
         # generate a random vector of length "eps"
         perturbation = np.random.rand (len (param_set)) * 2.0 - 1.0
         if (la.norm (perturbation) < 0.001): continue
         perturbation = perturbation / la.norm (perturbation) * eps
         candidate_params_list.append (param_set + perturbation)

      return candidate_params_list

   def update_params (self, x, y, param_set, step_size, itts):
      min_error_list = []
      param_set_list = [[],[]]

      for itt in range (itts):
         candidate_param_sets = self.perturb_params (param_set, step_size)
         min_error = self.compute_error (x, y, param_set)

         for candidate_param_set in candidate_param_sets:
            if abs(la.norm (candidate_param_set)) < 0.0001: continue
            err = self.compute_error (x, y, candidate_param_set)

            if err < min_error:
               param_set = candidate_param_set
               min_error = err

         min_error_list.append (min_error)
         param_set_list[0].append (param_set[0])
         param_set_list[1].append (param_set[1])

      return param_set, min_error_list, param_set_list

   def compute_error (self, x, y, param_set):
      return np.sum ((self.call (x, param_set) - y)**2)

if __name__ == "__main__":

   class weibull (fitter):
      def call (self, x, param_set):
         a = param_set[1] / param_set[0]
         b = (x / param_set[0])**(param_set[1] - 1)
         c = np.exp (-(x / param_set[0])**param_set[1])
         return a * b * c

   x = np.array ([0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
   y = np.array([0.0012812 , 0.00759732, 0.03599398, 0.10934005, 0.21296534, 0.26596152, 0.21296534, 0.10934005, 0.03599398, 0.00759732])

   param_set = [1.0, 1.0]

   Weibull = weibull ()

   fig, axs = plt.subplots (2)

   error_list = []
   
   def animate (i):
      global param_set
      global error_list
      param_set, min_error_list, param_set_list = Weibull.update_params (x, y, param_set, 0.001, 100)
      error_list.append (min_error_list[0])
      axs[0].clear ()
      axs[1].clear ()
      axs[0].plot (x, y, color = 'b')
      axs[0].plot (x, Weibull.call (x, param_set), color = 'r')
      axs[1].plot (range (len(error_list)), error_list, color = 'k')

   ani = animation.FuncAnimation(fig, animate, interval=100)
   plt.show ()
