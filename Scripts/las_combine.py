# Attempt to combine las files

import os
import pylas
import lastools

os.chdir('/Users/anthonysemeraro/Documents/Career/Career_Developement/Lidar_Processing/intro_project')

las2las -i King_2725_rp.las King_2726_rp.las  -merged -o Ballard.las