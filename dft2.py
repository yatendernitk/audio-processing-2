# DFT of complex Sinewave

import numpy as np
import matplotlib.pyplot as plt

X = np.array([])
N = 64
k0 = 7

# x = np.exp(1j * 2 * np.pi * k0 / N * np.arange(N))  // this is for
# complex sinewave
x = np.cos(2 * np.pi * k0 / N * np.arange(N))
#  for sinusoid signal
nv = np.arange(-N / 2, N / 2)
kv = np.arange(-N / 2, N / 2)
for k in kv:
    s = np.exp(1j * 2 * np.pi * k / N * nv)
    X = np.append(X, sum(x * np.conjugate(s)))

plt.plot(np.arange(N), abs(X))
plt.axis([0, N - 1, 0, N])
plt.show()
