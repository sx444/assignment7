'''this is for question 1'''
'''generate required arrays based on a given array'''

import numpy as np

class get_array:
      '''this class includes the original array and methods to get the required arrays'''
      def __init__(self):
          '''this is to get the original array'''
          self.array = np.arange(1, 16).reshape((3, 5)).transpose() 

      def get_rows2and4(self):
          '''this is for question (a) to get the 2nd and 4th rows of the given array'''
	  rows2and4 = self.array[[1,3], :]
	  return rows2and4

      def get_column2(self):
	  '''this is for question (b) to get the 2nd column'''
          column2 = self.array[:, [1]]
	  return column2

      def get_rectangular(self):
	  '''this is for question (c) to get the required rectangular'''
	  rectangular = self.array[1:4, :]
          return rectangular

      def get_3to11(self):
	  '''this is for question (d) to get elements from 3 to 11'''
	  d = self.array.ravel()
	  d.sort()
	  d = d[np.logical_and((d >= 3), (d <= 11))]
          return d








