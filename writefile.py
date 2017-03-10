import numpy as np
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt


(fs ,x) = read('flute-A4.wav')
y = x[::2]
write('test.wav',fs/2,y)
