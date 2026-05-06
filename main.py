import numpy as np
from system import TwoDOFSystem
from solver import frequency_response
from analysis import transmissibility, apparent_mass
from plots import plot_transmissibility, plot_apparent_mass

# Create system
system = TwoDOFSystem(
    m1=1.0,
    m2=2.0,
    k1=1000,
    k2=1500,
    c1=10,
    c2=20
)

# Frequency range
freq = np.linspace(1, 500, 500)

# Solve
response = frequency_response(system, freq)

# Analysis
R = transmissibility(response)
M = apparent_mass(response, freq)

# Plot results
plot_transmissibility(freq, R)
plot_apparent_mass(freq, M)
