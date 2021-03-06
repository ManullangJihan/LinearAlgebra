#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:11:40 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.proj3d import proj_transform
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.patches import FancyArrowPatch
class Arrow3D(FancyArrowPatch):
    def __init__(self, x, y, z, dx, dy, dz, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._xyz = (x,y,z)
        self._dxdydz = (dx,dy,dz)

    def draw(self, renderer):
        x1,y1,z1 = self._xyz
        dx,dy,dz = self._dxdydz
        x2,y2,z2 = (x1+dx,y1+dy,z1+dz)

        xs, ys, zs = proj_transform((x1,x2),(y1,y2),(z1,z2), renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        super().draw(renderer)

def _arrow3D(ax, x, y, z, dx, dy, dz, *args, **kwargs):
    '''Add an 3d arrow to an `Axes3D` instance.'''

    arrow = Arrow3D(x, y, z, dx, dy, dz, *args, **kwargs)
    ax.add_artist(arrow)
setattr(Axes3D,'arrow3D',_arrow3D)

## Code Start Here
plt.rcParams['figure.figsize'] = [20,13]
plt.rcParams.update({'font.size':18})

fig = plt.figure()
ax = fig.gca(projection='3d')

t = np.linspace(-2,2,20)
x = t.copy()
y = t.copy()
z = t.copy()
ax.plot(x,y,z,Color='b')
ax.plot(0,0,0,'o',Color='r')
ax.arrow3D(0,0,0,
           1,1,1,
           LineWidth=2,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
plt.grid('on')
plt.show()


fig = plt.figure()
ax = fig.gca(projection='3d')

s = np.linspace(-2,2,20)
t = np.linspace(-2,2,20)
x = t.copy()
y = t.copy()
z = t.copy()
ax.plot(x,y,z,Color='b')
ax.plot(0,0,0,'o',Color='r')
ax.arrow3D(0,0,0,
           1,1,1,
           LineWidth=2,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")

S,T = np.meshgrid(s,t)
X = -S-T
Y = S
Z = T
ax.plot_surface(X,Y,Z,Color='m',alpha=0.1)
plt.grid('on')
plt.show()










