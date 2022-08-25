# 3D Visualizing Intro Script
# Anthony Semeraro
# Aug 07 2022

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

file_path = "/Users/anthonysemeraro/Documents/Code/Lidar/Lidar_Data/sample.xyz"

point_cloud = np.loadtxt(file_path, skiprows = 1)

mean_Z = np.mean(point_cloud, axis=0)[2]

spatial_query = point_cloud[abs(point_cloud[:,2]-mean_Z)<1]

xyz = spatial_query[:,:3]

rgb = spatial_query[:,3:]

ax = plt.axes(projection = '3d')

ax.scatter(xyz[:,0], xyz[:,1], xyz[:,2], c = rgb/255, s = 0.01)

plt.show()