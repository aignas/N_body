#! /usr/bin/env python2

import numpy as np
from scipy.integrate import odeint

def Data_init(**kwargs):
  """
  if there is a kwarg['file'], then read from file, otherwise find
  kwarg['dimensions'] and kwarg['particles'] and randomize data.  If
  this fails, print an error.

  kwarg['time'] is a tuple of final time and number of steps.
  """
  if kwarg['file']:
    print "Reading the file"
  else:
    print "Randomizing the initial data"
    X = np.random.rand(kwarg['particles'],kwarg['dimensions'])
    V = np.random.rand(kwarg['particles'],kwarg['dimensions'])

  t = np.linspace(0,kwarg['time'])

  return X,V,t

def Gravitational_force(X,M):
  # Expand the collections
  x1, x2 = X
  m1, m2 = M

  # Calculate a displacement vector
  r = x2-x1
  # Calculate it's magnitude
  r_mod = np.sqrt(r.dot(r))
  # Calculate the force itself
  f = m1*m2*r / np.power(r_mod,3)

  return f

def Net_force_1(X,M):
  """
  This is a very stupid way of calculating the force, as we need to go
  through all the pairs recursivelly. This should be swapped for
  Barnes-Hut algorithm.
  """
  F = np.zeros(X.shape())
  for i in xrange(X.shape()[0]):
    for j in xrange(X.shape()[0]):
      if i == j:
        continue
      F += Gravitational_force(
          [ X[i,:], X[j,:] ],
          [ M[i], M[j] ]
          )
  return F

def ODE(X,t,M):
  """
  This is the function which is needed for odeint function
  """



# vim: tw=72
