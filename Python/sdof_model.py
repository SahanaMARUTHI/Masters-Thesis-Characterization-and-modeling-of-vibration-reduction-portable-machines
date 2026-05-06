import numpy as np

class TwoDOFSystem:
    def __init__(self, m1, m2, k1, k2, c1, c2):
        self.M = np.array([[m1, 0],
                           [0, m2]])

        self.C = np.array([[c1, -c1],
                           [-c1, c1 + c2]])

        self.K = np.array([[k1, -k1],
                           [-k1, k1 + k2]])

    def dynamic_matrix(self, omega):
        return (-omega**2 * self.M +
                1j * omega * self.C +
                self.K)
