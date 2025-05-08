import math
import numpy as np
import pywigxjpf as wig
#import ctypes
#from ctypes import c_int, c_double
#from sympy.physics.wigner import wigner_6j
from functools import lru_cache

'''
# Load the GSL library
gsl = ctypes.CDLL("/usr/local/lib/libgsl.dylib")

# Define the function signature for gsl_sf_coupling_6j
gsl.gsl_sf_coupling_6j.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int]
gsl.gsl_sf_coupling_6j.restype = c_double

# Define a Python wrapper for the GSL 6-j symbol function
def gsl_6j(a, b, e, c, d, f):
    try:
        result = gsl.gsl_sf_coupling_6j(2*a, 2*b, 2*e, 2*c, 2*d, 2*f)
        if result == float('inf') or result == float('-inf'):
            raise OverflowError("GSL overflow")
        print("Used GSL")
        return result
    except OverflowError:
        # Fallback to SymPy
        print("Used Sympy")
        return float(wigner_6j(a, b, e, c, d, f))
'''

# Precompute factorials up to a reasonable limit
FACTORIAL_CACHE = [math.factorial(i) for i in range(1000)]  # Adjust limit as needed

def factorial(n):
    if n < len(FACTORIAL_CACHE):
        return FACTORIAL_CACHE[n]
    return math.factorial(n)

# Define Theta function with precomputed factorials
def Theta(a, b, c):
    return ((-1) ** (a + b + c) * factorial(a + b + c + 1) /
            (factorial(a + b - c) * factorial(a - b + c) * factorial(-a + b + c)))

# Define Delta function
@lru_cache(maxsize=None)
def Delta(n):
    return (-1) ** (2 * n) * (2 * n + 1)

# Define Lambda function
def Lambda(a, b, c):
    return (-1) ** (a + b - c - 4 * a * b)

#Define 6-j symbol
def SixJ(a,b,e,c,d,f):
    
    if (a + b + e) % 1 == 0 and abs(a - b) <= e <= a + b and \
       (c + d + e) % 1 == 0 and abs(c - d) <= e <= c + d and \
       (d + a + f) % 1 == 0 and abs(a - d) <= f <= a + d and \
       (b + c + f) % 1 == 0 and abs(b - c) <= f <= b + c:
# sympy version
#   return wigner_6j(a, b, e, c, d, f)
# GSL version
#        return gsl_6j(a, b, e, c, d, f)
# pywigxjpf version
# Initialize the WIGXJPF library
        return wig.wig6jj(int(2*a), int(2*b), int(2*e), int(2*c), int(2*d), int(2*f))
    else:
        return 0
    '''
        try:
            maxj = max(a+b, c + d, a + d, b + c)  # Set the maximum quantum number
            wig.wig_table_init(maxj)
            wig.wig_temp_init()
            result = wig.wig6j(a, b, e, c, d, f)
            return result
        finally:
            # Free resources (cleanup)
            wig.wig_temp_free()
            wig.wig_table_free()
    '''

# Define SixJchange function
def SixJchange(a, b, e, c, d, f):
    return ((-1) ** (-(a + b + c + d + 2 * e)) *
            Delta(e) *
            abs(math.sqrt(Theta(a, b, f) * Theta(c, d, f) /
                      (Theta(b, c, e) * Theta(a, d, e)))))

def newSixJ(a, b, e, c, d, f):
    '''
    if (a + b + f) % 1 == 0 and abs(a - b) <= f <= a + b and \
       (c + d + f) % 1 == 0 and abs(c - d) <= f <= c + d and \
       (d + a + e) % 1 == 0 and abs(a - d) <= e <= a + d and \
       (b + c + e) % 1 == 0 and abs(b - c) <= e <= b + c:
    '''
    return ( SixJchange(a,b,e,c,d,f) *
                SixJ(a, b, f, c, d, e))
    '''
    else:
        return 0
    '''