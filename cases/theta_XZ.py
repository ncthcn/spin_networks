import utils.functions as f
from math import floor, cos, pi
from multiprocessing import Pool
import pywigxjpf as wig

# Parallelized summation
def parallel_sum(func, ranges, args):
    with Pool() as pool:
        results = pool.starmap(func, [(*args, alpha, i, j) for alpha in ranges[0]
                                      for i in ranges[1]
                                      for j in ranges[2]])
    # print(args, ranges, results)
    return sum(results)

# Define omegaxz function
def omegaxz(X, Xp, Y, Yp, Z, Zp, n, np, npp, alpha, i, j):
    try:
        maxj = 2*max(X-n+alpha, X, i+n, i+alpha, Yp, n+Y, n+np, Yp-np+Y, Zp-npp+j, X-n+npp, Zp, X-n+j, Z+Zp, X-n+alpha, X-n+Zp, Z+alpha)  # Set the maximum quantum number
        wig.wig_table_init(maxj,6)
        wig.wig_temp_init(maxj)
        return (f.Delta(alpha) *
                f.SixJ(X - n, alpha, np, i, n, X) ** 2 *
                f.SixJ(Yp - np, np, Yp, n, Y, i) ** 2 *
                f.SixJ(Zp - np, npp, Zp, X - n, j, Xp - n) ** 2 *
                f.SixJ(Z, Zp, np, X - n, alpha, j) ** 2)
    finally:
        # Free resources (cleanup)
        wig.wig_temp_free()
        wig.wig_table_free()

# Define omegaxzprime function
def omegaxzprime(X, Xp, Y, Yp, Z, Zp, n, np, npp, alpha, i, j):
    try:
        maxj = 2*max(X-n+alpha, X, i+n, i+alpha, Yp, n+Y, n+np, Yp-np+Y, Zp-npp+j, X-n+npp, Zp, X-n+j, Z+Zp, X-n+alpha, X-n+Zp, Z+alpha, Zp-npp, Xp-n+j, Xp-n+0.5, Zp-npp-0.5+j)  # Set the maximum quantum number
        wig.wig_table_init(maxj,6)
        wig.wig_temp_init(maxj)
        return (f.Delta(alpha) *
                f.SixJ(X - n, alpha, np, i, n, X) ** 2 *
                f.SixJ(Yp - np, np, Yp, n, Y, i) ** 2 *
                f.SixJ(Zp - npp - 0.5, 0.5, Zp - npp, Xp - n, j, Xp - n + 0.5) ** 2 *
                f.SixJ(Zp - npp, npp, Zp, X - n, j, Xp - n) ** 2 *
                f.SixJ(Z, Zp, np, X - n, alpha, j) ** 2)
    finally:
        # Free resources (cleanup)
        wig.wig_temp_free()
        wig.wig_table_free()

def probxz(X, Xp, Y, Yp, Z, Zp, n, np, npp):
    alpha_range = range(abs(X - n - np), X - n + np)
    i_range = range(abs(n - np), n + np)
    j_range = range(abs(Zp - X + n), Zp + X - n )

    numerator = parallel_sum(omegaxzprime, (alpha_range, i_range, j_range),
                             (X, Xp, Y, Yp, Z, Zp, n, np, npp))
    denominator = parallel_sum(omegaxz, (alpha_range, i_range, j_range),
                               (X, Xp, Y, Yp, Z, Zp, n, np, npp))
    if denominator == 0:
        #raise ValueError("Denominator is zero, cannot compute probxz.")
        return 0
    return abs(f.Delta(Xp - n + 0.5) * f.Delta(Zp - npp) * (numerator / denominator))

# Define probxzsimpler function
def probxzsimpler(X, n, c):
    return probxz(X, X + floor(n * cos(pi / 4)), X, X + floor(n * cos(pi / 6)), X, X + c, n, n, n)
