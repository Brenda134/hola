# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:57:58 2020

@author: User
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
xpos = [1]
ypos = [2]
num_elements = len(xpos)
zpos = [0]
dx = 27
dy = 10
dz = [10]

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='pink')