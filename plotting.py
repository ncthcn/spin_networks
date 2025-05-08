import numpy as np
import matplotlib.pyplot as plt
from math import cos, pi

# parameters
nb_interations = 10
open_units = 101
bridges = 50

# Load the data from the .npy file
filename = f"results_{open_units}_{bridges}_{nb_interations}.npy"
results = np.load(filename)

# Extract angles and probs
angles = np.array(results[0])  # First row
probs = np.array(results[1])  # Second row
cosines = np.cos(np.array(results[0])) # Second row

# Plot angles vs. probs
plt.plot(angles, probs, marker="o")

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