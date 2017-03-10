import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt


def giveArray(x):
    return x[44100:45100]
    
(fs, x) = read('flute-A4.wav')
y = giveArray(x)
print y.size
plt.plot(y)
plt.show()



