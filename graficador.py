


import matplotlib.mlab as mlab
from math import *
import pylab as p
import matplotlib.pyplot as plt
import numpy as np

datax = np.loadtxt(open("x.txt", 'r'))
datay = np.loadtxt(open("y.txt", 'r'))
dataz = np.loadtxt(open("z.txt", 'r'))

x = datax[:]
y = datay[:]
z = dataz[:]

count, bins, ignored =plt.hist(x, 40, normed=True)
plt.show()
count, bins, ignored =plt.hist(y, 40, normed=True)
plt.show()
count, bins, ignored =plt.hist(z, 40, normed=True)
plt.show()


H, xedges, yedges = np.histogram2d(x, y, bins=(1000,1000), normed =True)
H.shape, xedges.shape, yedges.shape

#extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]

plt.imshow(H)

plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

