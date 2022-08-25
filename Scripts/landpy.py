# Practice using Laspy

# Anthony Semeraro

# Aug 06, 2022

#%% Import Libraries
import os
import laspy
import pylas
import open3d as o3d
import numpy as np

# Sets working directory to file storage
os.chdir('/Users/anthonysemeraro/Documents/Code/Lidar/Lidar_Data')

# When using las, use read to read in all the points and metadata
# Use open to only view the metadata

las = laspy.read('King_2725_rp.las')

print(list(las.point_format.dimension_names))

print(set(list(las.classification)))

# Stacking x, y, z points to create a point cloud
point_data = np.stack([las.X, las.Y, las.Z], axis=0).transpose((1, 0))

# Filtering Point Clouds
#* bare_earth = laspy.create(point_format=las.header.point_format, file_version=las.header.version)
#* bare_earth.points = las.points[las.classification == 2]

# Write new .las file
#* bare_earth.write('bare_earth.las')

# Visualizing Point Clound using Open3D
geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)
o3d.visualization.draw_geometries([geom])
