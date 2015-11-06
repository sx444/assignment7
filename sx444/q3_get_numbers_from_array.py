'''this is for question 3'''
'''pick the number closest to 0.5 for each row of a 10*3 random array in range [0, 1].'''

import numpy as np

class pick_numbers_from_array:
      '''this class includes a 10*3 random array in [0, 1] and a method to get the numbers closest to 0.5'''
      def __init__(self):
          '''this is to generate the original 10*3 array'''
          self.array = np.random.rand(10, 3)

      def print_array(self):
          print self.array

      def pick_numbers(self):
          ''' find the closest number to 0.5 for each row'''
	  distance = np.abs(self.array - 0.5) # get the distance of each number to 0.5
          index_closest = np.argsort(distance)[:, 0] # get the index of the closest number in each row
          closest_numbers = self.array[np.arange(0,10),index_closest] # get the numbers closest to 0.5 in each row
	  return closest_numbers



