import matplotlib.pyplot as plot
import numpy as np
import numpy.fft as fft

sig1 = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]
sig2 = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]

cross_corr = fft.ifft(fft.rfft(sig1) * np.conj(fft.rfft(sig2)))

plot.plot(cross_corr)
plot.show()
