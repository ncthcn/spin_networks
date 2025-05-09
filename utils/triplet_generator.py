import numpy as np

def generate_angles(n, N, angle_min=0, angle_max=np.pi):
    grouped_angles = {}  # Use a dictionary to store (a, b) as keys and lists of c as values
    for _ in range(n):
        # Randomly generate a and b within the specified range
        a = np.random.uniform(angle_min, angle_max)
        b = np.random.uniform(angle_min, angle_max)
        
        # Create the pair (a, b)
        grouped_angles[(a, b)] = []  # Initialize an empty list for c values
        
        # Compute the valid range for c
        c_min = abs(a - b)
        c_max = a + b
        
        for __ in range(N):  # Generate N values of c for this (a, b) pair
            # Randomly generate c within the range [c_min, c_max]
            c = np.random.uniform(c_min, c_max)
            # Append c to the list for this (a, b) pair
            grouped_angles[(a, b)].append(c)

        grouped_angles[(a,b)] = sorted(grouped_angles[(a,b)])
    
    return grouped_angles