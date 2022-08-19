import math
import numpy as np

dim = 2
# Attempt at calculating the veilbein is a discrete form for the dirac solver

# First we need to define the metric - in our case this is in 2 dimensions one space and one time
# The metric will be a function of space so we shall define it as a function.
# Given a spacetime point (x,t) this function will return g * (x,t)^T

def metric(x,t,dims=dim):
    g = np.ones((dims,dims))
    g[0][0] = g_tt(t)
    g[1][1] = g_xx(x)
    return g

# We need to define the functions which define the metrix i.e. g_xx and g_tt

def g_xx(x):
    return x # Flat space time

def g_tt(t):
    return -t # Flat space time

def deritive(xOrt,xp,xm,h):
    if xOrt:
        #do this
    else:
        #do that
    return 0

# Since we can define the metric at any point we also need to define the christoffel symbols at each point
# as well

def christoffel(x,t,dx,dt,dims=dim):
    C = np.zeros((dims,dims,dims))

    for i in range(dims):
        for j in range(dims):
            for k in range(dims):
                tmp = 0
                for l in range(dims):
                    x=0
    return 0







