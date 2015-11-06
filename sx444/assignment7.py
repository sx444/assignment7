'''author: Siyi Xie (sx444)'''
'''This main program will generate all the answers of assignment7.'''

import numpy as np
import q1_get_array  
import q2_divide_array 
import q3_get_numbers_from_array 
import q4_compute_mandelbrot


def generate_answers():
    '''this is to generate the all the answers'''
    # 1st 
    q1_answers = q1_get_array.get_array()
    print "q1a: The new array containning the 2nd and 4nd rows:"
    print q1_answers.get_rows2and4()
    print "q1b: The new array that contains the 2nd column:"
    print q1_answers.get_column2()
    print "q1c: The new array containning all the elements in the rectangular section between the coordinates[1,0] and [3,2]:"
    print q1_answers.get_rectangular()
    print "q1d: The new array containning only elements with values that are between 3 and 11:"
    print q1_answers.get_3to11()

    # 2nd
    q2_answers = q2_divide_array.divide_array()
    print "q2: This is the divide result:"
    print q2_answers.divide()

    # 3rd
    q3_answers = q3_get_numbers_from_array.pick_numbers_from_array()
    print "q3: This is the original array:"
    q3_answers.print_array()
    print "q3: The number closest to 0.5 for each row is:"    
    print q3_answers.pick_numbers()

    # 4th

    print "q4: the result is saved"
    q4_compute_mandelbrot.compute_mandelbrot()

if __name__ == "__main__":
   try: 
       generate_answers()
   except EOFError:
	  pass
   except TypeError:
	  pass
   except KeyboardInterrupt:
	  pass
generate_answers()


