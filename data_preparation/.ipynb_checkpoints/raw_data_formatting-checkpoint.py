print('here1')

# Standard libraries
import sys
import math
import random
import time
import os

# Third-party imports
# import numpy as np
import pandas as pd
# import pickle as pkl

# import tensorflow as tf

import multiprocess
import psutil

# Project imports
from .. import ephesos
import utils
import prep_utils

# Number of processes
NUM_OF_PROCESSES = 20

MAX_TIME_GAP = 10  
CADENCE = 2  
SPLINE_TYPE = 'cubic'

print('here')
REMOVE_TOI = False
TIC = pd.read_csv('../assets/TIC/INSERTTOICATALOGNAME')

STANDARD_LEN = 1901
MIN_LEN = 600


for sector_number in range(1, 27):

    # Gather the paths of the fits data
    paths = prep_utils.return_sector_paths(sector_number)

    with multiprocess.Pool(NUM_OF_PROCESSES) as pool:
        # Curves are the raw fits data

    ###
        # check if should be map_async vs map_sync or whatever
    ###
        curves = pool.map_async(utils.create_curves, paths).get()  

    # # Interpolate and Format Light Curves
    # for i in range(len(raw_fits_data)):
    #     # Insert 'inter_spot' for later interpolation
    #     curre_curve = utils.inser_inter_spot(raw_fits_data[i], max_time_gap, caden)
    #     # Interpolate each cut
    #     raw_fits_data[i] = utils.inter_curve(curre_curve, spln_type)

    # curve = tf.keras.preprocessing.sequence.pad_sequences(raw_fits_data,
    #                                                        padding='pre',
    #                                                        dtype=object)



