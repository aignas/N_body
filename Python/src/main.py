#! /usr/bin/env python2

import numpy as np
import scipy.integrate as scp

class particle:
  def __init__(self, position, velocity, mass):
    self.x = position
    self.v = velocity
    self.m = mass

# This function calculates F/G
# Two particles named one and two:
# The force is how one is affected by two.
def Force(x1,x2,m1,m2):
  """
  Arguments:



  """
  # Calculate the displacement vector
  r = x2-x1
  r_mod = np.sqrt(r.dot(r))

  # Calculate the force itself:
  return m1*m2/np.power(r_mod,3)*r

# This calculates the net force in a very silly way
def Net_Force_Stupid(W,t,M):
  """
  Arguments:

    X:

    t:  Time

    M:

  """
  X,V = W
  f = np.zeros( Number_of_particles*2, Number_of_dimensions )
  for i in xrange(X.shape()[0]):
    for j in xrange(X.shape()[0]):
      if j==i:
        continue
      f = f + Force(X[i,:],X[j,:],M[i],M[j])

  # Return the net force
  return f

def ODE(W,t,M):
  X,V = W
  Force = Net_Force_Stupid(W,t,M)
  f = []
  for i in xrange(x.shape()[0]):
    f += [
        V[i,0], F[i,0],
        V[i,1], F[i,1],
        V[i,2], F[i,2]
        ]
  return f

# This for now just randomizes the data in the beginning:
def Container_construct(Number_of_particles,Number_of_dimensions):
  """
  Arguments:

    Number_of_particles - positive integer indicating how many particles we want

    Number_of_dimensions - positive integer from the set of {1,2,3}

  """
  X = np.random.rand( Number_of_particles, Number_of_dimensions )
  V = np.random.rand( Number_of_particles, Number_of_dimensions )
  M = np.random.rand( Number_of_particles )

  return X,V,M

# Create a container
X,V,M = Container_construct(3,2)
W = [X,V]

# ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 10.0
numpoints = 250

# Create the time samples for the output of the ODE solver.
# I use a large number of points, only because I want to make
# a plot of the solution that looks nice.
t = np.linspace(0,stoptime,numpoints)

# Call the ODE solver.
solution = scp.odeint(Net_Force_Stupid,W,t,atol=abserr,rtol=relerr)
