import matplotlib.pyplot as plt

def plot_transmissibility(freq, R):
    plt.figure()
    plt.plot(freq, R)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Transmissibility")
    plt.title("Transmissibility vs Frequency")
    plt.grid()
    plt.show()

def plot_apparent_mass(freq, M):
    plt.figure()
    plt.plot(freq, M)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Apparent Mass")
    plt.title("Apparent Mass vs Frequency")
    plt.grid()
    plt.show()
