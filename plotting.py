import numpy as np
import matplotlib.pyplot as plt
from math import cos, pi

# parameters
nb_tries = 10
nb_iterations = 100
x = 80
y = 90
z = 100
n = 10

# Load the data from the .npy file
#filename = f"results_{open_units}_{bridges}_{nb_iterations}.npy"
#results = np.load(filename)
filename = f"results_{x}{y}{z}{n}_{nb_tries}_{nb_iterations}.npz"
results = np.load(filename, allow_pickle=True)
grouped_angles = results['grouped_angles'].item()  # Convert back to a dictionary
probs = results['probs']


# Plot the results
plt.figure(figsize=(10, 6))

index = 0

for (a, b), c_values in grouped_angles.items():
    # Convert c_values to a NumPy array for mathematical operations
    c_values = np.array(c_values)
    
    # Extract the corresponding probabilities for this (a, b) pair
    num_c_values = len(c_values)
    probs_for_pair = probs[index:index + num_c_values]
    index += num_c_values  # Update the index for the next (a, b) pair
    
    # Compute the y-values for the plot
    y_values = probs_for_pair - abs(1 - np.cos(c_values)) / 2  # Use NumPy's cos for arrays
    
    # Plot the curve
    #plt.plot(c_values, y_values, label=f"(a={a:.2f}, b={b:.2f})")
    plt.plot(c_values, probs_for_pair, label=f"(a={a:.2f}, b={b:.2f})")


# Add labels, legend, and title
plt.xlabel("XZ angle")
plt.ylabel("Prob-1/2-cos/2")
plt.title("Euclideanity for Different (XY, YZ) Pairs")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Place legend outside the plot
plt.tight_layout()
plt.show()


'''
# Extract angles and probs
angles = np.array(results[0])  # First row
probs = np.array(results[1])  # Second row
cosines = np.cos(np.array(results[0])) # Second row

# Plot angles vs. probs
plt.plot(grouped_angles[1], probs, marker="o")

# Add labels and title
plt.xlabel("Angle")
plt.ylabel("P(Z+1/2)")
plt.title("Probability")

# Show the plot
plt.show()

# Plot angles vs. probs
plt.plot(angles, probs - abs(1-cosines) / 2, marker="o")

# Highlight the region between angle1 and angle2
plt.axvspan(abs( pi / 6- pi / 4), pi / 6+ pi / 4, color='red', alpha=0.3, label='Euclidean region')

# Add labels and title
plt.xlabel("Angle")
plt.ylabel("P(Z+1/2) - |1+cos(theta)|/2")
plt.title("Euclideanity")

# Show the plot
plt.show()
'''