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
glob_pattern_var = 'atm_2d_ml_'
## Define the paths
data_path1 = Path('/work/mh0287/m300083/experiments/dpp0066/')
## Collect all file names with pathlib's rglob and list compression  -- cloud liquid water \n",
files = sorted([str(f) for f in data_path1.glob(f'*{glob_pattern_var}*.nc')])[:] #Define a global pattern to find the files\n",

####variable to find
var='ts'

grid_file = '/work/mh0287/m300083/experiments/dpp0066/icon_grid_0015_R02B09_G.nc'
outfile = '/scratch/m/m300876/data/dpp0066/interp/ts/dpp0066_daily_ts_'
########

save_files = interp3d.get_data_2d(files[311:],var,0.25,0.25,grid_file,outfile,xini=-180., yini=-90., xend=180., yend=90., weights=None, better_times=True, resample_time = True, temporal_mean='1D')

