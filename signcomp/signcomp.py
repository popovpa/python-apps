import matplotlib.pyplot as plot
import math
import numpy

arr = numpy.arange(1, 1000, 1)

sign = numpy.sin(arr * (math.pi / 180))

plot.plot(sign)
plot.show()
