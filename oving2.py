#!/bin/python3
def pi():
    #acting with a radius of one
    s = 1. #length of a side
    e = 6. # nr of edges of this equilateral shape
    while True:
        yield e*s / 2
        e *= 2
        h_i = ( 1 - (s / 2)**2 )**0.5   #height of inner triangle
        h_e = 1 - h_i #height of exterior triangle
        s = (h_e**2 + (s/2)**2)**0.5

r = []
g = pi()
for i in range(150):
    v = next(g)
    print(v)
    r.append(v)


from matplotlib import pyplot as plt
from numpy import array
plt.xkcd()
plt.plot(r)
plt.show()
