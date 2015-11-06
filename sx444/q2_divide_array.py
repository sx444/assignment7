'''this is for question 2'''
'''divide each column of the given array element-wise with the second array'''

import numpy as np

class divide_array:
      '''this class includes the given array and a method to divide it'''
      def __init__(self):
	  '''this constructor is to generate the given array'''
          self.array = np.arange(25).reshape(5, 5)

      def divide(self):
	  '''this is to divide the given array using the second given array'''
          provided_array = np.array([1., 5, 10, 15, 20])
	  divider = provided_array[:, np.newaxis]
	  divided_array = np.divide(self.array, divider)
	  return divided_array

