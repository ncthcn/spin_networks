import numpy as np

def generate_angles(N, angle_min=0, angle_max=np.pi):
    triplets = []
    for _ in range(N):
        # Randomly generate a and b within the specified range
        a = np.random.uniform(angle_min, angle_max)
        b = np.random.uniform(angle_min, angle_max)
        
        # Compute the valid range for c
        c_min = abs(a - b)
        c_max = a + b
        
        # Randomly generate c within the range [c_min, c_max]
        c = np.random.uniform(c_min, c_max)
        
        # Append the triplet to the list
        triplets.append((a, b, c))
    return triplets
