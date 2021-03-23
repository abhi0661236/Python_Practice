import numpy
from scipy import stats

speed=[23,45,23,64,33,12,35,23,56,32,34,36,98,34,163,53,87]

mean = numpy.mean(speed)
print(mean)

speedmed = numpy.median(speed)
print(speedmed)

spmod = stats.mode(speed)
print(spmod)