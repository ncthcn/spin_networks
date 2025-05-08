import cases.theta_XZ as case
import matplotlib.pyplot as plt
import numpy as np
from math import floor, cos, pi


if __name__ == "__main__":

    # Parameters
    nb_interations = 10
    open_units = 101
    bridges = 50

    # Generate discrete values of c
    angles = np.linspace(-pi, pi, num=nb_interations)

    probs = []
    iter = 0
    for c in angles:
        probs.append(case.probxzsimpler(open_units, bridges, floor(bridges * cos(c))))
        iter = iter+1
        print("iteration ", iter, "/", nb_interations)

    # Convert the list to a NumPy array
    probs = np.array(probs)

    # Example: Save results to a .npy file
    filename = f"results_{open_units}_{bridges}_{nb_interations}.npy"
    results = np.array([angles, probs])  # Example NumPy array
    np.save(filename, results)