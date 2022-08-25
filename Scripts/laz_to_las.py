# .LAZ to ,LAS
# Anthony Semeraro
# Aug 06, 2022

# Reads in a .LAZ sipped las file, converts it to .LAS for use in geospatial analysis

# Import Libraries
import os
import laspy

os.chdir('/Users/anthonysemeraro/Documents/Career/Career_Developement/Lidar_Processing/intro_project')

# Reads in .LAZ file
las = laspy.read('King_2726_rp.laz')

# Converts .LAZ file to .LAS
las = laspy.convert(las)

# Writes new .LAS file
las.write('King_2726_rp.las')

print("Succesful conversion from .LAZ to .LAS")

#! DO NOT USE

#/// las = pylas.read('/Users/anthonysemeraro/Documents/Career/Career_Developement/Lidar_Processing/intro_project/King_2725_rp.laz')
#/// las = pylas.convert(las)
#/// las.write('/Users/anthonysemeraro/Documents/Career/Career_Developement/Lidar_Processing/intro_project/King_2725_rp.las')