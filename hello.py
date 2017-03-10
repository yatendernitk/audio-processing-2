import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt


(fs ,x) = read('flute-A4.wav')

t = np.arange(x.size)/float(fs)
plt.plot(t,x)
plt.show()
