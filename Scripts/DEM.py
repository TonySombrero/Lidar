# Dem Creation

# Creates a raster DEM from lidar point cloud datasets

import os
import numpy as np
import matplotlib.pyplot as plt
import rasterio as rio
from rasterio.plot import show
from rasterio.plot import show_hist
from shapely.geometry import Polygon, mapping
from rasterio.mask import mask
# a package created for this class that will be discussed later in this lesson
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep

# set home directory and download data
et.data.get_data("spatial-vector-lidar")
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))

# define path to digital terrain model
sjer_dtm_path = "data/spatial-vector-lidar/california/neon-soap-site/2013/lidar/SOAP_lidarDTM.tif"

# open raster data
lidar_dem = rio.open(sjer_dtm_path)
# optional - view spatial extent
lidar_dem.bounds
BoundingBox(left=296906.0, bottom=4100038.0, right=300198.0, top=4101554.0)

# plot the dem using raster.io
fig, ax = plt.subplots(figsize = (10,8))
show(lidar_dem,
     title="Lidar Digital Elevation Model (DEM) \n Boulder Flood 2013",
     ax=ax)
ax.set_axis_off()

# close the file connection
lidar_dem.close()

# open raster data connection - again
lidar_dem = rio.open(sjer_dtm_path)

fig, ax = plt.subplots(figsize = (10,10))
show(lidar_dem, 
     title="Once the connection is re-opened \nyou can work with the raster data", 
     ax=ax)
ax.set_axis_off()

lidar_dem.close()





