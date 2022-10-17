#!/usr/bin/env python

####importing packages
import sys
sys.path.append('/home/m/m300876/python/packages/')
import interp3d
from pathlib import Path
import importlib
import numpy as np

###preparing cpus
interp3d.prepare_cpu(memory='128GB')
####

##pattern of files
glob_pattern_var = 'atm_2d_ml_202002'
## Define the paths
data_path1 = Path('/work/mh0287/m300083/experiments/dpp0066/')
## Collect all file names with pathlib's rglob and list compression  -- cloud liquid water \n",
files = sorted([str(f) for f in data_path1.glob(f'*{glob_pattern_var}*.nc')])[:] #Define a global pattern to find the files\n",

####variable to find
var='pr'

grid_file = '/work/mh0287/m300083/experiments/dpp0066/icon_grid_0015_R02B09_G.nc'
outfile = '/scratch/m/m300876/data/dpp0066/dpp0066_hourly_pr_'
########

save_files = interp3d.get_data_2d(files,var,0.1,0.1,grid_file,outfile,xini=-180., yini=-30., xend=180., yend=30., weights='/scratch/m/m300876/weights/weight_file_0.1.nc', better_times=True, resample_time = True, temporal_mean='1H')

