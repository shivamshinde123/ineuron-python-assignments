import numpy as np

def calculate_vol_of_sphere(d):

    r = d/2

    return (4/3)*(np.pi)*(r**3)


vol = calculate_vol_of_sphere(12)

print(f"Volumn of the sphere with the diameter of 12cm is {np.round(vol,2)} cubicv.cm.")