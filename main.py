import cases.theta_XZ as case
import matplotlib.pyplot as plt
import triplet_generator as trip
import numpy as np
from math import floor, cos, pi


if __name__ == "__main__":

    # Parameters
    '''
    nb_interations = 10
    open_units = 101
    bridges = 50
    '''
    nb_interations = 10
    x = 80
    y = 90
    z = 100
    n = 10

    triplets = trip.generate_triplets(nb_interations)

    # Generate discrete values of c
 #   angles = np.linspace(-pi, pi, num=nb_interations)

    probs = []
    iter = 0
    for c in angles:
#        probs.append(case.probxzsimpler(open_units, bridges, floor(bridges * cos(c))))
        probs.append(case.probxz(x, x+floor(n*cos(triplets[0])), y, y+floor(n*cos(triplets[1])), z, z+floor(n*cos(triplets[2])),n,n,n))
        iter = iter+1
        print("iteration ", iter, "/", nb_interations)

    # Convert the list to a NumPy array
    probs = np.array(probs)

    # Example: Save results to a .npy file
    #filename = f"results_{open_units}_{bridges}_{nb_interations}.npy"
    filename = f"results_{x}{y}{z}{n}_{nb_interations}.npy"   
    results = np.array([triplets, probs])  # Example NumPy array
    np.save(filename, results)