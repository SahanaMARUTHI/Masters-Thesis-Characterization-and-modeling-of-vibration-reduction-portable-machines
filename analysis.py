import numpy as np

def transmissibility(response):
    X1 = response[:, 0]
    X2 = response[:, 1]
    return np.abs(X2 / X1)

def apparent_mass(response, freq):
    omega = 2 * np.pi * freq
    force = 1
    velocity = 1j * omega * response[:, 1]
    return np.abs(force / velocity)
