import cases.theta_XZ as case
import matplotlib.pyplot as plt
import utils.angle_generator as ang
import numpy as np
from math import floor, cos, pi


if __name__ == "__main__":

    # Parameters
    #nb_tries = 10
    nb_iterations = 100
    x = 80
    y = 90
    z = 100
    n = 10
    theta_XY = pi/4
    theta_YZ = pi/6

    probs = []
    iter = 0

    angles = ang.generate_angles(nb_iterations, theta_XY, theta_YZ)

    for c in angles:
        # Sort c values for smooth curves
        # Compute the probability
        probs.append(case.probxz(x, x + floor(n * cos(c)), 
                                     y, y + floor(n * cos(theta_XY)), 
                                     z, z + floor(n * cos(theta_YZ)), 
                                     n, n, n))
        print("iteration ", iter, "/", nb_iterations)
        iter += 1
    '''
    grouped_angles = ang.generate_angles(nb_tries, nb_iterations)
    # Iterate over (a, b) pairs and their corresponding c_values
    for (a, b), c_values in grouped_angles.items():  # Use .items() to unpack dictionary
        # Sort c values for smooth curves
        iter_c = 1
        c_values = sorted(c_values)
        # Compute the probability
        for c in c_values:
            probs.append(case.probxz(x, x + floor(n * cos(c)), 
                                     y, y + floor(n * cos(a)), 
                                     z, z + floor(n * cos(b)), 
                                     n, n, n))
            print("iteration ", iter * nb_iterations + iter_c, "/", nb_iterations*nb_tries)
            iter_c += 1
        iter += 1
    '''
    # Convert the list to a NumPy array
    probs = np.array(probs)

    # Save results to a .npy file
    '''
    filename = f"results_{x}{y}{z}{n}_{nb_tries}_{nb_iterations}.npz"
    np.savez(filename, grouped_angles=grouped_angles, probs=probs)
    '''
    filename = f"results_{x}{y}{z}{n}_{nb_iterations}.npz"
    np.savez(filename, angles=angles, probs=probs)