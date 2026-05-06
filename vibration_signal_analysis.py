import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

fs = 1000
t = np.linspace(0, 1, fs)

signal = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)
signal += 0.2*np.random.randn(len(t))

# FFT
fft_vals = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(signal), 1/fs)

# PSD
f_psd, psd = welch(signal, fs)

plt.figure()

plt.subplot(3,1,1)
plt.plot(t, signal)
plt.title("Time Signal")

plt.subplot(3,1,2)
plt.plot(freqs[:fs//2], np.abs(fft_vals[:fs//2]))
plt.title("FFT")

plt.subplot(3,1,3)
plt.semilogy(f_psd, psd)
plt.title("PSD")

plt.tight_layout()
plt.show()
