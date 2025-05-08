import numpy as np
from multiprocessing import Pool

# Parallelized summation
def parallel_sum(func, ranges, args):
    with Pool() as pool:
        results = pool.starmap(func, [(alpha, i, j, *args) for alpha in ranges[0]
                                      for i in ranges[1]
                                      for j in ranges[2]])
    return sum(results)