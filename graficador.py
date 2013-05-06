import matplotlib.mlab as mlab
from math import *
import pylab 
import matplotlib.pyplot as plt
import numpy as np

datax = np.loadtxt(open("x.txt", 'r'))
datay = np.loadtxt(open("y.txt", 'r'))
dataz = np.loadtxt(open("z.txt", 'r'))

x = datax[:]
y = datay[:]
z = dataz[:]

H1, x1edges, y1edges = np.histogram2d(x, y, bins=25, range=None, normed=False, weights=None)
H2, x2edges, y2edges = np.histogram2d(y, z, bins=25, range=None, normed=False, weights=None)
H3, x3edges, y3edges = np.histogram2d(z, x, bins=25, range=None, normed=False, weights=None)

extent1 = [y1edges[0], y1edges[-1], x1edges[-1], x1edges[0]]
extent2 = [y2edges[0], y2edges[-1], x2edges[-1], x2edges[0]]
extent3 = [y3edges[0], y3edges[-1], x3edges[-1], x3edges[0]]


plt.imshow(H1, extent=extent1, interpolation='nearest')
plt.colorbar()
plt.savefig('x_y.png')

plt.imshow(H2, extent=extent2, interpolation='nearest')
plt.colorbar()
plt.savefig('y_z.png')

plt.imshow(H3, extent=extent3, interpolation='nearest')
plt.colorbar()
plt.savefig('z_x.png')
