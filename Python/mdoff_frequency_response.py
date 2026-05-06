import numpy as np
import matplotlib.pyplot as plt
from sdof_model import TwoDOFSystem

system = TwoDOFSystem(
    m1=1, m2=2,
    k1=1000, k2=1500,
    c1=10, c2=20
)

freq = np.linspace(1, 500, 500)
omega = 2 * np.pi * freq

transmissibility = []

for w in omega:
    A = system.dynamic_matrix(w)

    F = np.array([1, 0])  # excitation

    X = np.linalg.solve(A, F)

    transmissibility.append(abs(X[1] / X[0]))

plt.plot(freq, transmissibility)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Transmissibility")
plt.title("Hand-Arm Vibration Response")
plt.grid()
plt.show()
