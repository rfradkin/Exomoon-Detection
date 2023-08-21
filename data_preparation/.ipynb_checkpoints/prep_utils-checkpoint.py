import os
from astropy.io import fits
import sys
import copy
import numpy as np
GENERAL_UTILS = '/home/rfradkin/Exomoon-Detection/utils'
sys.path.append(GENERAL_UTILS)
import utils


def return_sector_paths(sector_number):
    '''
    Returns a set of paths containing sectors of fits data from
    specified sector
    '''
    file_names = set()
    for file in os.listdir(f'../assets/fits_data/sector-{sector_number}'):
        # check if file already includes full path
        # don't remmeber, not sure
        file_names.add(f'../assets/fits_data/sector-{sector_number}/{file}')
    return file_names


def setup_curve(path):
    '''
    Import a TESS curve and setup for processing
    '''

    body_attributes = {
        'amplitude': None,
        'density': None,
        'eccentricity': None,
        'epoch': None,
        'inclination': None,
        'mass': None,
        'period': None,
        'radius': None,
        'sin_w': None,
        'signal': None,
        'signal_time': None,
        'snr': None,
        'transit_duration': None,
        'magnitude': None,
        'effective_temperature': None
    }

    cut_attributes = {
        'times': None,
        'transit': None,
        'number': None,
        'start_index': None
    }

    curve = {
        'injection_type': None, 
        'cut': cut_attributes,
        'data': None,
        'file_name': None,
        'injection_times': None,
        'interpolation_type': None,
        'initial_padding': None,
        'linear_limb_darkening_coefficient': None,
        'model_file': None,

        'planet': copy.deepcopy(body_attributes),
        'moon': copy.deepcopy(body_attributes),
        'star': copy.deepcopy(body_attributes),

        'planet_cut_injected': None,
        'planet_moon_cut_injected': None,

        'prediction': None,
        'quadratic_limb_darkening_coefficent': None,
        'ratio_moon_planet_radius': None,
        'ratio_moon_star_radius': None,
        'ratio_planet_star_radius': None,
        'raw_curve_length': None,
        'rms': None,
        'signal': None,
        'snr': None,
        'tic_id': None,
        'toi': None,
    }
    
    hdulist = fits.open(path)
    
    # Extract the data
    flux = hdulist[1].data['PDCSAP_FLUX']
    time = hdulist[1].data['TIME']
    
    hdulist.close()
    
    # Data array is an n by 2 array of type 
    # [[time1, flux1],
    #  [time2, flux2],
    #            ...]
    curve['data'] = np.column_stack((time, flux))
    curve['file_name'] = path.split('/')[-1]
    curve['tic_id'] = utils.return_TIC_id(path)
        
    return curve
