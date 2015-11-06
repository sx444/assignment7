'''this is for question4'''
'''compute the Mandelbrot fractal using the Mandelbrot iteration'''

import numpy as np
import matplotlib.pyplot as plt

def compute_mandelbrot():
    '''this is to do the iteration'''
    N_max = 50
    some_threshold = 50
    size = 1000

    # construct grid
    x = np.linspace(-2, 1, size)
    y = np.linspace(-1.5, 1.5, size)
    c = x[:, np.newaxis] + 1j * y[np.newaxis, :]

    # do the iteration
    z = c
    for v in range(N_max):
        with np.errstate(all = "ignore"):
	     z = z**2 + c
    with np.errstate(all = "ignore"):
	 mask = (abs(z) < some_threshold)

    # save the result to an image.
    plt.imshow(mask.T, extent = [-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
