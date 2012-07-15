#! /usr/bin/env python2

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def Data_init(**kwargs):
  """
  if there is a kwarg['file'], then read from file, otherwise find
  kwargs['dimensions'] and kwargs['particles'] and randomize data.  If
  this fails, print an error.

  kwargs['time'] is a tuple of final time and number of steps.
  """
  if 'file' in kwargs:
    print "Reading the file"
  else:
    print "Randomizing the initial data"
    XV = np.random.rand(kwargs['particles'],kwargs['dimensions']*2) * 2 - 1
    M = np.random.rand(kwargs['particles'])

  t_f,num = kwargs['time']
  t = np.linspace(0,t_f,num)

  return XV,M,t

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
  F = np.zeros(X.shape)
  for i in xrange(X.shape[0]):
    for j in xrange(X.shape[0]):
      if i == j:
        continue
      F[i] += Gravitational_force(
          [ X[i,:], X[j,:] ],
          [ M[i], M[j] ]
          )

  return F

def ODE(XV,t,M,shape):
  """
  This is the function which is needed for odeint function
  """
  dimensions = shape[1]/2
  XV = XV.reshape(shape)
  F = Net_force_1( XV[:,:dimensions], M)

  R = np.append( XV[:,dimensions:], F, axis=0 )

  return R.flatten()

debug = False

# Initiate the data:
XV0, M, t = Data_init(particles=4,dimensions=2,time=[10,255])

if debug:
  print """
  ====================================
  Debug
  ====================================
  """
  print XV0
  print "\n"
  print Gravitational_force([ XV0[0,:2],XV0[1,:2] ], [M[0],M[1]])
  print "\n"
  print Net_force_1(XV0[:,:2],M)
  print "\n"
  print ODE(XV0,1,M)

# Solve the ODE system
shape_tmp = XV0.shape
XV0 = XV0.flatten()
solution = odeint(ODE,XV0,t,args=(M,shape_tmp))
XV0 = XV0.reshape(shape_tmp)

solution = solution.reshape([255,4,4])
print solution.shape

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(
    solution[:,0,0], solution[:,0,1],
    solution[:,1,0], solution[:,1,1],
    solution[:,2,0], solution[:,2,1],
    solution[:,3,0], solution[:,3,1]
    )
plt.show()

# vim: tw=72
