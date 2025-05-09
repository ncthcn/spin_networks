import cases.theta_XZ as case
import matplotlib.pyplot as plt
import utils.triplet_generator as trip
import numpy as np
from math import floor, cos, pi


if __name__ == "__main__":

    # Parameters
    nb_tries = 10
    nb_iterations = 100
    x = 80
    y = 90
    z = 100
    n = 10

    probs = []
    iter = 0

    grouped_angles = trip.generate_angles(nb_tries, nb_iterations)
    # Iterate over (a, b) pairs and their corresponding c_values
    for (a, b), c_values in grouped_angles.items():  # Use .items() to unpack dictionary
        # Sort c values for smooth curves
        iter_c = 1
        c_values = sorted(c_values)
        # Compute the probability
        for c in c_values:
            probs.append(case.probxz(x, x + floor(n * cos(a)), 
                                     y, y + floor(n * cos(b)), 
                                     z, z + floor(n * cos(c)), 
                                     n, n, n))
            print("iteration ", iter * nb_iterations + iter_c, "/", nb_iterations*nb_tries)
            iter_c += 1
        iter += 1

    '''
    # Plot the curve
    plt.plot(c_values, y_values, label=f"(a={a:.2f}, b={b:.2f})")
    '''

    # Convert the list to a NumPy array
    probs = np.array(probs)

    # Example: Save results to a .npy file
    '''
    filename = f"results_{x}{y}{z}{n}_{nb_iterations}.npy"   
    results = np.array([grouped_angles, probs])
    np.save(filename, results)
    '''
    filename = f"results_{x}{y}{z}{n}_{nb_tries}_{nb_iterations}.npz"
    np.savez(filename, grouped_angles=grouped_angles, probs=probs)